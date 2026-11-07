import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCartLimit(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()

        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}")
            self.assertTrue(cart.add_dvd(dvd))

        extra_dvd = DigitalVideoDisc("Extra DVD")
        self.assertFalse(cart.add_dvd(extra_dvd))

if __name__ == '__main__':
    unittest.main()
