#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from math import sqrt
from pellish.sequence import IntegerSequence


__version__ = '0.0.1'


class Padovanish(IntegerSequence):

    def __init__(self, min_, req_, max_):
        # FIXME: These are pellish starting parameters
        if max_ / (3 + 2 * sqrt(2)) < min_ and (min_ + 2 * req_) > max_:
            raise Exception('Invalid starting parameters.')
        super(Padovanish, self).__init__(min_, req_, max_)
        self.fp = './padovanish.csv'
        self.n_shape = 3
        self.bootstrap = (
            ((9 - sqrt(69)) ** (1/3) + (9 + sqrt(69)) ** (1/3)) /
            (2 ** (1/3) * 3 ** (2/3))
        )

    def f(self, arr):

        return arr[0] + arr[1]

    def f_reverse(self, arr):

        return arr[2] - arr[0]

    def build_initial_series2(self):

        d = self.req_
        if self.req_ == self.min_:
            b = d
            c = d
            a = d
        else:
            b = d / self.bootstrap ** 2
            c = d / self.bootstrap
            b = round(b / self.min_) * self.min_
            c = round(c / self.min_) * self.min_
            a = d - b

        series = [a, b, c]
        # print(series)
        # print(c - a, self.min_)

        while c - a > self.min_:

            a_ = c - a
            c = b
            b = a
            a = a_

            if a > 0 and a not in series:
                series.append(a)
            if b > 0:
                if len(series) <= 1 or b not in series:
                    series.append(b)
            if c > 0:
                if len(series) <= 2 or c not in series:
                    series.append(c)

        series = sorted(series)

        return self.build_series(series[:3])

    # def build_all_series(self):
    #
    #     return [self.build_initial_series()]

    def write_csv(self):
        pell = self.build_all_series()
        with open('{}'.format(self.fp), 'w') as f:
            for s in pell:
                for x in s:
                    f.write('{},'.format(x if x is not None else ''))
                f.write('\n')


def main():

    def create_args():
        import argparse
        parser = argparse.ArgumentParser(
            description='Creates Padovan-like series of numbers based on user-supplied minimum, maximum, and required values.'
        )
        parser.add_argument(
            'minimum', type=float,
            help='Minimum number in all series. minimum > 0')
        parser.add_argument(
            'required', type=float,
            help='At least one series must contain this value. required > minimum.')
        parser.add_argument(
            'maximum', type=float,
            help='Maximum value for numbers in all series. maximum >= required')
        parser.add_argument(
            '-c', '--csv', action='store_true',
            help='Write values to CSV file instead of stdout')
        parser.add_argument(
            '-f', '--file', type=str,
            help='Path to CSV file')

        return parser.parse_args()

    args = create_args()

    p = Padovanish(args.minimum, args.required, args.maximum)

    if args.csv:
        if args.file:
            p.fp = args.file
        p.write_csv()
    else:
        try:

            for s in p.build_all_series():
                print(' '.join([
                    str(int(x) if p.min_ % 1 == 0 else x)
                        .rjust(p.longest_digit, ' ')
                    if x is not None
                    else ''.rjust(p.longest_digit, ' ')
                    for x in s
                ]))

        except:
            print('Creation of Padovanish series failed. Miserably.')


if __name__ == '__main__':
    p = Padovanish(3, 52, 100)
    print(p.build_all_series())

    # main()