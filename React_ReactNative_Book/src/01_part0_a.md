# PART 0 – JavaScript Needed for React {.part}

React is "just JavaScript". If these 14 ideas feel easy, React will feel easy too. You will see them in **every** React file you ever read.

> **Run the examples:** save each `js` example as `example.js` and run `node example.js`.

---

### 0.1 `let` and `const`

#### ELI5

Imagine a **lunch box with a name sticker**. With `const`, the sticker is glued on forever: this box is always "Asha's box". You can still change the food *inside*. With `let`, the sticker is a whiteboard label: you can erase it and write a new name.

#### Real explanation

- `const` creates a name that **cannot point to a new value**. It does *not* freeze objects or arrays. You can still change what is inside them.
- `let` creates a name you can **reassign**.
- Both are **block scoped**: they live only inside the `{ }` where you made them.
- `var` is the old way. It ignores blocks and causes bugs. **Do not use `var`.**
- Rule of thumb in React: use `const` by default. Use `let` only when you must reassign.

| Keyword | Reassign? | Block scoped? | Use today? |
|---------|-----------|---------------|------------|
| `const` | No        | Yes           | Yes (default) |
| `let`   | Yes       | Yes           | Yes (when needed) |
| `var`   | Yes       | No (function) | No |

#### Example code

```js
// const: the name cannot be reassigned
const name = "Asha";
// name = "Ravi";   // would throw: TypeError (assignment to constant)

// const with an array: we can change the INSIDE, not the label
const cart = ["apple"];
cart.push("banana");
console.log(cart);

// let: can be reassigned
let score = 0;
score = score + 10;
console.log(score);

// block scope: "inside" only exists in these braces
if (true) {
  let inside = "I live in the block";
  console.log(inside);
}
console.log(typeof inside); // "undefined" because inside is gone here
```

#### Output / what happens

```text
[ 'apple', 'banana' ]
10
I live in the block
undefined
```

The array changed even though it is `const`. The variable `inside` is not visible outside the `if` block.

#### Common mistakes

- **Reassigning a `const`.**

```javascript
// ❌ Wrong
const count = 0;
count = count + 1;   // TypeError

// ✅ Right
let count2 = 0;
count2 = count2 + 1;
```

- **Thinking `const` makes objects frozen.**

```javascript
// ❌ Wrong belief: "user can't change"
const user = { name: "Asha" };
user.name = "Ravi";  // this works!

// ✅ Right: if you need it frozen
const frozen = Object.freeze({ name: "Asha" });
```

- **Using `var` in loops.** `var` leaks out of the loop. Use `let`.

#### Mini practice task

Create `const PI = 3.14`. Create `let radius = 2`. Print the area (`PI * radius * radius`). Change `radius` to 5 and print again.

#### Key takeaway

> Use `const` by default, `let` when you must reassign, and never `var`.

---

### 0.2 Arrow functions

#### ELI5

A normal function is a **recipe card with a title**. An arrow function is a **sticky note** with the same recipe, written short. Same cooking, less writing.

#### Real explanation

An arrow function is a shorter way to write a function. It uses `=>`.

- One expression and no `{ }`: the result is **returned automatically** (implicit return).
- With `{ }`: you must write `return` yourself.
- One parameter: the `( )` are optional. Zero or many parameters: `( )` are needed.
- Returning an **object** directly? Wrap it in `( )`.
- Arrow functions do not have their own `this`. This is why React uses them for event handlers and callbacks.

Every React component and every callback you write will be an arrow function or a normal function.

#### Example code

```js
// 1. Normal function
function addOld(a, b) {
  return a + b;
}

// 2. Arrow function with a body
const add = (a, b) => {
  return a + b;
};

// 3. Arrow function with implicit return (no braces, no return)
const double = (n) => n * 2;

// 4. Returning an object: wrap it in parentheses
const makeUser = (name) => ({ name, active: true });

// 5. Used as a callback
const numbers = [1, 2, 3];
const doubled = numbers.map((n) => n * 2);

console.log(addOld(2, 3));
console.log(add(2, 3));
console.log(double(4));
console.log(makeUser("Asha"));
console.log(doubled);
```

