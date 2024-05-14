let length = 2 * 3;
let array = [1, 1, 1, 1, 1, 1].sort((a, b) => a - b);

let result = 0;

for (let i = 0; i < length; i++) {
    let prevIndex = i;
    if (array[i] <= array[i++]) {
        result += array[prevIndex];
    }
}

console.log(result);