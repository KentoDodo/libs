#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


class LogText():
    u"""ログのテキストを管理するクラス"""

    def __init__(self, text):
        self.text = text

    def color(self, color):
        self.text = "\x1b[1;%dm%s\x1b[0m" % (color, self.text)
        return self

    def black(self):
        return self.color(color=30)

    def red(self):
        return self.color(color=31)

    def green(self):
        return self.color(color=32)

    def yellow(self):
        return self.color(color=33)

    def blue(self):
        return self.color(color=34)

    def magenta(self):
        return self.color(color=35)

    def cyan(self):
        return self.color(color=36)

    def white(self):
        return self.color(color=37)


class Logger():
    u"""ログ出力のためのクラス"""

    def _print(self, text):
        sys.stderr.write(text)
        sys.stderr.flush()

    def _print_w_time(self, text):
        self._print("[%s] %s" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text))


    def start(self, description):
        self._print_w_time("%s ..." % description)


    def end(self, text):
        self._print("%s\n" % (text))

    def success(self):
        self.end(LogText("success").green().text)

    def failed(self):
        self.end(LogText("failed").red().text)


    def info(self, description):
        self._print_w_time("%s\n" % description)
