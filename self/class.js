'use strict';

console.log(`====================  CLASS  ====================
 
`)
// class { fields , methods } template

// object instance of a class

// 1. Class declarations
class Person {
    //constructor
    constructor(name, age) {
        //fields
        this.name = name;
        this.age = age;
    }

    // methods
    speak() {
        console.log(`${this.name}: hello!`);
    }

}
const jinsoo = new Person('jinsoo',20);
console.log(jinsoo.name);
console.log(jinsoo.age);
jinsoo.speak();

// 2. Getter and setters
class User {
    constructor(firstName, lastName, age) {
        this.firstName = firstName ;
        this.lastName = lastName;
        this.age = age;
    }
    get age() {
        return this._age;
    }
    set age(value) {
        this._age = value < 0 ? 0 : value;
    } 
}

const user1 = new User('jinsoo','son',-21);
const user2 = new User('jinsu','son',25)
console.log(user1.age)                      // 0
console.log(user2.age)                      // 25

// not common but new

// Fields (public, private)
class Experiment  {
    constructor (a,b){
        this.publicField = a;
        this.#privateField = b;
        console.log(this.#privateField);    // 2
        console.log(this.privateField);     // undefined 
    }
    publicField = 0;                //  Can access outside of the function
    #privateField = 1;              //  Can not access outside of the function
}
const experiment = new Experiment(1,2);
console.log(experiment.privateField)        // undefined

// Static properties and methods    // 모든 객체가 공통 값을 가지는 것들은 static 사용
class Article {
    static publisher = 'Jinsoo Son'
    static printPublisher() {
        console.log(Article.publisher);
    }
}
const article = new Article();   // = {}    객체안에는 static 포함이 안된다.
console.log(Article.publisher);             // Jinsoo Son
Article.printPublisher();                   // Jinsoo Son


// Inheritance
class Shape {
    constructor(width, height, color){
        this.width = width;
        this.height = height;
        this.color = color;
    }
    draw() {
        console.log(`drawing ${this.color} color of`)
    }
    getArea() {
        return this.width * this.height;
    }
}
class Rectangle extends Shape{};
const rectangle = new Rectangle(20,20,'blue');
class Triangle extends Shape{                       // 필요한 함수만 재정의 가능 /overwriting
    getArea() {
        return [this.width * this.height / 2, super.getArea()];   // [200, 400] super.func(부모 class func 호출)
    }
}
const triangle = new Triangle(20,20,'red');

// triangle instanceof Triangle  === true
// triangle instanceof Rectangle === false
// triangle instanceof Shape     === true
// triangle instanceof Object    === true
