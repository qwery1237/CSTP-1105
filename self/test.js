'use strict';
const binary = -0b1111011;
console.log(binary);

// +(data) => data type to num

// !!(data) => data type to boolean
const narcissistic = value => String(value).split('').map(el => value.length)//.reduce((crr,acc) => crr+acc) 
const test = narcissistic(7)
console.log(test)