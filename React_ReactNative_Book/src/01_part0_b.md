### 0.8 Array method: `reduce`

#### ELI5

You have a **piggy bank** and a pile of coins. You pick up one coin at a time and drop it in. At the end, the whole pile has become **one number**: your total. `reduce` squashes many things into one.

#### Real explanation

`array.reduce(fn, start)` walks through the array. `fn(accumulator, item)` gets the running result (the **accumulator**) and the current item. Whatever `fn` returns becomes the accumulator for the next round. The final accumulator is the answer.

The answer can be a number, an object, an array, anything. Always give a **start value** (second argument).

```text
 start = 0
   [10, 20, 30]
    |
    +-- acc=0  + 10  -> 10
    +-- acc=10 + 20  -> 30
    +-- acc=30 + 30  -> 60   <-- final answer
```

In React, `reduce` is used for totals (cart price), counting, grouping, and inside `useReducer` (Part 3).

#### Example code

```js
const cart = [
  { name: "Pen", price: 10, qty: 3 },
  { name: "Book", price: 120, qty: 1 },
  { name: "Bag", price: 500, qty: 2 },
];

// 1. Total price: many items -> one number
const total = cart.reduce((sum, item) => sum + item.price * item.qty, 0);

// 2. Count how many times each word appears: many items -> one object
const words = ["a", "b", "a", "c", "a"];
const counts = words.reduce((acc, w) => {
  acc[w] = (acc[w] || 0) + 1;
  return acc; // always return the accumulator
}, {});

console.log(total);
console.log(counts);
```

#### Output / what happens

```text
1150
{ a: 3, b: 1, c: 1 }
```

#### Common mistakes

- **No start value.** With an empty array, `reduce` crashes.

```javascript
// ❌ Wrong: TypeError on an empty array
[].reduce((a, b) => a + b);

// ✅ Right
[].reduce((a, b) => a + b, 0);   // 0
```

- **Forgetting to return the accumulator.**

```javascript
// ❌ Wrong: acc becomes undefined on the next round
words.reduce((acc, w) => { acc[w] = 1; }, {});

// ✅ Right
words.reduce((acc, w) => { acc[w] = 1; return acc; }, {});
```

#### Mini practice task

Use `reduce` to find the **largest** number in `[3, 9, 4]`. (Hint: start with `-Infinity`, or with the first item.)

#### Key takeaway

> `reduce` folds a whole array into one value. Always give a start value and always return the accumulator.

---

### 0.9 Array method: `find` (and friends)

#### ELI5

You are looking for **your red socks** in a drawer. You stop the moment you see them. You don't check the rest. `find` stops at the **first match**.

#### Real explanation

| Method       | Returns                                  | Stops early? |
|--------------|------------------------------------------|--------------|
| `find(fn)`      | the **first item** that passes, or `undefined` | Yes |
| `findIndex(fn)` | the **position** of the first match, or `-1`   | Yes |
| `some(fn)`      | `true` if **at least one** passes              | Yes |
| `every(fn)`     | `true` if **all** pass                         | Yes |
| `includes(x)`   | `true` if the value is in the array            | Yes |

In React you use `find` to pick one item by id (for a detail page) and `some`/`every` for checks like "is any field empty?".

#### Example code

```js
const users = [
  { id: 1, name: "Asha", admin: false },
  { id: 2, name: "Ravi", admin: true },
  { id: 3, name: "Meena", admin: false },
];

const ravi = users.find((u) => u.id === 2);          // the object
const missing = users.find((u) => u.id === 99);      // undefined
const index = users.findIndex((u) => u.name === "Meena");
const hasAdmin = users.some((u) => u.admin);         // true
const allAdmin = users.every((u) => u.admin);        // false
const hasTwo = [1, 2, 3].includes(2);                // true

console.log(ravi);
console.log(missing);
console.log(index, hasAdmin, allAdmin, hasTwo);
```

#### Output / what happens

```text
{ id: 2, name: 'Ravi', admin: true }
undefined
2 true false true
```

#### Common mistakes

- **Using the result without checking for `undefined`.**

```javascript
// ❌ Wrong: crashes if user 99 doesn't exist
console.log(users.find((u) => u.id === 99).name);

// ✅ Right
const u = users.find((x) => x.id === 99);
console.log(u ? u.name : "Not found");
// or: users.find((x) => x.id === 99)?.name   (see 0.13)
```

