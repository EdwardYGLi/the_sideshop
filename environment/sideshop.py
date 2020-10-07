"""
Created by Edward Li at 10/6/20
"""

import numpy as np

class SideShop:
    def __init__(self, bench_size = 5, counter_size = 9, starting_money = 1000):
        self.bench_size = bench_size
        self.counter_size = counter_size
        self.starting_money = starting_money

        self.bench = [None] * bench_size
        self.counter = [None] * counter_size

    def action(self, action):
        pass

    def refresh_bench(self):
        pass
