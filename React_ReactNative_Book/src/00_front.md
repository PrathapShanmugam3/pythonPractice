<div class="title-page">

<div class="tp-small">A Zero-to-Master Learning Book</div>

# React & React Native

<div class="tp-sub">From "What is a component?" to shipping apps on the Play Store and App Store</div>

<div class="tp-meta">Explained like you are 5 &nbsp;•&nbsp; Built up to professional depth<br>
React 19 &nbsp;•&nbsp; Expo Router &nbsp;•&nbsp; New Architecture &nbsp;•&nbsp; TypeScript</div>

<div class="tp-note">Edition 1 &mdash; released one Part at a time</div>

</div>

<div class="pb"></div>

## Table of Contents {.unnumbered .toc-title}

**Front matter**

- How to Use This Book

**Web: React**

- **Part 0** – JavaScript Needed for React *(included in this edition)*
- **Part 1** – React Basics
- **Part 2** – State and Events
- **Part 3** – Hooks Deep Dive
- **Part 4** – How React Works Internally
- **Part 5** – Routing
- **Part 6** – Data Fetching and APIs
- **Part 7** – State Management
- **Part 8** – Forms and Validation
- **Part 9** – Performance
- **Part 10** – Advanced Patterns
- **Part 11** – TypeScript with React
- **Part 12** – Testing
- **Part 13** – Next.js Essentials

**Mobile: React Native**

- **Part 14** – React Native Basics
- **Part 15** – React Native Navigation
- **Part 16** – React Native Data and Storage
- **Part 17** – Device Features
- **Part 18** – UI and Animations
- **Part 19** – RN Performance and Native Code
- **Part 20** – Build and Publish

**Capstone**

- **Part 21** – Master Projects (Task Manager, Expense Tracker, Monorepo)

**Appendix**

- 50 Interview Questions, Hooks Cheat Sheet, Recommended Folder Structure, Glossary

### Part 0 in detail {.unnumbered}

| #    | Topic                                   |
|------|-----------------------------------------|
| 0.1  | `let` and `const`                       |
| 0.2  | Arrow functions                         |
| 0.3  | Template literals                       |
| 0.4  | Destructuring                           |
| 0.5  | Spread and rest                         |
| 0.6  | Array method: `map`                     |
| 0.7  | Array method: `filter`                  |
| 0.8  | Array method: `reduce`                  |
| 0.9  | Array method: `find` (and friends)      |
| 0.10 | Modules: `import` and `export`          |
| 0.11 | Promises                                |
| 0.12 | `async` / `await`                       |
| 0.13 | Optional chaining `?.`                  |
| 0.14 | Nullish coalescing `??`                 |
|      | Quiz and Mini Project                   |

<div class="pb"></div>

## How to Use This Book {.unnumbered}

### Who this book is for

You know a little JavaScript. You want to build real apps with React (web) and React Native (mobile). This book treats **every topic as new**, so nothing is skipped.

### How every topic is built

Each topic follows the same 8 steps. Once you see the pattern, you can read fast.

| Step | Name                | What it gives you                                    |
|------|---------------------|------------------------------------------------------|
| 1    | **Title**           | A number, like `3.2 useEffect`                       |
| 2    | **ELI5**            | A real-life picture (kitchen, school, shop, toys)    |
| 3    | **Real explanation**| What it is, why it exists, how it works inside       |
| 4    | **Example code**    | A complete, commented example you can run            |
| 5    | **Output**          | What you see when you run it                         |
| 6    | **Common mistakes** | 2–3 traps with wrong vs right code                   |
| 7    | **Mini practice**   | One small exercise to try yourself                   |
| 8    | **Key takeaway**    | One line to remember                                 |

At the end of every Part you get a **5-question quiz** (with answers) and a **mini project** that mixes the whole Part.

### The best way to learn

1. **Read** the ELI5 first. If it clicks, the rest is easy.
2. **Type** the example yourself. Do not copy-paste. Typing builds memory.
3. **Break** it on purpose. Change a line and predict what happens.
4. **Do** the mini practice task before you move on.
5. **Take** the quiz without looking at the answers.
6. **Build** the mini project. This is where learning sticks.

A good pace is **one Part per week**, about 1 hour a day.

### What you need installed

| Tool            | Why                                   | Check with        |
|-----------------|---------------------------------------|-------------------|
| Node.js 20+     | Runs JavaScript outside the browser   | `node --version`  |
| A code editor   | VS Code is a good choice              | –                 |
| A browser       | Chrome or Firefox, with DevTools      | –                 |
| Git             | Saves your work                       | `git --version`   |

Later Parts add more tools (Vite, Expo, Android Studio, Xcode). Each Part tells you exactly what to install.

### Code conventions

- Modern JavaScript only. React 19, function components, hooks. No class components (one short "legacy" note later).
- React Native examples work with **Expo**.
- `// ❌` marks wrong code. `// ✅` marks right code.
- Part 0 examples run with Node. Save as `example.js` and run `node example.js`.
- ASCII diagrams show flows. Tables compare ideas.

<div class="pb"></div>
