MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        #print("The disc has been added")
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def print_cart(self):
        """In danh sách các item trong giỏ hàng kèm theo tổng chi phí."""
        print("\n=======================CART=======================")
        print("Ordered Items:")
        if not self.items:
            print("The cart is empty")
        else:
            for idx, item in enumerate(self.items, 1):
                print(f"{idx}. {item}")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("==================================================")

    def total_cost_with_discount(self, percent):
        total = self.total_cost()
        if percent < 0 or percent > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        return total - (total * percent / 100)

    def sort_by_title(self):
        self.items.sort(key=lambda item: item.title.lower())

    def sort_by_cost(self):
        self.items.sort(key=lambda item: (item.cost, item.title.lower()))
