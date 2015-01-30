#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'

from math import sqrt


class Pellish(object):

    def __init__(self, min_, req_, max_):
        if (min_ + 2 * req_) > max_:
            raise Exception('Invalid starting parameters.')
        self.req_ = req_
        self.max_ = max_
        self.min_ = min_
        self.fp = './pellish.csv'

    @property
    def longest_digit(self):
        return len(str(max(map(max, zip(*self.build_all_series()))))) + 1

    def build_series(self, a, b):
        """Create a Pellish series based on two initial values.

        :param float a: n_0
        :param float b: n_1
        :returns: 1-dimensional series of Pellish values
        :rtype: list
        """

        series = [a, b]

        while b <= self.max_:
            c = a + 2 * b
            series.append(c)
            a = b
            b = c

        return series[:-1]

    def build_initial_series(self):
        """Build initial series based on required, minimum, and maximum values.

        :returns: 1-dimensional series of initial Pellish values
        :rtype: list
        """

        b = self.req_

        if self.min_ == self.req_ or self.req_ == 3 * self.min_:
            a = b = self.min_
            return self.build_series(a, b)
        elif self.req_ < 3 * self.min_:
            a = self.min_
            return self.build_series(a, b)
        else:
            a = b / (1 + sqrt(2))
            a = round(a / self.min_) * self.min_
        xs = []

        while a >= self.min_:
            a_ = b - a * 2
            b = a
            a = a_
            if a > 0 and a not in xs:
                xs.append(a)
            if b > 0:
                if len(xs) <= 1 or b not in xs:
                    xs.append(b)

        xs = sorted(xs)

        return self.build_series(xs[0], xs[1])

    def build_all_series(self):
        """Build all series based on required, minimum, and maximum values.

        :returns: 2-dimensional array of Pellish values
        :rtype: list
        """

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

    def build_next(self, series):
        """Given a series, build the next series.

        :param list series: a Pellish series
        :return: the next Pellish series
        :rtype: list
        """
        a = series[1] - series[0]
        b = series[2] - series[1]
        return self.build_series(a, b)

    def build_previous(self, series):
        """Given a series, build the series two steps in front. Ie,
        given series[6], return series[4].

        :param list series: a Pellish series
        :return: the next Pellish series
        :rtype: list
        """
        a = series[0] / 2.
        b = series[1] / 2.
        return self.build_series(a, b)

    def get_minor_triplets(self):
        """Build all minor triplets in the 2-dimensional Pellish array.

        :return: a list of all minor triplets
        :rtype: list
        """
        triplets = []
        all_series = self.build_all_series()
        for i in range(len(all_series)):
            for j in range(len(all_series[i])):
                try:
                    t = [
                        all_series[i][j],
                        all_series[i][j + 1],
                        all_series[i + 1][j + 1],
                    ]
                    if None not in t:
                        triplets.append(sorted(t))
                except IndexError:
                    pass
        return sorted(triplets, key=lambda x: (x[0], x[1], x[2]))

    def get_major_triplets(self):
        """Build all major triplets in the 2-dimensional Pellish array.

        :return: a list of all major triplets
        :rtype: list
        """
        triplets = []
        all_series = self.build_all_series()
        for i in range(len(all_series)):
            for j in range(len(all_series[i])):
                try:
                    t = [
                        all_series[i][j],
                        all_series[i + 1][j],
                        all_series[i + 1][j + 1],
                    ]
                    if None not in t:
                        triplets.append(sorted(t))
                except IndexError:
                    pass
        return sorted(triplets, key=lambda x: (x[0], x[1], x[2]))

    def get_triplets(self):
        """Retrieve all triplets in the 2-dimensional Pellish array.

        :return: a list of all major triplets
        :rtype: list
        """
        return [
            self.get_minor_triplets(),
            self.get_major_triplets(),
        ]

    def get_diagonals(self):
        """Retrieve all diagonals in the 2-dimensional Pellish array.

        :return: a list of all diagonals
        :rtype: list
        """
        diagonals = []
        all_series = self.build_all_series()
        for i in range(len(all_series[0])):
            diagonal = [all_series[0][i], ]
            for j in range(1, len(all_series)):
                try:
                    x = all_series[j][i+j]
                    if x is not None:
                        diagonal.append(x)
                except IndexError:
                    pass
            if len(diagonal) > 1:
                diagonals.append(diagonal)
        return sorted(diagonals)

    def print_triplets(self, triplets, lb=True):
        """Pretty print triplets in three columns.

        :param list triplets: list of triplets to print
        :param bool lb: whether or not to include line breaks
        :return: pretty string
        :rtype: str
        """

        z = zip(*[
            [' '.join(
                [str(x).rjust(self.longest_digit, ' ')
                 if x is not None
                 else ''.rjust(self.longest_digit, ' ')
                 for x in t])
             for t in triplets[:int(len(triplets)/3.)]],
            [' '.join(
                [str(x).rjust(self.longest_digit, ' ')
                 if x is not None
                 else ''.rjust(self.longest_digit, ' ')
                 for x in t])
             for t in triplets[int(len(triplets)/3.):int(len(triplets)/3.*2)]],
            [' '.join(
                [str(x).rjust(self.longest_digit, ' ')
                 if x is not None
                 else ''.rjust(self.longest_digit, ' ')
                 for x in t])
             for t in triplets[int(len(triplets)/3.*2):]],
        ])
        return '{}'.format('\n' if lb else '    ')\
            .join(['{}    {}    {}'.format(a, b, c)
                   for a, b, c in z])

    def print_diagonals(self, diagonals, lb=True):
        """Print diagonals horizontally.

        :param list triplets: list of triplets to print
        :param bool lb: whether or not to include line breaks
        :return: pretty string
        :rtype: str
        """
        return '{}'.format('\n' if lb else ', ').join([' '.join(
            [str(x).rjust(self.longest_digit, ' ')
             if x is not None
             else ''.rjust(self.longest_digit, ' ')
             for x in t]) for t in diagonals])

    def write_csv(self):
        """Write Pellish array to a CSV file.

        :return: None
        :rtype: None
        """
        pell = self.build_all_series()
        with open('{}'.format(self.fp), 'w') as f:
            for s in pell:
                for x in s:
                    f.write('{},'.format(x if x is not None else ''))
                f.write('\n')


