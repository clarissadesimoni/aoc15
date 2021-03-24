const fs = require('fs');
const input = fs.readFileSync("day3/day3.txt", 'utf-8');

function part1() {
    var x = 0, y = 0;
    var res = new Set();
    res.add("0, 0");
    for (var i = 0; i < input.length; i++) {
        if (input[i] == '^') {
            y++;
        } else if (input[i] == 'v') {
            y--;
        } else if (input[i] == '>') {
            x++;
        } else if (input[i] == '<') {
            x--;
        }
        res.add(x + ", " + y);
    }
    return res.size;
}

function part2() {
    var x = [0, 0], y = [0, 0];
    var res = new Set();
    res.add("0, 0");
    for (var i = 0; i < input.length; i++) {
        if (input[i] == '^') {
            y[i % 2]++;
        } else if (input[i] == 'v') {
            y[i % 2]--;
        } else if (input[i] == '>') {
            x[i % 2]++;
        } else if (input[i] == '<') {
            x[i % 2]--;
        }
        res.add(x[i % 2] + ", " + y[i % 2]);
    }
    return res.size;
}

console.log("Part 1: " + part1());
console.log("Part 2: " + part2());