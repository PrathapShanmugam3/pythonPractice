// Run with: npx tsx types-basics.ts
export {};

// 1. Basic types
const courseName: string = 'Angular';
let lessons: number = 38;
const isFun: boolean = true;
const topics: string[] = ['Components', 'Services', 'Routing'];
const level: [string, number] = ['Beginner', 10]; // tuple: fixed length and types

// 2. Union of literal values: only these three strings are allowed
type Level = 'Beginner' | 'Intermediate' | 'Advanced';

function describe(level: Level, count: number = 1): string {
  return `${count} topic(s) at ${level} level`;
}

// 3. Generic function: works for any type T
function first<T>(items: T[]): T | undefined {
  return items[0];
}

console.log(`${courseName} has ${lessons} lessons. Fun? ${isFun}`);
console.log('Topics:', topics.join(', '));
console.log('Tuple:', level[0], level[1]);
console.log(describe('Beginner', 10));
console.log('First topic:', first(topics));
console.log('First of empty list:', first<number>([]));

// describe('Expert'); // <- compile error: 'Expert' is not a valid Level
