function reverse(array) {

    for (let i = array.length - 1; i >= array.length / 2; i--) {
        
        //temp = array[array.length - 1 - i] 
        [array[array.length - 1 - i], array[i]] = [array[i], array[array.length - 1 - i]]
        //array[i] = temp


    }

    return array;
}


let str = ['h','e','l','l','o', 'w', 'o', 'r', 'l', 'd'];
console.log(reverse(str));