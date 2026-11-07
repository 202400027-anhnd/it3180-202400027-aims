import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.dvd1 = DigitalVideoDisc(
            "The Lion King", "Animation", "Roger Allers", 87, 19.95
        )
        self.dvd2 = DigitalVideoDisc(
            "Star Wars", "Science Fiction", "George Lucas", 87, 24.95
        )
        self.dvd3 = DigitalVideoDisc(
            "Aladdin", "Animation", "John Musker", 90, 18.99
        )
        self.items = [self.dvd1, self.dvd2, self.dvd3]

    def test_search_by_category(self):
        results = search_by_category(self.items, "Animation")
        self.assertEqual(len(results), 2)
        self.assertIn(self.dvd1, results)
        self.assertIn(self.dvd3, results)

    def test_search_by_category_case_insensitive(self):
        results = search_by_category(self.items, "animation")
        self.assertEqual(len(results), 2)


if __name__ == "__main__":
    unittest.main()