#### Output / what happens

```text
5
5
8
{ name: 'Asha', active: true }
[ 2, 4, 6 ]
```

#### Common mistakes

- **Forgetting `return` when you use braces.**

```javascript
// ❌ Wrong: returns undefined
const triple = (n) => { n * 3 };

// ✅ Right
const triple2 = (n) => { return n * 3; };
const triple3 = (n) => n * 3;
```

- **Returning an object without parentheses.** JavaScript thinks `{ }` is a function body.

```javascript
// ❌ Wrong: returns undefined
const makeBad = (name) => { name };

// ✅ Right
const makeGood = (name) => ({ name });
```

#### Mini practice task

Write an arrow function `isEven(n)` that returns `true` when `n` is even. Test it with 4 and 7.

#### Key takeaway

> `(args) => result` is a short function. Braces need `return`; parentheses around `{}` return an object.

---

### 0.3 Template literals

#### ELI5

Think of a **fill-in-the-blank card**: "Hello, ____! You have ____ new toys." You write the card once and drop the words in the blanks. Backticks let you do that in code.

#### Real explanation

A template literal is a string written with **backticks** `` ` ``. Inside it you can:

- put any JavaScript expression with `${ ... }`
- write text over **many lines** without `\n`

Old way: `"Hello, " + name + "!"`. It gets messy fast. In React you use `${ }` for class names, URLs and messages all the time.

#### Example code

```js
const name = "Asha";
const items = 3;
const price = 49.5;

// Insert variables and expressions
const message = `Hello, ${name}! You have ${items} items.`;
const total = `Total: ${(items * price).toFixed(2)} rupees`;

// Multi-line text
const card = `Dear ${name},
Thank you for shopping.
Bye!`;

// A common React use: building a URL
const userId = 42;
const url = `https://api.example.com/users/${userId}`;

console.log(message);
console.log(total);
console.log(card);
console.log(url);
```

#### Output / what happens

```text
Hello, Asha! You have 3 items.
Total: 148.50 rupees
Dear Asha,
Thank you for shopping.
Bye!
https://api.example.com/users/42
```

#### Common mistakes

- **Using quotes instead of backticks.**

```javascript
// ❌ Wrong: prints the text ${name} literally
const bad = "Hello ${name}";

// ✅ Right
const good = `Hello ${name}`;
```

- **Putting a statement inside `${ }`.** Only expressions work (things that produce a value).

```javascript
// ❌ Wrong
const x1 = `Result: ${ if (true) { "yes" } }`;

// ✅ Right: use a ternary
const x2 = `Result: ${true ? "yes" : "no"}`;
```

#### Mini practice task

Make variables `product` and `qty`. Print: `You bought 2 pens.` using a template literal.

#### Key takeaway

> Use backticks and `${ }` to put values inside text.

---

### 0.4 Destructuring

#### ELI5

You get a **toy box** with a car, a ball and a doll inside. Instead of saying "take the car from the box, take the ball from the box...", you say **"unpack the box: give me car and ball"**. Destructuring unpacks.

#### Real explanation

Destructuring pulls values out of **objects** or **arrays** into separate variables, in one line.

- **Object destructuring** uses `{ }` and matches by **name**.
- **Array destructuring** uses `[ ]` and matches by **position**.
- You can set **default values** and **rename** variables.
- You can destructure **function parameters**. React does this for props: `function Card({ title, price })`.
- `useState` returns an array, so you will write `const [count, setCount] = useState(0)` (array destructuring).

#### Example code

```js
const user = { name: "Asha", age: 25, city: "Chennai" };

// Object destructuring (by name)
const { name, age } = user;

// Rename and default value
const { city: town, country = "India" } = user;

