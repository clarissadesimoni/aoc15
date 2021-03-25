const fs = require('fs');
const input = fs.readFileSync("day6/day6.txt", 'utf-8').split('\n');

function part1() {
    var grid = Array.from({length: 1000}, () => (Array.from({length: 1000}, () => (0))));
    input.forEach(function(line) {
        var items = line.split(" ");
        if (items[0] == "turn") items.splice(0, 2, items[0] + " " + items[1]);
        items.splice(2, 1);
        items[1] = items[1].split(",").map(s => +s);
        items[2] = items[2].split(",").map(s => +s);
        switch(items[0]) {
            case "toggle":
                for (var i = items[1][1]; i <= items[2][1]; i++)
                    for (var j = items[1][0]; j <= items[2][0]; j++)
                        grid[i][j] = grid[i][j] == 0 ? 1 : 0;
                break;
            case "turn on":
                for (var i = items[1][1]; i <= items[2][1]; i++)
                    for (var j = items[1][0]; j <= items[2][0]; j++)
                        grid[i][j] = 1;
                break;
            case "turn off":
                for (var i = items[1][1]; i <= items[2][1]; i++)
                    for (var j = items[1][0]; j <= items[2][0]; j++)
                        grid[i][j] = 0;
                break;
        }
    });
    return grid.map(l => l.reduce((a, b) => a + b, 0)).reduce((a, b) => a + b, 0);
}

function part2() {
    var grid = Array.from({length: 1000}, () => (Array.from({length: 1000}, () => (0))));
    input.forEach(function(line) {
        var items = line.split(" ");
        if (items[0] == "turn") items.splice(0, 2, items[0] + " " + items[1]);
        items.splice(2, 1);
        items[1] = items[1].split(",").map(s => +s);
        items[2] = items[2].split(",").map(s => +s);
        switch(items[0]) {
            case "toggle":
                for (var i = items[1][1]; i <= items[2][1]; i++)
                    for (var j = items[1][0]; j <= items[2][0]; j++)
                        grid[i][j] += 2;
                break;
            case "turn on":
                for (var i = items[1][1]; i <= items[2][1]; i++)
                    for (var j = items[1][0]; j <= items[2][0]; j++)
                        grid[i][j] += 1;
                break;
            case "turn off":
                for (var i = items[1][1]; i <= items[2][1]; i++)
                    for (var j = items[1][0]; j <= items[2][0]; j++)
                        grid[i][j] = Math.max(0, grid[i][j] - 1);
                break;
        }
    });
    return grid.map(l => l.reduce((a, b) => a + b, 0)).reduce((a, b) => a + b, 0);
}

console.log("Part 1: " + part1());
console.log("Part 2: " + part2());