- **Using `filter(...)[0]` when you want one item.** `find` is simpler and faster.

#### Mini practice task

From `["red", "green", "blue"]`, check if it includes `"green"`, and find the first color whose length is greater than 3.

#### Key takeaway

> `find` gets the first match, `some`/`every` answer yes/no questions. Always handle "not found".

---

### 0.10 Modules: `import` and `export`

#### ELI5

A big school has **many classrooms**. Each classroom (file) keeps its own stuff. If one class wants to use another class's globe, the owner must **offer it** (`export`) and the other class must **ask for it** (`import`).

#### Real explanation

A **module** is just a file. Variables inside are private unless you `export` them. Other files `import` what they need.

| Type          | Export                          | Import                         | How many per file |
|---------------|---------------------------------|--------------------------------|-------------------|
| **Named**     | `export const add = ...`        | `import { add } from "./math.js"` | many |
| **Default**   | `export default Button`         | `import Button from "./Button.js"` | one |

- Named imports must use the **same name** (you may rename with `as`).
- Default imports can use **any name**.
- A path starting with `./` means "this folder". A bare name like `"react"` means "an installed package".
- **React: one component per file, usually a default export.** Helpers and hooks use named exports.

```text
  math.mjs  ---- export add, PI ---->  main.mjs
                                         import { add, PI } from "./math.mjs"
```

#### Example code

Save these two files in the same folder. Use the `.mjs` extension so Node treats them as modules.

```js
// ===== File 1: math.mjs =====
export const PI = 3.14;                     // named export
export const add = (a, b) => a + b;         // named export
export default function greet(name) {       // default export (only one)
  return `Hello, ${name}!`;
}
```

```js
// ===== File 2: main.mjs =====
// Run with: node main.mjs
import greet, { add, PI as pie } from "./math.mjs";
// "greet" is the default import (any name works)
// { add, PI as pie } are named imports (PI renamed to pie)

console.log(greet("Asha"));
console.log(add(2, 3));
console.log(pie);
```

#### Output / what happens

```text
Hello, Asha!
5
3.14
```

#### Common mistakes

- **Curly braces on a default import (and none on a named one).**

```javascript
// ❌ Wrong
import { greet } from "./math.mjs";   // greet is a default export
import add from "./math.mjs";         // add is a named export

// ✅ Right
import greet, { add } from "./math.mjs";
```

- **Forgetting `./` for your own files.**

```javascript
// ❌ Wrong: looks for an npm package called "math.mjs"
import { add } from "math.mjs";

// ✅ Right
import { add } from "./math.mjs";
```

#### Mini practice task

Create `shape.mjs` that exports a function `area(w, h)`. Import and use it in `main.mjs`.

#### Key takeaway

> `export` offers, `import` asks. Named = with `{ }`, default = without.

---

### 0.11 Promises

#### ELI5

You order a **pizza** and get a **buzzer**. The buzzer is a promise: "pizza is coming". While you wait you can chat. Soon it either **rings** (pizza ready = success) or **blinks red** (oven broke = failure).

#### Real explanation

Some work takes time (loading data from a server, reading a file). JavaScript does not freeze while waiting. It gives you a **Promise**: an object that will have a result **later**.

A promise is always in one of 3 states:

```text
          +--> fulfilled (success, has a value) --> .then(value => ...)
pending --+
          +--> rejected  (failure, has an error) --> .catch(error => ...)
```

- `.then(fn)` runs when it succeeds.
- `.catch(fn)` runs when it fails.
- `.finally(fn)` runs either way.
- You can chain `.then` calls. Each one gets the previous one's return value.
- `fetch()` in React returns a promise. So does almost every API call.

#### Example code

```js
// A fake server call: waits 500 ms, then succeeds or fails
function fakeFetchUser(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id > 0) resolve({ id, name: "Asha" }); // success
      else reject(new Error("Invalid id"));      // failure
    }, 500);
  });
}

console.log("1. Asking for user...");

fakeFetchUser(1)
  .then((user) => {
    console.log("3. Got user:", user.name);
    return user.id * 100;          // passed to the next .then
  })
  .then((n) => console.log("4. Next step got:", n))
  .catch((err) => console.log("Error:", err.message))
  .finally(() => console.log("5. Done (success or fail)"));

console.log("2. This line runs while we wait!");
```

#### Output / what happens

