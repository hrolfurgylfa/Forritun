# Verkefni 2

1.  ```javascript
    let manneskja = {
        nafn: "Jón Jónsson",
        kennitala: 2505004790,
        heimilisfang: "Bæjargata 22",
        heimasími: 5550357,
        farsími: 7385023
    };
    ```
2.  ```javascript
    for (let eiginleiki in manneskja) {
        console.log(eiginleiki + ": " + manneskja[eiginleiki])
    }
    ```
3.  ```javascript
    let manneskja = {
        nafn: "Jón Jónsson",
        aldur: 18,// Það var enginn aldur í lið 1 svo að ég bætti honum bara við hérna svo að ég gæti kallað í hann
        kennitala: 2505004790,
        heimilisfang: "Bæjargata 22",
        heimasími: 5550357,
        farsími: 7385023,
        nafnOgAldur: function() {
            console.log(this.nafn);
            console.log(this.aldur);
        }
    };
    ```
4.  ```javascript
    console.log(family.parents.fathers[1].name);
    ```
5.  ```javascript
    let breakfast = {
        name: "The Lumberjack",
        price: 9.95,
        ingredients: ["eggs", "sausage", "toast", "hashbrowns", "pancakes"]
    };
    ```
6.  ```javascript
    var savingsAccount = {
        balance: 1000,
        interestRatePercent: 1,
        deposit: function addMoney(amount) {
            if (amount > 0) {
                savingsAccount.balance += amount;
            }
        },
        withdraw: function removeMoney(amount) {
            var verifyBalance = savingsAccount.balance - amount;
            if (amount > 0 && verifyBalance >= 0) {
                savingsAccount.balance -= amount;
            }
        },
        // your code goes here
        printAccountSummary: function() {
            let strengur = 
            "Welcome!\nYour balance is currently $"
            + String(savingsAccount.balance)
            + " and your interest rate is "
            + String(savingsAccount.interestRatePercent)
            + "%.";
            return strengur;
        }
    };

    console.log(savingsAccount.printAccountSummary());
    ```
7.  ```javascript
    donuts.forEach(kleinuhringur => {
        console.log(kleinuhringur.type+" donuts cost $"+kleinuhringur.cost+" each");
    });
    ```
8. Ég fann ekkert um þetta sama hversu mikið ég leitaði.
9. Fyrst er object-ið `{name:"John"}`, svo er breytan `user` búin til og svo er breytan `user` látin vísa á object-ið. Í næstu línu þá er breytan `admin` búin til og látin vísa á það sama og breytan `user` er að vísa á og þá vísa báðar breyturnar á sama object-ið og þess vegna þegar maður breytir einu þá breytist hitt líka.
10. Þetta virkar vegna þess að const gerir breytuna óbreytanlega en þegar það er bætt við `user.age` þá er verið að breyta object-i sem breytan vísar á og breytan er allveg eins og hún var, það eina sem breyttist var object-ið sem breytan vísar á.
