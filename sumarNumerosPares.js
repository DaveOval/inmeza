function sumarNumerosPares(numeros) {
    let sum = 0;
    for (const num of numeros) {
        if (num % 2 === 0) {
            sum += num;
        }
    }
    return sum;
}


const input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const output = sumEvenNumbers(input);
console.log(output); 