```text
1. Asking for user...
2. This line runs while we wait!
3. Got user: Asha
4. Next step got: 100
5. Done (success or fail)
```

Line 2 prints **before** line 3. JavaScript did not wait. After about half a second the promise finished and the `.then` code ran. Change `fakeFetchUser(1)` to `fakeFetchUser(-1)` to see the `.catch` path.

#### Common mistakes

- **Treating a promise like the final value.**

```javascript
// ❌ Wrong: user is a Promise, not an object
const user = fakeFetchUser(1);
console.log(user.name);   // undefined

// ✅ Right
fakeFetchUser(1).then((u) => console.log(u.name));
```

- **Forgetting `.catch`.** An unhandled rejection can crash Node or fail silently in the browser.

```javascript
// ❌ Wrong
fakeFetchUser(-1).then((u) => console.log(u));

// ✅ Right
fakeFetchUser(-1).then((u) => console.log(u)).catch((e) => console.log(e.message));
```

- **Not returning inside `.then`.** The next `.then` gets `undefined`.

#### Mini practice task

Write `wait(ms)` that returns a promise resolving after `ms` milliseconds. Use `.then` to print `"done"` after 1 second.

#### Key takeaway

> A promise is a "result coming later". Use `.then` for success and `.catch` for failure.

---

### 0.12 `async` / `await`

#### ELI5

Same pizza buzzer, but now you write the story **like a normal list**: "order pizza, wait for the buzzer, eat pizza". The word `await` means "pause *me* here until the buzzer rings". Other people in the shop keep working.

#### Real explanation

`async`/`await` is a cleaner way to write promise code. It reads top-to-bottom like normal code.

- Put `async` before a function. That function now **always returns a promise**.
- Inside it, `await promise` pauses **that function** until the promise settles, then gives you the value.
- Use `try / catch / finally` for errors instead of `.catch`.
- `await` only works inside an `async` function (or at the top level of a module).
- To run things **at the same time**, use `Promise.all([...])`.

In React you write `async` functions for every API call (but **not** as the component function itself, which you will see in Part 3).

#### Example code

```js
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function getUser(id) {
  await wait(300);
  if (id <= 0) throw new Error("Invalid id");
  return { id, name: "User" + id };
}

async function main() {
  try {
    // Sequential: one after another (about 600 ms)
    const a = await getUser(1);
    const b = await getUser(2);
    console.log("Sequential:", a.name, b.name);

    // Parallel: both at the same time (about 300 ms)
    const [c, d] = await Promise.all([getUser(3), getUser(4)]);
    console.log("Parallel:", c.name, d.name);

    await getUser(-1); // this one fails
    console.log("never printed");
  } catch (err) {
    console.log("Caught:", err.message);
  } finally {
    console.log("Finished");
  }
}

main();
```

#### Output / what happens

```text
Sequential: User1 User2
Parallel: User3 User4
Caught: Invalid id
Finished
```

The sequential lines take about 0.6 seconds. The parallel pair takes about 0.3 seconds, because both waited together.

#### Common mistakes

- **Forgetting `await`.**

```javascript
// ❌ Wrong: user is a Promise
const user = getUser(1);
console.log(user.name);   // undefined

// ✅ Right
const user2 = await getUser(1);
```

- **Using `await` in a normal function.**

```javascript
// ❌ Wrong: SyntaxError
function load() { const u = await getUser(1); }

// ✅ Right
async function load2() { const u = await getUser(1); }
```

- **Awaiting one by one when they don't depend on each other.** Use `Promise.all`.

#### Mini practice task

Write an `async` function that waits 1 second, then returns `"Hello"`. Call it and print the result.

#### Key takeaway

> `await` pauses an `async` function until a promise is done. Use `try/catch` for errors and `Promise.all` for parallel work.

---

### 0.13 Optional chaining `?.`

#### ELI5

You want to open **a door, then a cupboard behind it, then take the cookie**. If the door isn't there, you don't want to crash into a wall. `?.` says: **"if this thing exists, keep going; if not, stop and say 'nothing'."**

#### Real explanation

Reading a property of `undefined` or `null` throws an error: `Cannot read properties of undefined`. This is the **most common error in React apps**, because data often arrives late (after an API call).

`?.` stops safely and returns `undefined` instead of crashing.

