#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt


class IntegerSequence(object):

    def __init__(self, min_, req_, max_):
        self.req_ = req_
        self.max_ = max_
        self.min_ = min_
        self.n_shape = 1
        self.bootstrap = None
        self.fp = './sequence.csv'

    @property
    def longest_digit(self):
        """Length of longest number in series.

        Used to format command line output.

        :return: Length of longest number
        :rtype: int
        """
        return len(str(max(map(max, zip(*self.build_all_series()))))) + 1

    def f(self, arr):
        """The basic operation in the sequence.

        :param arr: The sequence of nubers to operate on.
        :type arr: list
        :return: The next number in the series.
        :rtype: float
        """
        return arr[-1] + 1

    def f_reverse(self, arr):
        """The basic operation in the sequence reversed.

        :param arr: The sequence of nubers to operate on.
        :type arr: list
        :return: The previous number in the series.
        :rtype: float
        """
        return arr[0] - 1

    def bootstrap_a(self, val):
        """Find previous value in series, w.r.t. val.

        :param val: Arbitrary vale in series
        :type val: float
        :return: Previous value in series
        :rtype: float
        """
        if self.bootstrap is None:
            return self.f_reverse([val])
            raise Exception('This sequence has no bootstrap value.')
        return round(
            (val / self.bootstrap) / self.min_
        ) * self.min_

    def o(self, x):
        return self.f(x)

    def build_series(self, arr):

        series = arr
        l = len(arr)

        while series[-1] <= self.max_:
            x = self.o(arr)
            series.append(x)
            arr = series[-l:]

        return series[:-1]

    def build_initial_series(self):
        """Build initial series based on required, minimum, and maximum values.

        :returns: 1-dimensional series of initial values
        :rtype: list
        """

        b = self.req_
        c = self.f([self.min_ for i in range(self.n_shape)])

        if self.min_ == self.req_:
            a = b = self.min_
            return self.build_series([self.min_ for i in range(self.n_shape)])

        if self.req_ == c:
            a = b = self.min_
            return self.build_series([self.min_ for i in range(self.n_shape)])

        if self.req_ < c:
            a = self.min_
            arr = [self.min_ for i in range(self.n_shape)]
            arr[-1] = b
            return self.build_series(arr)

        return self.build_series(self.find_initial_a(b))

    def find_initial_a(self, b):
        a = self.bootstrap_a(b)
        series = []

        while a > self.min_:
            a_ = self.f_reverse([a, b])
            b = a
            a = a_
            if a >= self.min_ and a not in series:
                series.append(a)
            if b > 0:
                if len(series) <= 1 or b not in series:
                    series.append(b)

        series = sorted(series)
        return series[:self.n_shape]

    def build_next(self, series):
        a = series[1] - series[0]
        b = series[2] - series[1]
        if a == series[0] and b == series[1]:
            return []
        if a == series[1] and b == series[2]:
            return []
        return self.build_series([a, b])

    def build_previous(self, series):
        a = series[0] - 1.
        b = series[0]
        return self.build_series([a, b])

    def build_all_series(self):

        all_series = []
        s = self.build_initial_series()

        while len(s) > 2:
            all_series.append(s)
            s = self.build_next(s)

        if len(all_series) > 1:
            while all_series[0][1] >= all_series[0][0] >= self.min_:
                s = self.build_previous(all_series[1])
                all_series.insert(0, s)

        for series in all_series:
            if 0 < series[0] < self.min_:
                all_series.remove(series)

        all_series = [[int(x) if self.min_ % 1 == 0 else x
                      for x in s] for s in all_series]

        l = len(max(all_series, key=len))
        for i in range(len(all_series)):
            for j in range(i):
                all_series[i].insert(0, None)
            for j in range(l - len(all_series[i])):
                all_series[i].insert(len(all_series[i]), None)

        return all_series

    def write_csv(self):
        """Write sequence to a CSV file.

        :return: None
        :rtype: None
        """
        series = self.build_all_series()
        with open('{}'.format(self.fp), 'w') as f:
            for s in series:
                for x in s:
                    f.write('{},'.format(x if x is not None else ''))
                f.write('\n')