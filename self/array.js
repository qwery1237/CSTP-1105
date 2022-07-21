'use strict';
console.clear();
console.log(`====================  ARRAY  ====================

`)
const arr1 = [1,2,3]
arr1.forEach(el => console.log(el));
arr1.push(4,5);     // add el at the end    
arr1.pop();         // delete el at the end
arr1.unshift(0)     // add el at the beginnig
arr1.shift(0)        // delete el at the beginning
log(arr1)
arr1.splice(1, 1,'two')       // (start , numOfDelete, ...add )
log(arr1)
arr1.lastIndexOf(3) // <===> indexOf(3)`
arr1[1] = 2;
log(arr1);
const arr2 = arr1.map(el => el*2);
log(arr1,arr2);