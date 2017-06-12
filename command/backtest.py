#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pylab import *
import pandas as pd

from base import CommandBase
from util.logger import Logger
from service.backtest.indicator import BacktestIndicator
from service.backtest.base import BacktestBase
from service.backtest.market import BacktestMarket
from service.backtest.fitting import BacktestFitting
from service.backtest.test import BacktestTest


logger = Logger()


class Command(CommandBase):

    def __init__(self):
        super(Command, self).__init__(description="バックテスト")
        self.parser.add_argument(
            "--training_start",
            # default="2015-08-25 21:55:00",
            default="2011-01-01",
            # default="2015-01-01",
            help="学習開始日時"
        )
        self.parser.add_argument(
            "--start",
            # default="2015-08-25 22:10:00",
            default="2013-01-01",
            # default="2015-01-01",
            help="取引開始日時"
        )
        self.parser.add_argument(
            "--end",
            # default="2015-08-25 22:10:00",
            default="2016-01-01",
            help="取引終了日時"
        )
        self.parser.add_argument(
            "--action_csv",
            default="data/action.csv",
            help="取引記録CSV出力ファイル名"
        )
        # self.parser.add_argument(
        #     "--csv",
        #     default="data/backtest.csv",
        #     help="出力CSVファイル名"
        # )
        # self.parser.add_argument(
        #     "--type",
        #     default=None,
        #     nargs="+",
        #     help="バックテストタイプ"
        # )


    def handle(self):
        self.training_start = self.parse_args.training_start
        self.start = self.parse_args.start
        self.end = self.parse_args.end
        self.action_csv = self.parse_args.action_csv
        # self.csv = self.parse_args.csv
        # self.type = self.parse_args.type

        backtest = BacktestIndicator(
            training_start=self.training_start,
            start=self.start,
            end=self.end,
            is_print_progress=True
        )

        # backtest = BacktestBase(
        #     training_start=self.training_start,
        #     start=self.start,
        #     end=self.end,
        #     is_print_progress=True
        # )

        # backtest = BacktestMarket(
        #     training_start=self.training_start,
        #     start=self.start,
        #     end=self.end,
        #     is_print_progress=True
        # )

        # backtest = BacktestFitting(
        #     training_start=self.training_start,
        #     start=self.start,
        #     end=self.end,
        #     is_print_progress=True,
        #     action_csv=self.action_csv
        # )

        # backtest = BacktestTest(
        #     training_start=self.training_start,
        #     start=self.start,
        #     end=self.end,
        #     is_print_progress=True
        # )

        backtest.run()


command = Command()
command.run()
