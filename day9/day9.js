const fs = require('fs');
const input = fs.readFileSync("day9/day9.txt", 'utf-8').split('\n');

function listOccurrences(string, substring) {
    var count = [];
    if (string.includes(substring)) for (var i = 0; i < string.length; i++) if (string.slice(i).startsWith(substring)) count.push(i);
    return count;
}

function permutations(array, r) {
    var n = array.length;
    if (r === undefined) r = n;
    if (r > n) return;
    var indices = [];
    for (var i = 0; i < n; i++) indices.push(i);
    var cycles = [];
    for (var i = n; i > n - r; i--) cycles.push(i);
    var results = [];
    var res = [];
    for (var k = 0; k < r; k++) res.push(array[indices[k]]);
    results.push(res);
    var broken = false;
    while (n > 0) {
        for (var i = r - 1; i >= 0; i--) {
            cycles[i]--;
            if (cycles[i] === 0) {
                indices = indices.slice(0, i).concat(indices.slice(i + 1).concat(indices.slice(i, i + 1)));
                cycles[i] = n - i;
                broken = false;
            } else {
                var j = cycles[i];
                var x = indices[i];
                indices[i] = indices[n - j];
                indices[n - j] = x;
                var res = [];
                for (var k = 0; k < r; k++) res.push(array[indices[k]]);
                results.push(res);
                broken = true;
                break;
            }
        }
        if (broken === false) break;
    }
    return results;
}

function parseString(s) {
    var res = s.split(' ');
    res.splice(1, 3, res[2]);
    res[2] = parseInt(res[2]);
    return res;
}

var data = input.map(l => parseString(l));
rides = data.reduce(function(acc, curr) {
    acc[curr[0]] = {};
    acc[curr[1]] = {};
    return acc;
}, {});

data.forEach(function(line) {
    rides[line[0]][line[1]] = line[2];
    rides[line[1]][line[0]] = line[2];
});

var cities = Object.keys(rides);
var perm = permutations(cities, cities.length);
var costs = perm.map(p => p.reduce(function(acc, curr, i) {return acc + (i == cities.length - 1 ? 0 : rides[curr][p[i + 1]]);}, 0))

function part1() {
    return Math.min(...costs);
}

function part2() {
    return Math.max(...costs);
}

console.log("Part 1: " + part1());
console.log("Part 2: " + part2());