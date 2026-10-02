// Run with: npx tsx classes-interfaces.ts
export {};

// An interface describes the SHAPE of an object
interface Course {
  id: number;
  title: string;
  price?: number; // optional
}

// A class with a constructor shortcut (parameter properties)
class Student {
  private enrolled: Course[] = [];

  constructor(public name: string) {}

  enroll(course: Course): void {
    this.enrolled.push(course);
  }

  get summary(): string {
    const titles = this.enrolled.map((c) => c.title).join(', ');
    return `${this.name} is learning: ${titles || 'nothing yet'}`;
  }
}

const angular: Course = { id: 1, title: 'Angular', price: 999 };
const ts: Course = { id: 2, title: 'TypeScript' }; // price is optional

const priya = new Student('Priya');
console.log(priya.summary);
priya.enroll(angular);
priya.enroll(ts);
console.log(priya.summary);

// Template string + optional chaining + nullish coalescing
console.log(`TypeScript price: ${ts.price ?? 'free'}`);
