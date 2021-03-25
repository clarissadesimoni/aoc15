const fs = require('fs');
const input = fs.readFileSync("day5/day5.txt", 'utf-8').split('\n');

function listOccurrences(string, substring) {
    var count = [];
    if (string.includes(substring)) for (var i = 0; i < string.length; i++) if (string.slice(i).startsWith(substring)) count.push(i);
    return count;
}

function contains3vowels(string) {
    return ['a', 'e', 'i', 'o', 'u'].map(v => listOccurrences(string, v).length).reduce((a, b) => a + b, 0) >= 3;
}

function containsDoubles(string) {
    var alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    for (var a of alphabet) if (listOccurrences(string, a + a).length >= 1) return true;
    return false;
}

function containsNoNaughty(string) {
    return ['ab', 'cd', 'pq', 'xy'].every(n => !string.includes(n));
}

function isNice1(string) {
    return contains3vowels(string) && containsDoubles(string) && containsNoNaughty(string);
}

function containsRepeatingCouple(string) {
    var found = false;
    for (var i = 0; i < string.length - 1; i++) {
        var occ = listOccurrences(string, string.slice(i, i + 2));
        occ = occ.filter(o => !occ.includes(o - 1));
        found = occ.length - 1 > 0;
        if (found) break;
    }
    return found;
}

function containsAlternatingLetter(string) {
    var found = false;
    for (var i = 0; i < string.length - 2; i++) {
        found = string[i] == string[i + 2];
        if (found) break;
    }
    return found;
}

function isNice2(string) {
    return containsRepeatingCouple(string) && containsAlternatingLetter(string);
}

function part1() {
    return input.filter(l => isNice1(l)).length;
}

function part2() {
    return input.filter(l => isNice2(l)).length;
}

console.log("Part 1: " + part1());
console.log("Part 2: " + part2());