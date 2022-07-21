'use strict';
console.log(`====================  FUNCTION  ====================

`)
// TO set default params' val 
const showMessage = (message, from = 'unknown') => log(`${message} by ${from}`);
showMessage('hi','jinsoo');
showMessage('hi');

const printAll = (a,b,...arr) => log(a,b,...arr);
printAll(1,2,[3,4,5],4,5);
log(1,2,3,4,5);
log(1,2,[3,4,5]);
console.log(1,2,[3,4,5]);
