import unittest
from datetime import timedelta

def convert(num):
    return TimeAmount(num)


class TimeAmount(object):
    units = {
        'days': 24 * 60 * 60,
        'hours': 60 * 60,
        'minutes': 60,
        'seconds': 1,
    }

    def __init__(self, amount, unit=None):
        self.amount, self.unit = amount, unit

    def __getattr__(self, attr):
        if attr in self.units:
            if self.unit:
                return self.convert(attr)
            else:
                return TimeAmount(self.amount, attr)

    @property
    def to(self):
        return self

    def convert(self, to_unit):
        seconds = self.units[self.unit] * self.amount
        return seconds / self.units[to_unit]


class Tests(unittest.TestCase):
    def test_minutes_to_seconds(self):
        self.assertEquals(convert(5).minutes.to.seconds, 5 * 60)
        self.assertEquals(convert(3).days.to.minutes, 3 * 24 * 60)
        self.assertEquals(convert(4).minutes.to.seconds, 4 * 60)
        self.assertEquals(convert(5).minutes.to.minutes, 5)


if __name__ == '__main__':
    unittest.main()