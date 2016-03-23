# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from pellish.padovanish import Padovanish


class PadovanishTest(unittest.TestCase):

    def setUp(self):
        self.fixture = Padovanish(3, 5, 20)

    def tearDown(self):
        del self.fixture

    def test_build_initial_series(self):
        p = self.fixture.build_initial_series()
        self.failUnlessEqual(
            [3, 3, 5, 6, 8, 11, 14, 19, ],
            p
        )

    def test_build_series(self):
        p = self.fixture.build_series([1, 1, 1])
        self.failUnlessEqual(
            [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, ],
            p
        )

    def test_build_next(self):
        s = self.fixture.build_initial_series()
        p = self.fixture.build_next(s)
        self.failUnlessEqual(
            [],
            p
        )

    def test_build_previous(self):
        s = self.fixture.build_initial_series()
        p = self.fixture.build_previous(s)
        self.failUnlessEqual(
            [],
            p
        )


if __name__ == '__main__':
    unittest.main()
