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