| Syntax            | Meaning                                  |
|-------------------|------------------------------------------|
| `obj?.prop`       | read `prop` only if `obj` is not null/undefined |
| `obj?.[key]`      | same, with brackets                      |
| `fn?.()`          | call `fn` only if it exists              |
| `arr?.[0]`        | read first item only if `arr` exists     |

#### Example code

```js
const user = {
  name: "Asha",
  address: { city: "Chennai" },
  greet() { return "Hi!"; },
};
const empty = null;

console.log(user.address?.city);       // "Chennai"
console.log(user.job?.title);          // undefined (no job, no crash)
console.log(empty?.name);              // undefined (no crash)
console.log(user.greet?.());           // "Hi!"
console.log(user.dance?.());           // undefined (no function, no crash)

const list = undefined;
console.log(list?.[0]);                // undefined

// Without ?. this line would crash:
// console.log(user.job.title);
```

#### Output / what happens

```text
Chennai
undefined
undefined
Hi!
undefined
undefined
```

#### Common mistakes

- **Using `?.` everywhere "just in case".** It can hide real bugs. Use it only where data may truly be missing.

```javascript
// ❌ Wrong: user always exists here, so ?. hides mistakes
const n = user?.name;

// ✅ Right: use it for data that may be missing
const t = user.job?.title;
```

- **Using `?.` on the left side of an assignment.**

```javascript
// ❌ Wrong: SyntaxError
user?.name = "Ravi";

// ✅ Right
if (user) user.name = "Ravi";
```

#### Mini practice task

Make `const data = { profile: null }`. Safely print `data.profile?.email`.

#### Key takeaway

> `?.` means "only continue if it exists". It prevents "Cannot read properties of undefined".

---

### 0.14 Nullish coalescing `??`

#### ELI5

"If you don't have a pencil, **use this spare one**." But the important part: if you have a pencil that is **0 cm long**, it is still *your pencil*. It is only "missing" when you truly have nothing (`null` or `undefined`).

#### Real explanation

`a ?? b` returns `b` **only if `a` is `null` or `undefined`**. Otherwise it returns `a`.

It differs from `||`, which replaces **every falsy value**: `0`, `""`, `false`, `NaN`. That is often a bug.

| `a` is...   | `a \|\| "x"` | `a ?? "x"` |
|-------------|-------------|-----------|
| `undefined` | `"x"`       | `"x"`     |
| `null`      | `"x"`       | `"x"`     |
| `0`         | `"x"` (!)   | `0`       |
| `""`        | `"x"` (!)   | `""`      |
| `false`     | `"x"` (!)   | `false`   |
| `"hi"`      | `"hi"`      | `"hi"`    |

It pairs well with `?.`: `user.nickname ?? "Guest"`. There is also `??=` which assigns only when the value is missing.

#### Example code

```js
const settings = { volume: 0, nickname: "", theme: undefined };

// || treats 0 and "" as missing (usually wrong)
console.log(settings.volume || 50);       // 50  (bug: user chose 0!)
console.log(settings.nickname || "Guest");// "Guest"

// ?? only replaces null / undefined (correct)
console.log(settings.volume ?? 50);       // 0
console.log(settings.nickname ?? "Guest");// ""
console.log(settings.theme ?? "light");   // "light"

// Combine with ?.
const user = { profile: null };
console.log(user.profile?.city ?? "Unknown city");

// ??= assigns only if missing
let color;
color ??= "blue";
console.log(color);
```

#### Output / what happens

```text
50
Guest
0
(empty line)
light
Unknown city
blue
```

The 4th line prints an empty string, so you see a blank line.

#### Common mistakes

- **Using `||` for defaults when `0` or `""` are valid.**

```javascript
// ❌ Wrong: a score of 0 becomes 100
const score = 0;
const shown = score || 100;

// ✅ Right
const shown2 = score ?? 100;
```

- **Mixing `??` with `||` or `&&` without parentheses.** It is a SyntaxError.

```javascript
// ❌ Wrong
const v = a || b ?? c;

// ✅ Right
const v2 = (a || b) ?? c;
```

#### Mini practice task

Write `const age = 0`. Print the age using `??` so that `0` stays `0`, and print `"unknown"` for `undefined`.

#### Key takeaway

> `??` gives a default only for `null`/`undefined`. Use it instead of `||` when `0`, `""` or `false` are real values.

---

## Part 0 Quiz {.unnumbered}

Try all 5 before reading the answers.

1. Which line throws an error?
   `const a = [1]; a.push(2);` or `const b = 1; b = 2;`