// Array destructuring (by position)
const colors = ["red", "green", "blue"];
const [first, second] = colors;

// Skip an item with an empty slot
const [, , third] = colors;

// Destructure function parameters (just like React props)
const greet = ({ name, age }) => `${name} is ${age}`;

console.log(name, age);
console.log(town, country);
console.log(first, second, third);
console.log(greet(user));
```

#### Output / what happens

```text
Asha 25
Chennai India
red green blue
Asha is 25
```

#### Common mistakes

- **Wrong brackets.** Objects use `{ }`, arrays use `[ ]`.

```javascript
// ❌ Wrong: array brackets on an object
const [name] = { name: "Asha" };   // TypeError

// ✅ Right
const { name: n } = { name: "Asha" };
```

- **Wrong name.** Object keys must match exactly.

```javascript
// ❌ Wrong: key is "name", not "username"
const { username } = { name: "Asha" };   // username is undefined

// ✅ Right
const { name: username2 } = { name: "Asha" };
```

#### Mini practice task

Given `const book = { title: "Atomic Habits", pages: 320 }`, destructure `title` and `pages` and print them.

#### Key takeaway

> `{ }` unpacks objects by name, `[ ]` unpacks arrays by position.

---

### 0.5 Spread and rest (`...`)

#### ELI5

**Spread** is like **pouring all the sweets from one jar into a new jar**, and maybe adding a few more. **Rest** is the opposite: **"put all the leftover sweets into one bag"**. Same three dots, two jobs.

#### Real explanation

The three dots `...` do two jobs, depending on where you put them:

| Where                        | Name   | What it does                              |
|------------------------------|--------|-------------------------------------------|
| In an array/object **literal** or function **call** | Spread | Expands items out |
| In a function **parameter** or **destructuring**     | Rest   | Collects leftovers into one |

Spread **copies** (a shallow copy). It is the main way to update state in React **without changing the original**: `setUser({ ...user, age: 26 })`. You will use this daily.

#### Example code

```js
// SPREAD with arrays
const a = [1, 2];
const b = [...a, 3, 4];          // new array: [1,2,3,4]

// SPREAD with objects (later keys win)
const user = { name: "Asha", age: 25 };
const older = { ...user, age: 26 };   // copy, then override age

// SPREAD in a function call
const nums = [5, 1, 9];
console.log(Math.max(...nums));

// REST in parameters: collects all arguments
const sum = (...values) => values.reduce((t, v) => t + v, 0);

// REST in destructuring: "everything else"
const { name, ...others } = { name: "Asha", age: 25, city: "Chennai" };
const [head, ...tail] = [10, 20, 30];

console.log(b);
console.log(older, user);
console.log(sum(1, 2, 3));
console.log(others);
console.log(head, tail);
```

#### Output / what happens

```text
9
[ 1, 2, 3, 4 ]
{ name: 'Asha', age: 26 } { name: 'Asha', age: 25 }
6
{ age: 25, city: 'Chennai' }
10 [ 20, 30 ]
```

The original `user` did **not** change. That is the whole point.

#### Common mistakes

- **Thinking spread is a deep copy.** It copies only the first level.

```javascript
// ❌ Wrong: inner object is shared
const p = { name: "A", address: { city: "X" } };
const q = { ...p };
q.address.city = "Y";   // p.address.city is also "Y" now!

// ✅ Right: copy the inner object too
const q2 = { ...p, address: { ...p.address, city: "Y" } };
```

- **Changing the original instead of copying.**

```javascript
// ❌ Wrong: mutates the original array
const list = [1, 2];
list.push(3);

// ✅ Right: make a new array
const list2 = [...list, 4];
```

#### Mini practice task

Start with `const todo = { text: "Study", done: false }`. Create a new object where `done` is `true` without changing `todo`.

#### Key takeaway

> `...` spreads things out (to copy) or gathers leftovers (rest). Copy, don't mutate.

---

### 0.6 Array method: `map`

#### ELI5

A **chocolate factory belt**. Every plain biscuit goes in and comes out wrapped in chocolate. You get the **same number of items**, each one changed.

#### Real explanation

`array.map(fn)` runs `fn` on **every item** and returns a **new array** with the results. The new array always has the **same length**. The original is not changed.

**In React, `map` turns a list of data into a list of UI elements.** This is the most-used array method in React.

#### Example code

```js
const prices = [100, 250, 400];

