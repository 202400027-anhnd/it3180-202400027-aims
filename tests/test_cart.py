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

class TestCartDiscount(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", cost=100.0))

    def test_discount_calculation(self):
        self.assertAlmostEqual(
            self.cart.total_cost_with_discount(20), 80.0, places=2
        )

    def test_invalid_discount_percent(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)

if __name__ == '__main__':
    unittest.main()
