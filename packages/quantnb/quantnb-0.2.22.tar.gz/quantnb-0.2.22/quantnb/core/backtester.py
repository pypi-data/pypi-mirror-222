from cycler import mul
import numpy as np
from quantnb.core.enums import OrderType
import numpy as np
import numba as nb
from numba import float32, int32, int64
from numba import from_dtype, njit

from typing import List

dt = np.dtype([("x", np.float32), ("y", np.float32)])
nb_dt = from_dtype(dt)


@nb.experimental.jitclass
class Backtester:
    # DATA
    open: float32[:]
    high: float32[:]
    low: float32[:]
    close: float32[:]
    volume: float32[:]
    date: int64[:]

    # Bid Ask Data
    bid: float32[:]
    ask: float32[:]

    # PORTFOLIO
    initial_capital: float32
    cash: float32
    final_value: float32
    total_pnl: float32
    multiplier: float32
    equity: float32[:]
    default_size: float32

    # TRADE MANAGEMENT
    in_position: nb.boolean
    stop_loss: float32
    entry_time: int32
    entry_size: float32
    entry_price: float32
    current_trade_type: int32
    commission: float32
    commission_type: str
    slippage: float32
    slippage_type: str

    # MISC
    order_idx: int32
    trade_idx: int32
    orders: float32[:, :]
    trades: float32[:, :]
    final_trades: float32[:, :]

    # TRADE MANAGEMENT
    active_trades: float32[:, :]
    closed_trades: float32[:, :]
    number_of_closed_trades: int32

    # POSITION MANAGEMENT
    total_volume: float32
    weighted_sum: float32
    average_price: float32

    # GENERAL
    prev_percentage: float32

    def __init__(
        self,
        initial_capital=10000,
        commission=0.0,
        commission_type="percentage",
        multiplier=1,
        default_size=None,
        slippage=None,
        slippage_type="fixed",
    ):
        # PORTFOLIO
        self.cash = initial_capital
        self.initial_capital = initial_capital
        self.final_value = initial_capital
        self.total_pnl = 0.0
        self.multiplier = multiplier
        if default_size is not None:
            self.default_size = default_size

        if slippage is not None:
            self.slippage = slippage
        self.slippage_type = slippage_type

        # TRADE MANAGEMENT
        self.in_position = False
        self.stop_loss = 0
        self.entry_time = 0
        self.entry_size = 0
        self.entry_price = 0
        self.commission = commission
        self.commission_type = commission_type

        # MISC
        self.order_idx = 0
        self.trade_idx = 0

        # POSITION MANAGEMENT
        self.total_volume = 0
        self.weighted_sum = 0

    def set_bid_ask_data(self, date, bid, ask, volume=None):
        # DATA
        self.date = date
        self.bid = bid
        self.ask = ask
        self.close = bid
        if volume is not None:
            self.volume = volume

        self.set_general()

    def set_data(self, open, high, low, close, date):
        # DATA
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.date = date

        self.set_general()

    def set_general(self):
        # PORTFOLIO
        self.equity = np.empty(len(self.close), dtype=float32)
        self.equity[0] = self.cash

        # MISC
        self.orders = np.zeros((len(self.close), 5), dtype=float32)
        self.trades = np.zeros((len(self.close), 8), dtype=float32)

    # ===================================================================================== #
    #                                       HELPERS                                         #
    # ===================================================================================== #

    @staticmethod
    def calculate_fees(price, size, commission, commission_type):
        if commission_type == "percentage":
            return price * size * commission
        else:
            return commission

    # ===================================================================================== #

    #                                POSITION MANAGEMENT                                    #
    # ===================================================================================== #
    def new_order(self, i, order_type, close):
        self.orders[self.order_idx, :] = [
            i,
            order_type.value,
            close,
            self.entry_size,
            self.cash,
        ]
        self.order_idx += 1

    def go_long(self, price, i):
        # self.entry_size = self.cash / self.close[i]

        fee = self.calculate_fees(
            price, self.entry_size, self.commission, self.commission_type
        )
        self.cash -= self.entry_size * price - fee

        self.new_order(i, OrderType.LONG, price)

        self.entry_time = self.date[i]
        # print(f"Entry time: {self.entry_time}")
        self.entry_price = price
        self.in_position = True

        self.current_trade_type = OrderType.LONG.value

    def go_short(self, i):
        close = self.close[i]

        fee = self.calculate_fees(
            close, self.entry_size, self.commission, self.commission_type
        )
        self.cash -= self.entry_size * close - fee

        self.new_order(i, OrderType.SHORT, close)

        self.entry_time = self.date[i]
        # print(f"Entry time: {self.entry_time}")
        self.entry_price = close
        self.in_position = True

        self.current_trade_type = OrderType.LONG.value

    def close_position(self, i, exit_price):
        close = self.close[i]

        fee = self.calculate_fees(
            close, self.entry_size, self.commission, self.commission_type
        )
        # print("closing position")
        # print(self.cash)
        # print(self.cash)

        order_type = OrderType.LONG
        if self.current_trade_type == OrderType.LONG.value:
            order_type = OrderType.SHORT
        self.new_order(i, order_type, close)

        if self.commission_type == "percentage":
            print("need to update commissions calculation of percentage trades")
            entry_fee = self.entry_price * self.entry_size * self.commission
        elif self.commission_type == "fixed":
            fee = fee * 2

        pnl = (exit_price - self.entry_price) * self.entry_size * self.multiplier - fee
        self.cash += self.entry_size * exit_price - fee
        self.total_pnl += pnl

        self.trades[self.trade_idx, :] = [
            self.entry_time,
            self.date[i],
            self.entry_price,
            exit_price,
            pnl,
            fee,
            self.entry_size,
            self.current_trade_type,
        ]
        self.trade_idx += 1
        self.entry_size = 0
        self.in_position = False

    # ===================================================================================== #
    #                                       CORE BACKTESTER                                 #
    # ===================================================================================== #
    def from_signals(
        self, entry_signals, exit_signals, sl=None, use_sl=False, mode=1, debug=False
    ):
        close = self.close
        stop_loss = 0

        if debug:
            print("Backtest launched")

        for i in range(1, len(close)):
            if debug:
                print(f"========== {i}")
            if entry_signals[i]:
                if not self.in_position:
                    # print("GOING LONG")
                    if use_sl and sl is not None:
                        stop_loss = sl[i]

                    self.entry_size = self.cash / self.close[i]
                    if self.default_size is not None:
                        self.entry_size = self.default_size
                    self.go_long(self.close[i], i)

            elif exit_signals[i]:
                if self.in_position:
                    self.close_position(i, close[i])

            if use_sl and self.in_position:
                if mode == 1:
                    if close[i] < stop_loss:
                        self.close_position(i, self.open[i + 1])
                elif mode == 2:
                    if self.low[i] < stop_loss:
                        self.close_position(i, stop_loss)

            fee = self.calculate_fees(
                close[i], self.entry_size, self.commission, self.commission_type
            )
            if self.commission_type == "percentage":
                print("missing")
            else:
                fee = fee * 2
            # pnl = 0
            # for j in range(0, self.trade_idx):
            #     pnl += self.trades[j, 4]
            self.equity[i] = self.initial_capital + self.total_pnl

        self.final_value = self.equity[-1]

    def add_position(self, price, volume):
        self.total_volume += volume
        self.weighted_sum += price * volume
        self.average_price = self.weighted_sum / self.total_volume

    def remove_position(self, price, volume):
        self.total_volume -= volume
        self.weighted_sum -= price * volume
        if self.total_volume > 0:
            self.average_price = self.weighted_sum / self.total_volume
        else:
            self.average_price = 0

    def backtest_bid_ask(
        self,
        entry,
        exit,
        entry_volume,
        exit_volume,
        sl=None,
        use_sl=False,
        mode=1,
        debug=False,
    ):
        self.close = self.bid
        bid = self.bid

        if debug:
            print("Backtest launched")

        for i in range(1, len(bid)):
            if debug:
                print(f"========== {i}")
            # if entry_volume[i] > 0:
            #     print(entry_volume[i])
            if entry[i]:
                self.entry_size = entry_volume[i]
                self.go_long(self.ask[i], i)
                self.add_position(bid[i], entry_volume[i])
                print("========== GOING LONG")
                print("volume", entry_volume[i])
            if exit[i]:
                print("========== Close Position")
                print(self.cash)

                self.close_position(i, bid[i])
                self.remove_position(bid[i], exit_volume[i])

            fee = self.calculate_fees(
                bid[i], self.total_volume, self.commission, self.commission_type
            )
            self.equity[i] = self.cash + self.total_volume * bid[i] - fee

        print("========== DONE =========")
        print(self.average_price)
        print(self.total_volume)
        self.final_value = self.equity[-1]

    def from_orders(self, size):
        close = self.bid
        for i in range(len(self.bid)):
            volume = size[i]
            if volume != 0:
                # If the volume is positive, then we take from buy and take the ask price
                if volume > 0:
                    price = self.ask[i]
                else:
                    price = self.bid[i]

                self.total_volume += volume
                self.weighted_sum += price * volume
                self.average_price = self.weighted_sum / self.total_volume

            self.equity[i] = (
                self.cash + (self.average_price - close[i]) * self.weighted_sum
            )

            # if self.equity[i] < 99994.02:
            #     print("ASD")

        print(self.weighted_sum)

    def was_trade_filled(self, i, ohlc, last_trade, last_trade_index=None, debug=False):
        tick = ohlc[i]
        next_tick = ohlc[i + 1]

        # print("==========")
        # print(last_trade)
        # print(tick)
        if tick < last_trade <= next_tick:
            # The order will be placed on the next tick
            # new_array[i] = [next_tick, vol[last_trade_index]]
            # last_trade_index += 1
            return True

        elif last_trade < tick:
            if debug:
                print("Skippped tick", last_trade_index, last_trade, tick, next_tick, i)
            # new_array[i] = [tick, vol[last_trade_index]]
            # last_trade_index += 1
            return True
        else:
            # new_array[i] = [tick, 0]
            return False

    def update_trades_pnl(self, index, active_trades):
        for trade in active_trades:
            direction = trade[1]
            trade_price = trade[3]

            commission = 0
            trade_volume = trade[6]
            if self.commission_type == "fixed":
                commission = self.commission

            if direction == 1:  # LONG
                price = self.ask[index]
                pnl = (price - trade_price) * trade_volume - commission
            else:
                price = self.bid[index]
                pnl = (trade_price - price) * trade_volume - commission

            self.trades[int(trade[0])][7] = pnl

    def calculate_exit_price(self, trade, index):
        direction = trade[1]
        if direction == 1:  # LONG
            exit_price = self.bid[index]
        else:
            exit_price = self.ask[index]
        return exit_price

    def calculate_trade_exit_pnl(self, trade, exit_price):
        direction = trade[1]
        trade_price = trade[3]
        trade_volume = trade[6]

        commission = 0
        if self.commission_type == "fixed":
            commission = self.commission

        if direction == 1:  # LONG
            pnl = (exit_price - trade_price) * trade_volume - commission
        else:
            pnl = (trade_price - exit_price) * trade_volume - commission
        return pnl

    def check_trades_to_close(self, current_tick, index):
        for trade in self.active_trades:
            trade_exit = trade[4]
            if trade_exit < current_tick:
                # print("need to close trade")
                exit_price = self.calculate_exit_price(trade, index)

                new_trade = trade
                new_trade[9] = False
                new_trade[5] = exit_price
                new_trade[7] = self.calculate_trade_exit_pnl(trade, exit_price)

                self.trades[int(trade[0])] = new_trade

                self.closed_trades[self.number_of_closed_trades] = new_trade

                realized_pnl = 0
                for trade in self.closed_trades:
                    realized_pnl += trade[7]
                self.total_pnl = realized_pnl

                self.number_of_closed_trades += 1
                self.update_active_trades()

    def update_active_trades(self):
        # Extract the last column (assuming it contains boolean values)
        last_column = self.trades[:, -1]
        mask = last_column == True
        self.active_trades = self.trades[mask]

    def update_equity(self, index, active_trades):
        pnl = 0
        for trade in active_trades:
            # if index > 20008:
            #     print(pnl, "  --  ", trade[7])
            pnl += trade[7]

        # if index > 20008:
        #     print(self.cash, self.total_pnl, pnl)

        self.equity[index] = self.cash + self.total_pnl + pnl

    # def from_trades(self, trades, progress_proxy):
    def print_bar(self, length, fill, iteration, total):
        percentage = iteration * 100 / total
        if percentage - self.prev_percentage > 10:
            progress = iteration / float(total)
            filled_length = int(length * progress)
            bar = fill * filled_length + "-" * (length - filled_length)
            print(np.round(percentage), f"% | {bar} |")
            self.prev_percentage = percentage
            # print(f"\r{prefix} |{bar}| {progress:.1%}", end=end)

    def from_trades(self, trades):
        last_trade_index = 0
        close = self.bid

        """
        A trade row contains the following:
        ["Index", "Direction", "EntryTime", "EntryPrice", "ExitTime", "ExitPrice", "Volume", "TP", "SL", "PNL", "Commission", "Active"]
        """
        self.trades = np.zeros((len(trades), 10), dtype=float32)
        self.closed_trades = np.zeros((len(trades), 10), dtype=float32)
        self.number_of_closed_trades = 0

        self.prev_percentage = 0

        for i in range(len(self.bid)):
            self.print_bar(40, "█", i, len(self.bid))
            curr_trade = trades[last_trade_index]

            if last_trade_index < len(trades):
                self.update_trades_pnl(i, self.active_trades)
                self.check_trades_to_close(self.date[i], i)
                self.update_equity(i, self.active_trades)

                if self.was_trade_filled(i, self.date, curr_trade[0], debug=False):
                    entry_time = curr_trade[0]
                    exit_time = curr_trade[1]
                    volume = curr_trade[2]
                    direction = curr_trade[3]

                    if direction == 1:
                        price = self.ask[i]
                    else:
                        price = self.bid[i]

                    commission = 0
                    if self.commission_type == "fixed":
                        commission = self.commission
                    self.trades[last_trade_index] = [
                        last_trade_index,
                        direction,
                        entry_time,
                        price + self.slippage,
                        exit_time,  # Exit Time
                        -1,  # Exit Price
                        volume,
                        0,  # PNL
                        commission,  # Need to implement commission
                        True,
                    ]
                    # print("Entering a trade")
                    last_trade_index += 1
                    self.update_active_trades()

        self.trades = self.trades[:last_trade_index]
        self.closed_trades = self.closed_trades[: self.number_of_closed_trades]
