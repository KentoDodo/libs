#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

from logger import Logger


def output_csv(csvfile='output.csv', header=[], data=[]):
    """2次元配列`data`を指定ファイル`csvfile`にcsv形式で保存する"""

    f = open(csvfile, 'w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(header)
    writer.writerows(data)
    f.close()
    Logger().info("Output to csv file (%s)" % csvfile)


def input_csv(csvfile='output.csv'):
    """`csvfile`で指定したcsv形式ファイルを読み込む"""

    def isfloat(value):
        try:
            float(value)
            return True
        except:
            return False

    f = open(csvfile, 'r')
    reader = csv.reader(f)
    header = next(reader)
    data = [[(float(d) if isfloat(d) else d) for d in row] for row in reader]
    f.close()
    return header, data