2. What does `[1, 2, 3].map((n) => { n * 2 })` return?
3. What is the result of `0 ?? 10` and of `0 || 10`?
4. How do you wait for two independent API calls **at the same time**?
5. A file has `export default function Card() {}`. Write the correct import line.

### Quiz answers {.unnumbered}

1. `b = 2` throws, because `b` is a `const`. `a.push(2)` is fine: `const` protects the label, not the contents.
2. `[undefined, undefined, undefined]`. The braces need a `return`.
3. `0 ?? 10` is `0`. `0 || 10` is `10`.
4. `const [x, y] = await Promise.all([callA(), callB()]);`
5. `import Card from "./Card.js";` (no curly braces for a default export).

---

## Part 0 Mini Project: Shopping Cart Report {.unnumbered}

**Goal:** One small program that uses almost every topic in this Part.

You have a product list from a "server". Build a report: load data (promise + `async/await`), filter in-stock items, add tax (`map`), compute totals (`reduce`), find the cheapest (`find`/`reduce`), and print safe text (`?.`, `??`, template literals, destructuring, spread).

Save as `cart.mjs` and run `node cart.mjs`.

```js
// cart.mjs  –  Part 0 mini project
// ---------- 1. Fake server (promises, async/await) ----------
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function fetchProducts() {
  await wait(300); // pretend we call an API
  return [
    { id: 1, name: "Pen", price: 10, qty: 10, inStock: true, discount: 0 },
    { id: 2, name: "Notebook", price: 60, qty: 2, inStock: true },
    { id: 3, name: "Bag", price: 500, qty: 1, inStock: false },
    { id: 4, name: "Bottle", price: 150, qty: 3, inStock: true, discount: 10 },
  ];
}

// ---------- 2. Helpers (arrow functions) ----------
const TAX_RATE = 0.18; // const: never changes
const money = (n) => `₹${n.toFixed(2)}`; // template literal

// Price of one line after discount (?? gives 0 when discount is missing)
const lineTotal = ({ price, qty, discount }) =>
  price * qty * (1 - (discount ?? 0) / 100);

// ---------- 3. Main program ----------
async function main() {
  const products = await fetchProducts();

  // filter: only items in stock
  const available = products.filter((p) => p.inStock);

  // map: add a "total" to each item (spread copies the object)
  const lines = available.map((p) => ({ ...p, total: lineTotal(p) }));

  // reduce: add all totals
  const subtotal = lines.reduce((sum, l) => sum + l.total, 0);
  const tax = subtotal * TAX_RATE;
  const grandTotal = subtotal + tax;

  // reduce: find the cheapest line
  const cheapest = lines.reduce((min, l) => (l.total < min.total ? l : min));

  // find + ?. : look up an id that may not exist
  const item9 = products.find((p) => p.id === 9);

  // destructuring in the loop
  console.log("=== Cart Report ===");
  for (const { name, qty, total } of lines) {
    console.log(`${name} x${qty} = ${money(total)}`);
  }
  console.log("-------------------");
  console.log(`Subtotal: ${money(subtotal)}`);
  console.log(`Tax (18%): ${money(tax)}`);
  console.log(`Grand total: ${money(grandTotal)}`);
  console.log(`Cheapest line: ${cheapest.name}`);
  console.log(`Item 9: ${item9?.name ?? "not found"}`);
}

main().catch((err) => console.log("Failed:", err.message));
```

**Expected output**

```text
=== Cart Report ===
Pen x10 = ₹100.00
Notebook x2 = ₹120.00
Bottle x3 = ₹405.00
-------------------
Subtotal: ₹625.00
Tax (18%): ₹112.50
Grand total: ₹737.50
Cheapest line: Pen
Item 9: not found
```

**Stretch goals**

1. Move the helpers into `helpers.mjs` and `import` them.
2. Add a `searchTerm` and filter lines by name.
3. Use `Promise.all` to fetch products and a "coupons" list together.

**Topics used:** 0.1 `const`/`let` • 0.2 arrows • 0.3 templates • 0.4 destructuring • 0.5 spread • 0.6 `map` • 0.7 `filter` • 0.8 `reduce` • 0.9 `find` • 0.11–0.12 promises and `async/await` • 0.13 `?.` • 0.14 `??`

---

*End of Part 0. Say **"next"** to continue to Part 1 – React Basics.*