def main():

    from colorama import init, Fore, Style

    init(autoreset=True)

    def create_args():
        import argparse
        parser = argparse.ArgumentParser(
            description='Creates Pell-like series of numbers based on user-supplied minimum, maximum, and required values.'
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
        me_group = parser.add_mutually_exclusive_group()
        me_group.add_argument(
            '-t', '--triplets', action='store_true',
            help='Show triplets instead of matrix',
        )
        me_group.add_argument(
            '-d', '--diagonals', action='store_true',
            help='Show diagonals instead of matrix',
        )

        return parser.parse_args()

    args = create_args()

    p = Pellish(args.minimum, args.required, args.maximum)

    if args.csv:
        if args.file:
            p.fp = args.file
        p.write_csv()
    else:
        try:

            if not args.diagonals and not args.triplets:

                for s in p.build_all_series():
                    print(' '.join(
                        [str(x).rjust(p.longest_digit, ' ')
                         if x is not None
                         else ''.rjust(p.longest_digit, ' ')
                         for x in s]))

            if args.triplets:
                minor, major = p.get_triplets()
                print('##############')
                print(Style.BRIGHT + 'Minor triplets')
                print('##############')
                print(p.print_triplets(minor))
                print('##############')
                print('Major triplets')
                print('##############')
                print(p.print_triplets(major))

            if args.diagonals:
                print('#########')
                print('Diagonals')
                print('#########')
                print(p.print_diagonals(p.get_diagonals()))

        except:
            raise Exception('Creation of Pellish series failed. Miserably.')


if __name__ == '__main__':
    main()