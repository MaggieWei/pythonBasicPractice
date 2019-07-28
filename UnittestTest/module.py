# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 15:43
# @Author  : 魏芳萤
# 实现简单计算器：加减乘除


class Calculator:
    """实现两个数的加减乘除"""
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b
