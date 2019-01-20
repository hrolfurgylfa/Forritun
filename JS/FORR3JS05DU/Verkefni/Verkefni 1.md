# Spurningar

1. Null og undefinded eru bæði til þess að geyma breytu fyrir notkun seinna og eru svipaðar að flestu leiti nema það að þegar maður býr til breytu án þess að seta gildi þá verður hún undefinded en maður þarf að gera breitu að null.
2. Use strict gerir það að verkum að javascript interpreterinn hjálpar ekki með stafsetninguna heldur ef þú skrifar villu þá hættir hann í staðin fyrir að reyna að laga villuna, eins og ef maður gleimir semíkommu.
3. const geymir eitthvað sem er ekki hægt að breyta, let geymir breitu sem hægt er að breyta en ef maður skilgreinir hana inni í if eða for þá er bara hægt að nota breytuna þar og var er gamalt út ES5 og virkar eins og let nema það að það spáir ekki í því hvort að það sé búið til inni í if eða for eða ekki. 
4. ```javascript
   for (let x = 9; x >= 1; x -= 1) {
      console.log("hello " + x)
   }
   ```
5. 
   1. ```javascript
      function a(a) {
         return "a"
      }
      ```
   2. ```javascript
      let b = function(b) {
         return "b"
      }
      ```
   3. ```javascript
      let c = function c() {
         return "c"
      }
      ```
6. Þetta er gamall kóði úr ES5 og það sem hann gerir er að passa að breytur sem eru búnar til þarna eyðist þegar kóðinn er búinn að keyra þetta en það þarf ekki lengur að gera þetta því að let gerir þetta núna inni í svigum. 
   ```javascript
   (// Þetta opnar sviga sen verður svo notaður til þess að keyra nafnlausa fallið
      function() {// Þetta býr til nafnlaust fall
         alert('Hello World');// Þetta setir glugga á skjáinn sem segir Hello World
      }
   )
   ();// Þetta keyrir fallið inni í sviganum sem kom á undan og endar svo statement-ið
   ```
7. a er enþá 1 þegar það er prentað út vegna þess að það var breytt því inni í falli og aldrei skilað svo að það fór aftur í 1 þegar það var farið útúr fallinu og a er ekki fall vegna þess að það er skilað úr fallinu b áður en það er náð að búa til fallið a.
   Kóðinn raðaður rétt fyrir JS þýðandann:
   ```javascript
   "use strict";
   let a = 1;// Breytan a búin til sem 1
   b();// Fallið b keyrt
   // Farið inn í fall 1
      a = 10;// a breitt í 10 á meðan það er inni í fallinu
      return;// Hérna er farið útúr fallinu svo að fallið a er aldrei búið til og a var aldrei skilað aftur svo að það er enþá 1
   console.log(a);// a prentað út og það er enþá 1 hérna
   ```
8. ```javascript
   var test = [12, 929, 11, 3, 199, 1000, 7, 1, 24, 37, 4,
      19, 300, 3775, 299, 36, 209, 148, 169, 299,
      6, 109, 20, 58, 139, 59, 3, 1, 139
   ];

   // Write your code here
   let test2 = [];

   test.forEach(function(tala, numer){
      if (tala % 3 === 0){
         tala += 100;
      }
      test2.push(tala)
   });
   test = test2

   console.log(test);
   ```
9. ```javascript
   let bills = [50.23, 19.12, 34.01,
      100.11, 12.15, 9.90, 29.11, 12.99,
      10.00, 99.22, 102.20, 100.10, 6.77, 2.22
   ];
   let totals = bills.map(function(tala){
      tala = tala + tala * .15
      return Number(tala.toFixed(2))
   })
   console.log(totals);
   ```
10. ```javascript
    function a(){
       a();
    }
    a();
    ```