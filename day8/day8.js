const fs = require('fs');
const input = fs.readFileSync("day8/day8.txt", 'utf-8').split('\n');

function part1() {
    return input.map(function(string) {
        var i = 0, code = 0, memory = 0
        const hexChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'];
        while (i < string.length) {
            if (string[i] == '\\') {
                if (string[i + 1] == 'x' && hexChars.includes(string[i + 2]) && hexChars.includes(string[i + 3])) {
                    memory += 3;
                    i += 3;
                } else {
                    memory += 1;
                    i += 1;
                }
            } else if (string[i] == '\"') code -= 1;
            code += 1;
            memory += 1;
            i += 1;
        }
        return memory - code;
    }).reduce((a, b) => a + b, 0);
}

function part2() {
    return input.map(function(string) {
        var i = 0, encoded = 0, memory = 0
        const hexChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'];
        while (i < string.length) {
            if (string[i] == '\\') {
                if (string[i + 1] == 'x' && hexChars.includes(string[i + 2]) && hexChars.includes(string[i + 3])) {
                    memory += 3;
                    encoded += 4;
                    i += 3;
                } else {
                    memory += 1;
                    encoded += 3;
                    i += 1;
                }
            } else if (string[i] == '\"') encoded += 2;
            encoded += 1;
            memory += 1;
            i += 1;
        }
        return encoded - memory;
    }).reduce((a, b) => a + b, 0);
}

console.log("Part 1: " + part1());
console.log("Part 2: " + part2());