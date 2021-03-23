const fs = require('fs');
var input = fs.readFileSync("day1/day1.txt", 'utf-8');

function part1() {
    var res = 0;
    for(var i = 0; i < input.length; i++) {
        if (input.charAt(i) === '(') res++;
        else if (input.charAt(i) === ')') res--;
    }
    return res;
}

function part2() {
    var res = 0;
    var i = 0;
    for(i = 0; i < input.length; i++) {
        if (res === -1) break;
        if (input.charAt(i) === '(') res++;
        else if (input.charAt(i) === ')') res--;
    }
    return i;
}

console.log("Part 1:" + part1());
console.log("Part 2:" + part2());