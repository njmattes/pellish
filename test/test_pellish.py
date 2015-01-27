# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from pellish.pellish import Pellish


class PellishTest(unittest.TestCase):

    def setUp(self):
        self.fixture = Pellish()
        self.fixture.min_ = .5
        self.fixture.max_ = 5
        self.fixture.p = 3.5

    def tearDown(self):
        del self.fixture

    def test_build_initial_series(self):
        p = self.fixture.build_initial_series()
        self.failUnlessEqual(
            [0.5, 1.5, 3.5],
            p
        )

    def test_build_series(self):
        p = self.fixture.build_series(1, 2)
        self.failUnlessEqual(
            [1.0, 2.0, 5.0],
            p
        )

    def test_build_next(self):
        s = self.fixture.build_initial_series()
        p = self.fixture.build_next(s)
        self.failUnlessEqual(
            [1, 2, 5],
            p
        )

    def test_build_previous(self):
        s = self.fixture.build_initial_series()
        p = self.fixture.build_previous(s)
        self.failUnlessEqual(
            [.25, .75, 1.75, 4.25],
            p
        )

    def test_get_minor_triplets(self):
        t = self.fixture.get_minor_triplets()
        self.failUnlessEqual(
            [[.5, .5, 1.0],
             [.5, 1.0, 1.5],
             [1.0, 1.5, 2.5],
             [1.5, 2.0, 3.5],],
            t
        )

    def test_get_major_triplets(self):
        t = self.fixture.get_major_triplets()
        self.failUnlessEqual(
            [[.5, 1.0, 1.5],
             [1.0, 1.5, 2.0],
             [1.5, 2.5, 3.5],
             [2.0, 3.5, 5.0],],
            t
        )

    def test_get_triplets(self):
        t = self.fixture.get_triplets()
        self.failUnlessEqual(
            [[[.5, .5, 1.0],
              [.5, 1.0, 1.5],
              [1.0, 1.5, 2.5],
              [1.5, 2.0, 3.5],],
             [[.5, 1.0, 1.5],
              [1.0, 1.5, 2.0],
              [1.5, 2.5, 3.5],
              [2.0, 3.5, 5.0],],],
            t
        )

    def test_get_diagonals(self):
        d = self.fixture.get_diagonals()
        self.failUnlessEqual(
            [[.5, .5, 1.0],
             [1.0, 1.5, 2.0],
             [2.5, 3.5, 5.0],],
            d
        )


if __name__ == '__main__':
    unittest.main()
