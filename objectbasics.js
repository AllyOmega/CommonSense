function sumOfTripledEvens(array) {

    return array 
        .filter((num) => num % 2 === 0)
        .map((num) => num * 3 )
        .reduce((total, currentItem) => total + currentItem, 0);

}

console.log(sumOfTripledEvens([1, 2, 3, 4,5, 6]));