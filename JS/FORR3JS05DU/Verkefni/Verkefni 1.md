# Spurningar

1. Null og undefinded eru bæði til þess að geyma breytu fyrir notkun seinna og eru svipaðar að flestu leiti nema það að þegar maður býr til breytu án þess að seta gildi þá verður hún undefinded en maður þarf að gera breitu að null
2. Use strict gerir það að verkum að javascript interpreterinn hjálpar ekki með stafsetninguna heldur ef þú skrifar villu þá hættir hann í staðin fyrir að reyna að laga villuna, eins og ef maður gleimir semíkommu.
3. k
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
8. k
9. k
10. ```javascript
    function a(){
       a();
    }
    a();
    ```