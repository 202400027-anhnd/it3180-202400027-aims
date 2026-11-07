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

class TestCartSorting(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.dvd1 = DigitalVideoDisc(
            "Star Wars", "Science Fiction", "George Lucas", 87, 24.95
        )
        self.dvd2 = DigitalVideoDisc(
            "Aladdin", "Animation", "John Musker", 90, 18.99
        )
        self.dvd3 = DigitalVideoDisc(
            "The Lion King", "Animation", "Roger Allers", 87, 19.95
        )

        self.cart.add_dvd(self.dvd1)
        self.cart.add_dvd(self.dvd2)
        self.cart.add_dvd(self.dvd3)

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        titles = [item.title for item in self.cart.items]
        self.assertEqual(titles, ["Aladdin", "Star Wars", "The Lion King"])

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        costs = [item.cost for item in self.cart.items]
        self.assertEqual(costs, [18.99, 19.95, 24.95])

if __name__ == '__main__':
    unittest.main()
