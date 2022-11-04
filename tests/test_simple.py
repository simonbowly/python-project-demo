import unittest

import hatch_demo_simon_bowly


class Test(unittest.TestCase):
    def test_simple(self):
        hatch_demo_simon_bowly.do_the_thing()
