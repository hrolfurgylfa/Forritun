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
    1.  ```javascript
        let geimflaug = {
            life: 10,
            speed: 10
        }
        function GeimflaugaConstructor (nafn) {
            this.nafn = nafn;
        }
        GeimflaugaConstructor.prototype = geimflaug;

        let f1 = new GeimflaugaConstructor("SSE Cydonia");
        let f2 = new GeimflaugaConstructor("HMS Deonida");
        let f3 = new GeimflaugaConstructor("ISS Covenant");
        ```
    2.  ```javascript
        f1.speed = 4;
        f2.speed = 7;
        f3.speed = 11;
        ```
    3.  ```javascript
        geimflaug.fly = function() {
            this.speed += 1;
        }
        ```
    4.  ```javascript
        f1.setLife = function() {
            this.life += 1;
        }
        ```
4.  
5.  Það er enginn munur á `class` og `prototype` nema bara útlit, javascript compilerinn breytir `class` í `prototype` þegar hann compilar kóðann en það er samt mun betra að horfa á `class`.