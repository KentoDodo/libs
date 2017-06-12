#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


class CommandBase(object):
    """
    コマンド基本クラス
    これを継承してコマンドを作成する。継承先クラスは、run()の中身を実装する。
    """

    def __init__(self, description=None):
        self.description = description
        self.parser = self._parser()

    def _parser(self):
        parser = argparse.ArgumentParser(description=self.description)
        return parser

    @property
    def parse_args(self):
        return self.parser.parse_args()

    def run(self):
        self.parse_args
        self.before_handle()
        self.handle()
        self.after_handle()

    def handle(self, **kwargs):
        print "This is define handle(). You should implement handle()."

    def before_handle(self):
        print "=" * 75

    def after_handle(self):
        print "=" * 75