// Make a new array with 10% tax added
const withTax = prices.map((p) => p * 1.1);

// map gives you the item and its index
const labels = prices.map((p, i) => `Item ${i + 1}: ${p}`);

// Turn data into "UI-like" strings (React will return JSX here later)
const names = ["Asha", "Ravi"];
const html = names.map((n) => `<li>${n}</li>`).join("");

console.log(withTax);
console.log(labels);
console.log(html);
console.log(prices); // original is unchanged
```

#### Output / what happens

```text
[ 110.00000000000001, 275, 440.00000000000006 ]
[ 'Item 1: 100', 'Item 2: 250', 'Item 3: 400' ]
<li>Asha</li><li>Ravi</li>
[ 100, 250, 400 ]
```

(The long decimals are normal floating-point behaviour. Use `.toFixed(2)` when you show money.)

#### Common mistakes

- **Forgetting to return.**

```javascript
// ❌ Wrong: braces but no return -> [undefined, undefined]
const r1 = [1, 2].map((n) => { n * 2 });

// ✅ Right
const r2 = [1, 2].map((n) => n * 2);
```

- **Using `map` just for side effects.** If you don't use the new array, use `forEach`.

```javascript
// ❌ Wrong
[1, 2].map((n) => console.log(n));

// ✅ Right
[1, 2].forEach((n) => console.log(n));
```

#### Mini practice task

Given `["a", "b", "c"]`, use `map` to return `["A", "B", "C"]` (hint: `.toUpperCase()`).

#### Key takeaway

> `map` changes every item and gives back a new array of the same length.

---

### 0.7 Array method: `filter`

#### ELI5

A **sieve in the kitchen**. You pour in rice and stones. Only the rice passes through. Whatever **passes the test** is kept.

#### Real explanation

`array.filter(fn)` calls `fn` on each item. If `fn` returns something **truthy**, the item is kept. You get a **new array** that can be **shorter** (or even empty). The original is unchanged.

In React, `filter` is how you **delete an item from state** (keep everything except one) and how you build **search boxes**.

#### Example code

```js
const todos = [
  { id: 1, text: "Study", done: true },
  { id: 2, text: "Cook", done: false },
  { id: 3, text: "Walk", done: false },
];

// Keep only pending todos
const pending = todos.filter((t) => !t.done);

// "Delete" todo with id 2: keep every todo that is NOT id 2
const afterDelete = todos.filter((t) => t.id !== 2);

// Search: items whose text includes "al"
const found = todos.filter((t) => t.text.toLowerCase().includes("al"));

console.log(pending.map((t) => t.text));
console.log(afterDelete.map((t) => t.id));
console.log(found.map((t) => t.text));
```

#### Output / what happens

```text
[ 'Cook', 'Walk' ]
[ 1, 3 ]
[ 'Walk' ]
```

#### Common mistakes

- **Expecting a single item.** `filter` always gives an **array**.

```javascript
// ❌ Wrong: result is an array, not an object
const todo = todos.filter((t) => t.id === 2);
console.log(todo.text);   // undefined

// ✅ Right: use find for one item
const todo2 = todos.find((t) => t.id === 2);
```

- **Mutating with `splice` in React state.** Use `filter` to get a new array.

```javascript
// ❌ Wrong
todos.splice(1, 1);

// ✅ Right
const next = todos.filter((t) => t.id !== 2);
```

#### Mini practice task

From `[5, 12, 8, 20]`, keep only numbers greater than 10.

#### Key takeaway

> `filter` keeps the items that pass your test and returns a new array.

---
