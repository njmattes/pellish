# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from pellish.sequence import IntegerSequence


class SequenceTest(unittest.TestCase):

    def setUp(self):
        self.fixture = IntegerSequence(0., 4., 10.)

    def tearDown(self):
        del self.fixture

    def test_build_initial_series(self):
        p = self.fixture.build_initial_series()
        self.failUnlessEqual(
            [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.],
            p
        )

    def test_build_series(self):
        p = self.fixture.build_series([1])
        self.failUnlessEqual(
            [1., 2., 3., 4., 5., 6., 7., 8., 9., 10.],
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
            [-1., 0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.],
            p
        )


if __name__ == '__main__':
    unittest.main()
