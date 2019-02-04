function Book(isbn) {// Hérna er fall sem verður notað sem constructorinn
    this.isbn = isbn;//Þetta setir það sem kom inn í síðasta object (this) og .isbn
}
Book.prototype.getIsbn = function () {
    return "Isbn is " + this.isbn;
};
let bookObject = new Book(12345);