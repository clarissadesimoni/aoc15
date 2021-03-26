const fs = require('fs');
const input = fs.readFileSync("day7/day7.txt", 'utf-8').split('\n');
var data = input.map(line => line.split(' -> ')).reduce((acc, line) => {
    acc[line[1]] = line[0];
    return acc;
}, {});

var seen = {};

const operators = {
    NOT: (arg) => ~arg[1],
    AND: (arg) => arg[0] & arg[2],
    OR: (arg) => arg[0] | arg[2],
    LSHIFT: (arg) => arg[0] << arg[2],
    RSHIFT: (arg) => arg[0] >> arg[2]
}

function getWire(wire) {
    if (!isNaN(wire)) return +wire;
    if (wire in seen) return seen[wire];
    var cmd = data[wire].split(" ");
    var res = 0;
    if (cmd.length == 1) return getWire(cmd[0]);
    if (cmd.includes("NOT")) {
        cmd[1] = getWire(cmd[1]);
        res = operators["NOT"](cmd);
    }
    else {
        cmd[0] = getWire(cmd[0]);
        cmd[2] = getWire(cmd[2]);
        res = operators[cmd[1]](cmd);
    }
    seen[wire] = res;
    return res;
}

function part1() {
    return getWire('a');
}

function part2() {
    seen = {b: part1()};
    return getWire('a');
}

console.log("Part 1: " + part1());
console.log("Part 2: " + part2());