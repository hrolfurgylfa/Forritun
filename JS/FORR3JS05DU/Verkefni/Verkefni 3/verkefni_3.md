# Verkefni 3

1.  Objectar eru tengdir saman með prototype og ef það finnst ekki eitthvað í objecti sem maður leitar að þá fer forritið að leita í objectinum fyrir ofan.
2.  ```javascript
    function Book(isbn) {// Hérna er fall sem verður notað sem constructorinn
        this.isbn = isbn;//Þetta setir það sem kom inn í síðasta object (this) og .isbn
    }
    Book.prototype.getIsbn = function () {
        return "Isbn is " + this.isbn;
    };
    let bookObject = new Book(12345);
    ```
3.  
    1.  