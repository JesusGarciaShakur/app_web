class Pagination:
    def __init__(self, items, page, per_page):
        self.items = items
        self.page = page
        self.per_page = per_page

    @property
    def total_pages(self):
        return (len(self.items) - 1) // self.per_page + 1

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.total_pages

    @property
    def prev_num(self):
        return self.page - 1 if self.has_prev else None

    @property
    def next_num(self):
        return self.page + 1 if self.has_next else None

    def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
        last = 0
        for num in range(1, self.total_pages + 1):
            if num <= left_edge or (self.page - left_current - 1 < num < self.page + right_current) or num > self.total_pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num

    def iter_pages_grouped(self, group_size=5):
        last = 0
        for num in range(1, self.total_pages + 1, group_size):
            yield num