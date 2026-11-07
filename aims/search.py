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
    return [
        item
        for item in items
        if hasattr(item, "title")
        and item.title
        and keyword.lower() in item.title.lower()
    ]
