'use strict';
console.log(`====================  OBJECT  ====================

`)

const obj1 = {};
const obj2 = new Object;

// add element
obj1.add = true;

// delete element
delete obj1.add;



// Object의 공통 인자들을 파라미터로 받고 this.params = params;
// The first letter of the function name need to be uppercase;
// const variable = new func(...params);

// property value shorthand
const person1 = { name : 'bob', age: 2};
const person2 = { name : 'steve', age: 3};
const person3 = { name : 'dave', age: 4};
const person4 = new Person3('jinsoo',25);
const person5 = new Person3('yu',24);
console.log(person4);

// constructor function
function Person3(name,age) {
    this.name = name;
    this.age = age;
}

// in operator (key in Obj);
log('name' in person4); // true
log('gender' in person4); // false
console.clear(); // clear the console

//
const person6 = person5; // 같은 Ref 할당
//
const person7 = Object.assign({},person5); // 값만참조해옴 깊은 복사
log(person7.name);                         //yu
person6.name = 'hatoyama';
log(person5.name);                         //hatoyama
log(person7.name);                         //yu
