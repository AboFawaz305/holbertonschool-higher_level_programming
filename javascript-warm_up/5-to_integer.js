#!/usr/bin/node
const argv = process.argv;
const num = Number.parseInt(argv[2], 10);
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
