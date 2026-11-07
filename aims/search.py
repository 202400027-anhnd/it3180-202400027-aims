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