function Book(isbn) {// Hérna er fall sem verður notað sem constructorinn fyrir objecta
    this.isbn = isbn;// Þetta setir breytu í nýju objectana sem heitir isbn og er sama gildi og breytan sem kom inn með fallinu
}
Book.prototype.getIsbn = function () {// Þessari function er bætt við í prototype á Book og það er það sem er notað til þess að gera __proto__ þegar það er notað new svo að þessi function mun bætast við í __proto__ á öllum nýjum objectum sem eru búnit til úr fallinu Book
    return "Isbn is " + this.isbn;
};
let bookObject = new Book(12345);// Þessi lína býr til nýja let breytu sem er undefined og bætir svo nýjum object úr fallinu Book í breytuna