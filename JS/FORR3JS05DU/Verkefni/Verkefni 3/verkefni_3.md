# Verkefni 3

1.  Objectar eru tengdir saman með `__proto__` og ef það finnst ekki eitthvað í objecti sem maður leitar að þá fer forritið að leita í næsta objecti í `__proto__` keðjuni.
2.  ```javascript
    function Book(isbn) {// Hérna er fall sem verður notað sem constructorinn fyrir objecta
        this.isbn = isbn;// Þetta setir breytu í nýju objectana sem heitir isbn og er sama gildi og breytan sem kom inn með fallinu
    }
    Book.prototype.getIsbn = function () {// Þessari function er bætt við í prototype á Book og það er það sem er notað til þess að gera __proto__ þegar það er notað new svo að þessi function mun bætast við í __proto__ á öllum nýjum objectum sem eru búnit til úr fallinu Book
        return "Isbn is " + this.isbn;
    };
    let bookObject = new Book(12345);// Þessi lína býr til nýja let breytu sem er undefined og bætir svo nýjum object úr fallinu Book í breytuna
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
4.  ```javascript
    // A
    class Geimflaug {
        constructor(nafn) {
            this.nafn = nafn;
            this.speed = 10;
            this.life = 10;
        }
        // C
        fly() { this.speed += 1; }
    }

    let f1 = new Geimflaug("SSE Cydonia");
    let f2 = new Geimflaug("HMS Deonida");
    let f3 = new Geimflaug("ISS Covenant");

    // B
    f1.speed = 4;
    f2.speed = 7;
    f3.speed = 11;

    // D
    f1.setLife = () => this.life += 1;
    ```
5.  Það er enginn munur á `class` og `prototype` nema bara útlit, javascript compilerinn breytir `class` í `prototype` þegar hann compilar kóðann en það er samt mun betra að horfa á `class`.