class Book:
    def __init__(self, title, author, publisher, price, copies_sold):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._copies_sold = copies_sold

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher
    
    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value

    @property
    def copies_sold(self):
        return self._copies_sold
    
    @copies_sold.setter
    def copies_sold(self, value):
        self._copies_sold = value

    def royalty(self):
        royalty_amount = 0
        if self._copies_sold <= 5:
            royalty_amount = 0.10 * self._price * self._copies_sold
        elif self._copies_sold <= 1005:
            royalty_amount = (0.10 * 5 * self._price) + (0.125 * self._price * (self._copies_sold - 5))
        else:
            royalty_amount = (0.10 * 5 * self._price) + (0.125 * 1000 * self._price) + (0.15 * self._price * (self._copies_sold - 1005))
        return royalty_amount


class Ebook(Book):
    def __init__(self, title, author, publisher, price, copies_sold, format_type):
        super().__init__(title, author, publisher, price, copies_sold)
        self._format_type = format_type

    @property
    def format_type(self):
        return self._format_type
    
    @format_type.setter
    def format_type(self, value):
        self._format_type = value

    def overall_royalty(self):
        royalty_amount = super().royalty()
        gst = 0.12 * royalty_amount
        total_royalty = royalty_amount - gst
        return total_royalty


def main():
    # Creating a Book object
    book = Book("Python Programming", "John Doe", "Publisher A", 25.99, 500)
    print("Book Royalty:", book.royalty())

    # Creating an Ebook object
    ebook = Ebook("Python Programming (Ebook)", "John Doe", "Publisher A", 19.99, 1500, "PDF")
    print("Ebook Royalty (After GST):", ebook.overall_royalty())

if __name__ == "__main__":
    main()
