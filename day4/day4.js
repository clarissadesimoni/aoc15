const fs = require('fs');
const CryptoJS = require('crypto-js');
const input = fs.readFileSync("day4/day4.txt", 'utf-8');

function part1() {
    var i = 1;
    while (!CryptoJS.MD5(input + i).toString().startsWith("00000")) i++;
    return i;
}

function part2() {
    var i = 1;
    while (!CryptoJS.MD5(input + i).toString().startsWith("000000")) i++;
    return i;
}

console.log("Part 1: " + part1());
console.log("Part 2: " + part2());