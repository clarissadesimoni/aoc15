const fs = require('fs');
const input = fs.readFileSync("day2/day2.txt", 'utf-8').split('\n');

class Box {
    constructor(line) {
        var items = line.split("x");
        this.length = +items[0];
        this.width = +items[1];
        this.height = +items[2];
        this.areas = [this.length * this.width, this.length * this.height, this.width * this.height];
        this.surface = 2 * this.areas.reduce((a, b) => a + b) + Math.min(...this.areas);
    }
}

function getBoxSurface(line) {
    var items = line.split("x");
    length = +items[0];
    width = +items[1];
    height = +items[2];
    areas = [length * width, length * height, width * height];
    return 2 * areas.reduce((a, b) => a + b) + Math.min(...areas);
}

function part1() {
    return input.map(l => getBoxSurface(l)).reduce((a, b) => a + b);
}

function getRibbon(line) {
    var items = line.split("x").map(d => +d);
    items.sort((a, b) => a - b);
    return items.reduce((a, b) => a * b) + (2 * (items[0] + items[1]))
}

function part2() {
    return input.map(l => getRibbon(l)).reduce((a, b) => a + b);
}

console.log("Part 1:" + part1());
console.log("Part 2:" + part2());