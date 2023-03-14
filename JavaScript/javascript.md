# **JavaScript & Node**



**command line code**
```javascript

$ node -v
$ node file_name.js
```


**comments**
```javascript
// console.log("Single line comment")

/*
Multi line,
comment
*/
```


**data type & variables**
```javascript
const pi = 3.14
let helloMessage = "Hello, world!"
let price = 9.99400
let quantity = 10
let isRaining = true
let isSunny = false

let name
name = "Sakib"
console.log(name)
```


**standard built in object (library)**
```javascript
let pi = Math.PI
console.log(pi)

let currentDate = new Date()
console.log(currentDate.toLocaleString())
```

**template literals**
```javascript
let name = "Alice";
let age = 30;
let greeting = `Hello, my name is ${name} and I am ${age} years old.`;
console.log(greeting);

```


**built in object**
```javascript

// Object
let number = {"a": 5, "b": 10, "c": 35}
console.log(number.a)

// Arrays
let numbers = [1, 2, 3, 4, 5];
console.log(numbers);

//  Map
let myMap = new Map();
myMap.set(1, "one");
console.log(myMap.get(1));


// Set
let mySet = new Set([1, 2, 3, 4, 4, 5]);
console.log(mySet);

```


**function**
```javascript
// Function
function addNumbers(a, b) {
  return a + b;
}
let sum = addNumbers(2, 3);
console.log(sum);

// Array function
let addNumbers = (a, b) => {
  return a + b;
}
```

**conditional and loop statement**
```javascript
let age = 25;

if (age < 18) {
  console.log("You are not old enough to vote.");
} else if (age >= 18 && age < 21) {
  console.log("You can vote but cannot drink.");
} else {
  console.log("You can vote and drink.");
}

// For loop
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// While loop
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}

// Break statement
for (let i = 0; i < 5; i++) {
  if (i === 3) {
    break;
  }
  console.log(i);
}

// Continue statement
for (let i = 0; i < 5; i++) {
  if (i === 3) {
    continue;
  }
  console.log(i);
}


// Try Catch Finally
try {
  const x = y + 1; // throws an error because y is not defined
} catch (error) {
  console.log("An error occurred:", error);
} finally {
  console.log("This code will always execute");
}
```


**class**
```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHello() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

const person1 = new Person("Alice", 30);
person1.sayHello(); // logs "Hello, my name is Alice and I am 30 years old."

```

