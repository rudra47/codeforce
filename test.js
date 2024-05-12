let length = 6;
let a = [4, 5, 6, 7, 8, 9].sort((a, b) => a - b);
let b = [1, 2, 3, 4, 5, 6].sort((a, b) => a - b);

let result = 0;

for (let i = 0; i < length; i++) {
    if (a[i] > b[i]) {
        a.splice(i, 0, b[i]);

        a = a.sort((x, y) => x - y)

        result += 1;
    }
}

console.log(result);