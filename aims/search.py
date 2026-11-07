def search_by_category(items, category):
    if not category:
        return []
    return [
        item
        for item in items
        if hasattr(item, "category")
        and item.category
        and category.lower() == item.category.lower()
    ]


def search_by_title(items, keyword):
    if not keyword:
        return []
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
