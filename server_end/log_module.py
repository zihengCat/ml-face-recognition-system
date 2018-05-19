import os
import sys
import random
import json
import csv
import time
# 日志数据结构 =>
# [日期, 时间, 用户, 门号, 状态]
class Logs():
    def __init__(self):
        self.logpath = os.path.join(sys.path[0], 'logs/records.csv')
        self.logdata = [ ]
        f = open(self.logpath)
        f_csv = csv.reader(f)
        for r in f_csv:
            self.logdata.append(r)
        f.close()
        # 存盘指示器
        self.saver = 0
    # API 函数：数据落盘
    def dataSaver(self):
        if(self.saver == 1):
            f = open(self.logpath, 'wt')
            f_csv = csv.writer(f)
            f_csv.writerows(self.logdata)
            f.close()
    # 提取日志数据（全提取）
    def showRow(self, uid = None):
        return self.logdata
    # 添加日志数据
    def addRow(self, u_obj):
        if u_obj['uid'] == 'noface':
            # 没有识别到人脸，直接返回
            return
        else:
            row = [
                time.strftime("%Y-%m-%d", time.localtime()),
                time.strftime("%H:%M:%S", time.localtime()),
                '1',
                u_obj['uid'],
                'warning' if u_obj['uid'] == 'unknown' else 'passing'
            ]
            self.logdata.append(row)
            self.saver = 1
            self.dataSaver()
    # 删除日志数据
    def delRow(self, uid = None):
        pass

