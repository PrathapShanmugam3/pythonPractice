"""Angular - Beginner topics (01-10)."""

B = "Beginner"

TOPICS = [
    # ------------------------------------------------------------------ 01
    {
        "slug": "Introduction_to_Angular", "title": "Introduction to Angular", "level": B,
        "summary": "What Angular is, why companies use it, SPAs, and the big-picture architecture.",
        "definition": [
            "**Angular** is a free, open-source framework from Google for building web applications using "
            "**TypeScript**, HTML and CSS. Instead of writing one huge page, you build small reusable pieces called "
            "**components** and snap them together like LEGO blocks.",
            "Angular apps are usually **Single Page Applications (SPA)**: the browser loads the page once, and after "
            "that Angular only swaps the parts of the screen that change. No full page reload, so the app feels fast "
            "like a mobile app.",
            "Angular is a complete platform: it ships with routing, forms, HTTP, testing tools and a command-line "
            "tool (the Angular CLI), so you do not have to pick and glue together many separate libraries.",
        ],
        "diagram": {"type": "layers", "caption": "Big picture: every Angular app is a tree of components running in the browser",
                    "layers": [("Browser", "Chrome / Edge / Firefox"),
                               ("Angular Framework", "change detection, routing, forms, HTTP, DI"),
                               ("Your App", "components + services + routes"),
                               ("Component = Class (logic) + Template (HTML) + Styles (CSS)", "")]},
        "syntax": """@Component({
  selector: 'app-name',        // the HTML tag you will use
  template: `<h1>...</h1>`,    // what to show (or templateUrl: './x.html')
  styles: `h1 { color: red }`, // how it looks (or styleUrl)
})
export class NameComponent {
  // data and methods for the template
}""",
        "programs": [{
            "file": "hello-world.component.ts", "kind": "component",
            "code": r"""import { Component } from '@angular/core';

// A component is a TypeScript class + an HTML template + CSS styles.
@Component({
  selector: 'app-root', // the tag <app-root> in index.html will show this component
  template: `
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
  `,
  styles: `
    h1 { color: #dd0031; }
  `,
})
export class HelloWorldComponent {
  // Properties of the class can be shown in the template with {{ }}
  title = 'Hello, Angular!';
  message = 'My first Angular component is running.';
}
""",
        }],
        "tamil": [
            "சென்னை மெட்ரோ ரயில் நிலையத்தில் உள்ள அறிவிப்புத் திரையை நினைத்துப் பாருங்கள். அடுத்த ரயில் எப்போது வரும் "
            "என்ற நேரம் மட்டும் மாறுகிறது; முழு நிலையக் கட்டிடமும் மீண்டும் கட்டப்படுவதில்லை. அதே போலத்தான் "
            "Angular-இல் (SPA) பக்கம் ஒரு முறை மட்டுமே ஏற்றப்படும், அதன் பிறகு மாற வேண்டிய பகுதி மட்டும் "
            "புதுப்பிக்கப்படும்.",
            "அந்தத் திரையில் உள்ள ஒவ்வொரு பகுதியும் - ரயில் பெயர், நேரம், நடைமேடை எண் - ஒவ்வொரு தனித் "
            "**component** போல. பல component-களை ஒன்றாகச் சேர்த்துதான் முழு Angular செயலியை உருவாக்குகிறோம்.",
        ],
        "mistakes": [
            "Confusing **AngularJS** (old, 2010, JavaScript) with **Angular** (2016+, TypeScript). They are different frameworks.",
            "Thinking you must learn everything at once. Start with components and templates; the rest comes step by step.",
            "Skipping TypeScript basics, then getting stuck on error messages.",
            "Trying to edit the DOM directly (`document.getElementById`) instead of using template bindings.",
        ],
        "interview": [
            ("What is Angular?", "A TypeScript-based, open-source framework by Google for building single page web applications using components."),
            ("What is the difference between AngularJS and Angular?", "AngularJS (1.x) is JavaScript with controllers and scopes. Angular (2+) is a TypeScript rewrite built on components, with better performance and tooling."),
            ("What is a Single Page Application?", "An app that loads one HTML page and updates parts of it dynamically using JavaScript instead of reloading full pages."),
            ("Name the main building blocks of Angular.", "Components, templates, directives, pipes, services with dependency injection, modules/standalone components and the router."),
        ],
        "exercises": [
            "Write down 3 websites you use daily that behave like a SPA (no full reload when you click around).",
            "In `hello-world.component.ts`, change the title and message, then add a second `<p>` using a new property.",
            "Draw (on paper) the component tree for a shopping website: header, product list, product card, cart.",
        ],
    },
    # ------------------------------------------------------------------ 02
    {
        "slug": "Setup_and_Angular_CLI", "title": "Environment Setup and Angular CLI", "level": B,
        "summary": "Install Node.js, create a project with `ng new`, understand the folder structure and CLI commands.",
        "definition": [
            "To build Angular apps you need **Node.js** (runs JavaScript tools on your computer), **npm** (installs "
            "packages) and the **Angular CLI** (the `ng` command). The CLI creates projects, generates components, "
            "starts a dev server and builds your app for production.",
            "A new project contains `src/main.ts` (the entry point that starts the app), `src/app/app.ts` (the root "
            "component), `src/app/app.config.ts` (app-wide settings/providers) and `angular.json` (build settings).",
        ],
        "diagram": {"type": "flow", "caption": "What happens when you run the app",
                    "steps": [("ng serve", "dev server"), ("main.ts", "entry point"), ("bootstrapApplication", "starts Angular"),
                              ("<app-root>", "root component shows in index.html")]},
        "syntax": """# install tools (once)
npm install -g @angular/cli

# create and run a project
ng new my-first-app
cd my-first-app
ng serve            # http://localhost:4200

# generate code
ng generate component product-card   # short: ng g c product-card
ng generate service data
ng build            # production build into dist/""",
        "syntax_lang": "bash",
        "programs": [{
            "file": "app.ts", "kind": "component",
            "code": r"""import {
  ApplicationConfig,
  Component,
  provideBrowserGlobalErrorListeners,
} from '@angular/core';

// In a real project this goes in src/app/app.config.ts.
// main.ts then runs:  bootstrapApplication(App, appConfig)
export const appConfig: ApplicationConfig = {
  providers: [provideBrowserGlobalErrorListeners()],
};

// In a real project this is src/app/app.ts (the root component made by `ng new`).
@Component({
  selector: 'app-root',
  template: `
    <h1>Welcome to {{ appName }}</h1>
    <p>Created with: ng new {{ appName }}</p>
    <p>Started with: ng serve</p>
  `,
})
export class App {
  appName = 'my-first-app';
}
""",
        }],
        "tamil": [
            "ஒரு புதிய கடை திறக்கும்போது கட்டிடம், மின்சாரம், தண்ணீர் இணைப்பு, அலமாரிகள் எல்லாம் முதலில் தயார் செய்ய "
            "வேண்டும். அந்த வேலையை ஒவ்வொன்றாகச் செய்யாமல், ஒரு ஒப்பந்தக்காரர் (contractor) ஒரே நாளில் எல்லாவற்றையும் "
            "அமைத்துக் கொடுத்தால் எவ்வளவு எளிது!",
            "Angular CLI அந்த ஒப்பந்தக்காரர் போல. `ng new` என்று ஒரு கட்டளை கொடுத்தால் முழு project அமைப்பும் "
            "தயார்; `ng generate component` என்றால் புதிய அலமாரி தயார்; `ng serve` என்றால் கடை திறந்து வாடிக்கையாளர் "
            "பார்க்கலாம்.",
        ],
        "mistakes": [
            "Using an unsupported Node.js version. Check the Angular docs for the compatible Node versions.",
            "Running `ng serve` outside the project folder (it must be where `angular.json` is).",
            "Editing files in `node_modules` or `dist`; they are generated and your changes will be lost.",
            "Creating files by hand and forgetting to import them. `ng generate` avoids this.",
        ],
        "interview": [
            ("What is the Angular CLI?", "A command-line tool (`ng`) that creates, builds, tests and serves Angular applications and generates code."),
            ("What does `main.ts` do?", "It is the entry point; it calls `bootstrapApplication` to start the root component."),
            ("What is `angular.json`?", "The workspace configuration file holding build, serve and test settings for projects."),
            ("What is the difference between `ng serve` and `ng build`?", "`ng serve` runs a live-reloading dev server; `ng build` produces optimised static files for deployment."),
        ],
        "exercises": [
            "Install Node.js and the Angular CLI, then run `ng version` and note the versions.",
            "Create a project with `ng new demo`, run `ng serve`, and change the title in `app.ts` while the server is running.",
            "Run `ng generate component hello` and list which files were created.",
        ],
    },
    # ------------------------------------------------------------------ 03
    {
        "slug": "TypeScript_Essentials", "title": "TypeScript Essentials", "level": B,
        "summary": "Types, interfaces, classes, generics and modules - the language Angular is written in.",
        "definition": [
            "**TypeScript** is JavaScript with **types**. You tell the language what kind of value a variable holds "
            "(`string`, `number`, `boolean`...), and the editor warns you about mistakes before you even run the code.",
            "Angular is written in TypeScript, so you will use **interfaces** (shapes of objects), **classes**, "
            "**generics** and **decorators** (like `@Component`) every day. Browsers cannot run TypeScript directly; "
            "the Angular CLI compiles it to JavaScript for you.",
        ],
        "diagram": {"type": "flow", "caption": "TypeScript is checked and compiled to JavaScript",
                    "steps": [("app.ts", "TypeScript + types"), ("Compiler", "finds type errors"), ("app.js", "plain JavaScript"), ("Browser", "runs it")]},
        "syntax": """let name: string = 'Angular';
let count: number = 10;
let tags: string[] = ['a', 'b'];

interface User { id: number; name: string; email?: string }  // ? = optional

function add(a: number, b: number): number { return a + b; }

class Student { constructor(public name: string) {} }

function first<T>(items: T[]): T | undefined { return items[0]; }  // generic""",
        "programs": [
            {"file": "types-basics.ts", "kind": "script",
             "code": r"""// Run with: npx tsx types-basics.ts
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
"""},
            {"file": "classes-interfaces.ts", "kind": "script",
             "code": r"""// Run with: npx tsx classes-interfaces.ts
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
"""},
        ],
        "tamil": [
            "ரேஷன் கடையில் பொருள் வாங்கும்போது அரிசிக்கு தனி அளவு (கிலோ), எண்ணெய்க்கு தனி அளவு (லிட்டர்) என்று "
            "ஒவ்வொன்றுக்கும் ஒரு வகை உண்டு. யாராவது 'இரண்டு லிட்டர் அரிசி' என்று கேட்டால் கடைக்காரர் உடனே "
            "'அது தவறு' என்று சொல்லிவிடுவார்.",
            "TypeScript-உம் அப்படியே. `number`, `string` என்று ஒவ்வொரு மதிப்புக்கும் வகையைச் சொல்லிவிட்டால், தவறான "
            "வகையைப் பயன்படுத்தினால் நீங்கள் program-ஐ ஓட்டுவதற்கு முன்பே editor எச்சரிக்கை கொடுக்கும். இதனால் "
            "பிழைகள் குறையும்.",
        ],
        "mistakes": [
            "Using `any` everywhere. It switches off type checking and defeats the purpose of TypeScript.",
            "Forgetting that types disappear at runtime; you cannot check an interface with `typeof` or `instanceof`.",
            "Mixing `==` and `===`; always prefer `===`.",
            "Ignoring the editor's red underline and compiling anyway.",
        ],
        "interview": [
            ("What is TypeScript and why does Angular use it?", "A typed superset of JavaScript. Types catch bugs early, give great editor support and make large apps easier to maintain."),
            ("Interface vs type alias?", "Both describe shapes. Interfaces can be extended/merged and suit object shapes; type aliases can also name unions, tuples and primitives."),
            ("What is `any` vs `unknown`?", "`any` turns off checks. `unknown` is a safe version: you must narrow the type before using the value."),
            ("What are generics?", "Type parameters (like `T`) that let functions and classes work with many types while staying type-safe."),
            ("What does `?` after a property name mean?", "The property is optional; its type is `T | undefined`."),
        ],
        "exercises": [
            "Create an interface `Product` (id, name, price, inStock?) and an array of three products; print the names of those in stock.",
            "Write a generic function `last<T>(items: T[])` that returns the last item, and test it with numbers and strings.",
            "Make a class `BankAccount` with a private balance, `deposit`, `withdraw` (no negative balance) and a `balance` getter.",
        ],
    },
    # ------------------------------------------------------------------ 04
    {
        "slug": "Components", "title": "Components", "level": B,
        "summary": "Create components, use them inside other components and style them.",
        "definition": [
            "A **component** controls one part of the screen. It has three parts: a **class** (data and behaviour), a "
            "**template** (HTML) and **styles** (CSS). The `@Component` decorator ties them together and gives the "
            "component a **selector**, the custom HTML tag you write to use it.",
            "To use one component inside another, add it to the parent's `imports` array and write its selector in "
            "the parent's template. Styles written in a component are **scoped**: they only affect that component.",
        ],
        "diagram": {"type": "tree", "label": "AppComponent", "sub": "<app-root>",
                    "children": [{"label": "HeaderComponent", "sub": "<app-header>"},
                                 {"label": "ProductList", "sub": "<app-product-list>",
                                  "children": [{"label": "ProductCard"}, {"label": "ProductCard"}]},
                                 {"label": "FooterComponent", "sub": "<app-footer>"}],
                    "caption": "Components form a tree. A parent lists the children it uses in `imports`."},
        "syntax": """@Component({
  selector: 'app-child',
  imports: [OtherComponent],     // components/pipes/directives used in the template
  templateUrl: './child.html',   // or inline: template: `...`
  styleUrl: './child.css',       // or inline: styles: `...`
})
export class ChildComponent {}""",
        "programs": [{
            "file": "profile-card.component.ts", "kind": "component",
            "code": r"""import { Component } from '@angular/core';

// A small reusable child component
@Component({
  selector: 'app-profile-card',
  template: `
    <div class="card">
      <h3>{{ name }}</h3>
      <p>{{ role }} - {{ city }}</p>
    </div>
  `,
  // Styles are scoped: they only apply inside this component
  styles: `
    .card { border: 1px solid #999; padding: 8px; margin: 6px; border-radius: 6px; }
    h3 { margin: 0; }
  `,
})
export class ProfileCardComponent {
  name = 'Priya';
  role = 'Frontend Developer';
  city = 'Coimbatore';
}

// The parent (root) component uses the child by its selector
@Component({
  selector: 'app-root',
  imports: [ProfileCardComponent], // <- must list every component used in the template
  template: `
    <h1>Our Team</h1>
    <app-profile-card />
    <app-profile-card />
  `,
})
export class AppComponent {}
""",
        }],
        "tamil": [
            "ஒரு திருமண மண்டபத்தை எடுத்துக்கொள்ளுங்கள். சமையல் பகுதி, அலங்காரம், வரவேற்பு, உணவு பரிமாறும் பகுதி என்று "
            "ஒவ்வொன்றுக்கும் தனிப் பொறுப்பாளர் இருப்பார். ஒவ்வொருவரும் தன் வேலையை மட்டும் பார்த்துக்கொள்வார்கள்; எல்லாம் "
            "சேர்ந்துதான் திருமணம் நடக்கும்.",
            "Angular-இல் ஒவ்வொரு **component**-உம் அப்படியே ஒரு பொறுப்பாளர். Header, Footer, Product list என்று தனித்தனியாக "
            "எழுதி, `imports`-இல் சேர்த்து, பெரிய component-இல் பயன்படுத்துகிறோம். ஒரு பகுதியில் மாற்றம் செய்தால் "
            "மற்றவை பாதிக்கப்படாது - styles scoped ஆக இருப்பதால்.",
        ],
        "mistakes": [
            "Forgetting to add the child component to the parent's `imports`; Angular then reports an unknown element.",
            "Using a selector that does not match the tag in the template (typos like `app-profilecard`).",
            "Putting too much code in one big component instead of splitting it.",
            "Expecting parent CSS to style the child's inside automatically (styles are scoped).",
        ],
        "interview": [
            ("What is a component?", "A class decorated with `@Component` that controls a view through a template and styles."),
            ("What is a selector?", "The custom HTML tag (or attribute) used to place a component in a template."),
            ("What does `standalone` mean?", "A standalone component declares its own `imports` and needs no NgModule. It is the default since Angular 19."),
            ("What is view encapsulation?", "By default Angular scopes component CSS so it does not leak out or in (emulated shadow DOM)."),
        ],
        "exercises": [
            "Make a `product-card` component showing a name and price, and display it three times.",
            "Add a header and footer component and compose them in the root component.",
            "Move the template and CSS of `profile-card` into separate files using `templateUrl` and `styleUrl`.",
        ],
    },
    # ------------------------------------------------------------------ 05
    {
        "slug": "Data_Binding", "title": "Data Binding", "level": B,
        "summary": "Interpolation, property, attribute, event and two-way binding between class and template.",
        "definition": [
            "**Data binding** connects the component class to its template so the screen stays in sync with your data. "
            "Angular has four kinds: **interpolation** `{{ }}` (show a value), **property binding** `[prop]` (set an "
            "element property), **event binding** `(event)` (react to user actions) and **two-way binding** `[(ngModel)]` "
            "(both directions at once).",
            "Remember the brackets: `[ ]` sends data *into* the template, `( )` sends events *out* of it, and "
            "`[( )]` (banana in a box) does both. For `ngModel` you must import `FormsModule`.",
        ],
        "diagram": {"type": "rows", "caption": "Directions of data flow",
                    "rows": [{"title": "Class -> View", "steps": ["Component class", "{{ value }}  /  [property]", "Template"]},
                             {"title": "View -> Class", "steps": ["Template", "(click)  /  (input)", "Component class"]},
                             {"title": "Both ways", "steps": ["Component class", "[(ngModel)]", "Template"]}]},
        "syntax": """{{ expression }}                 <!-- interpolation -->
<button [disabled]="isBusy">      <!-- property binding -->
<div [attr.aria-label]="label">   <!-- attribute binding -->
<button (click)="save()">         <!-- event binding -->
<input [(ngModel)]="name" />      <!-- two-way (needs FormsModule) -->""",
        "syntax_lang": "html",
        "programs": [{
            "file": "data-binding.component.ts", "kind": "component",
            "actions": [["fill", "input", "Karthik"], ["click", "button"], ["click", "button"]],
            "action_notes": ["Type `Karthik` in the text box.", "Click the **Greet** button twice."],
            "code": r"""import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms'; // needed for [(ngModel)]

@Component({
  selector: 'app-root',
  imports: [FormsModule],
  template: `
    <!-- interpolation: show a class value as text -->
    <h2>{{ brand }}</h2>

    <!-- two-way binding [(ngModel)] + attribute binding [attr.aria-label] -->
    <input [(ngModel)]="name" placeholder="Your name" [attr.aria-label]="'Name for ' + brand" />

    <!-- event binding (click) + property binding [disabled] -->
    <button (click)="greet()" [disabled]="name.trim() === ''">Greet</button>

    <p>You typed: {{ name }}</p>
    <p>{{ greeting }}</p>
    <p>Button clicked {{ clicks }} time(s)</p>
  `,
})
export class DataBindingComponent {
  brand = 'Chennai Tea House';
  name = '';
  greeting = '';
  clicks = 0;

  greet() {
    this.greeting = `Vanakkam, ${this.name}!`;
    this.clicks++;
  }
}
""",
        }],
        "tamil": [
            "தேநீர்க் கடையில் நீங்கள் 'ஒரு டீ, சர்க்கரை குறைவா' என்று சொல்கிறீர்கள். மாஸ்டர் உடனே அதை கவனித்து அதன்படி "
            "டீ போடுகிறார்; விலைப்பட்டியல் பலகையில் உள்ள விலையை நீங்கள் படித்துக்கொள்கிறீர்கள். இரண்டு பக்கமும் தகவல் "
            "பரிமாறப்படுகிறது.",
            "பலகையில் உள்ள விலை = `{{ price }}` (class-இலிருந்து திரைக்கு). நீங்கள் சொல்லும் ஆர்டர் = `(click)` அல்லது "
            "`(input)` (திரையிலிருந்து class-க்கு). இரண்டும் எப்போதும் ஒத்திசைவாக இருப்பது = `[(ngModel)]`.",
        ],
        "mistakes": [
            "Forgetting to import `FormsModule`, which causes \"Can't bind to 'ngModel'\".",
            "Writing `{{ }}` inside a property binding like `[title]=\"{{ x }}\"`; use `[title]=\"x\"` instead.",
            "Mixing up `[ ]` and `( )` brackets.",
            "Putting heavy logic or function calls inside templates; they run on every change detection.",
        ],
        "interview": [
            ("What are the types of data binding in Angular?", "Interpolation, property binding, attribute binding, class/style binding, event binding and two-way binding."),
            ("Interpolation vs property binding?", "Interpolation converts the value to a string inside text; property binding sets a DOM property with its real type (boolean, object...)."),
            ("What is two-way binding?", "Combining property and event binding, written `[(ngModel)]`, so the view and the class update each other."),
            ("When do you use `[attr.x]`?", "When there is no DOM property for it (like `aria-*` or `colspan`), so you must set the HTML attribute."),
        ],
        "exercises": [
            "Build a temperature converter: an input for Celsius and text showing Fahrenheit.",
            "Add a button that is disabled until a checkbox is ticked.",
            "Make a character counter that shows how many letters are typed in a textarea.",
        ],
    },
    # ------------------------------------------------------------------ 06
    {
        "slug": "Control_Flow", "title": "Control Flow (@if, @for, @switch)", "level": B,
        "summary": "Show, hide and repeat parts of the template with the built-in control flow blocks.",
        "definition": [
            "**Control flow** decides *what* appears in the template. Angular's built-in blocks are `@if` / `@else` "
            "(conditions), `@for` (repeat a list) and `@switch` (choose one of many cases). They replaced the older "
            "`*ngIf` and `*ngFor` and need no imports.",
            "`@for` needs a **track** expression (usually an id) so Angular can reuse DOM elements efficiently when "
            "the list changes. Add `@empty` to show a message when the list is empty.",
        ],
        "diagram": {"type": "flow", "caption": "Angular evaluates the condition on every change and updates the DOM",
                    "steps": [("@if (open)", "condition"), ("true", "render block"), ("false", "render @else block")]},
        "syntax": """@if (condition) { ... } @else if (other) { ... } @else { ... }

@for (item of items; track item.id; let i = $index) { ... } @empty { ... }

@switch (value) {
  @case ('a') { ... }
  @default { ... }
}""",
        "syntax_lang": "html",
        "programs": [{
            "file": "tea-menu.component.ts", "kind": "component",
            "actions": [["click", "button"]],
            "action_notes": ["Click the **Open shop** button."],
            "code": r"""import { Component, signal } from '@angular/core';

interface Tea {
  name: string;
  price: number;
  available: boolean;
}

@Component({
  selector: 'app-root',
  template: `
    <button (click)="open.set(!open())">{{ open() ? 'Close' : 'Open' }} shop</button>

    @if (open()) {
      <h3>Today's Menu</h3>
      <ul>
        @for (item of menu; track item.name; let i = $index) {
          <li>
            {{ i + 1 }}. {{ item.name }} - ₹{{ item.price }}
            @switch (item.available) {
              @case (true) { (available) }
              @case (false) { (sold out) }
            }
          </li>
        } @empty {
          <li>No items today</li>
        }
      </ul>
    } @else {
      <p>The shop is closed.</p>
    }
  `,
})
export class TeaMenuComponent {
  open = signal(false);
  menu: Tea[] = [
    { name: 'Filter Coffee', price: 20, available: true },
    { name: 'Masala Tea', price: 15, available: true },
    { name: 'Badam Milk', price: 30, available: false },
  ];
}
""",
        }],
        "tamil": [
            "ஒரு திரையரங்கு டிக்கெட் கவுண்டரைப் பாருங்கள். 'டிக்கெட் இருக்கிறதா?' என்பதே `@if`. இருந்தால் டிக்கெட் கொடுப்பார்; "
            "இல்லையென்றால் 'ஹவுஸ்ஃபுல்' பலகை காட்டுவார் (`@else`).",
            "வரிசையில் நிற்கும் ஒவ்வொருவருக்கும் ஒரே செயலைச் செய்வது `@for`. யாருமே வரிசையில் இல்லையென்றால் 'இன்று காட்சி இல்லை' "
            "என்று காட்டுவது `@empty`. காலை, மதியம், இரவு என்று காட்சி நேரத்துக்கு ஏற்ப வேறு வேறு வேலை செய்வது `@switch`.",
        ],
        "mistakes": [
            "Leaving out `track` in `@for` (it is required) or tracking by array index for lists that change.",
            "Still using `*ngIf` / `*ngFor` in new code; the new blocks are faster and simpler.",
            "Forgetting that signals are called like functions: `open()` not `open`.",
            "Putting `@else` on a new line before the closing brace of `@if` incorrectly; it must follow `}`.",
        ],
        "interview": [
            ("What replaced `*ngIf` and `*ngFor`?", "The built-in control flow blocks `@if`, `@for` and `@switch` (stable since Angular 17)."),
            ("Why is `track` required in `@for`?", "It lets Angular identify items so it can move/reuse DOM nodes instead of re-creating the whole list."),
            ("What is `@empty`?", "A block displayed when the `@for` collection has no items."),
            ("Do the new control flow blocks need imports?", "No, they are part of the template syntax."),
        ],
        "exercises": [
            "Show a list of 5 students; display 'Pass' or 'Fail' using `@if` based on marks.",
            "Use `@switch` to show a different message for each day of the week.",
            "Add a button to the tea menu that removes an item and check that `@empty` appears at the end.",
        ],
    },
    # ------------------------------------------------------------------ 07
    {
        "slug": "Directives_and_Styling", "title": "Directives, Class and Style Binding", "level": B,
        "summary": "Change CSS classes and styles dynamically with [class], [style], NgClass and NgStyle.",
        "definition": [
            "A **directive** is an instruction that changes how an element looks or behaves. There are three kinds: "
            "components (directives with a template), **structural** directives (change the DOM structure, like `@if`) "
            "and **attribute** directives (change appearance, like `NgClass`).",
            "The easiest ways to style dynamically are **class binding** `[class.active]=\"cond\"` and **style binding** "
            "`[style.color]=\"value\"`. For many classes at once use `NgClass` / `NgStyle` with an object.",
        ],
        "diagram": {"type": "flow", "caption": "A signal changes -> bindings recalculate -> DOM classes/styles update",
                    "steps": [("isHot = true", "state"), ("[class.hot]", "binding"), ("<p class='hot'>", "DOM")]},
        "syntax": """<p [class.active]="isActive">...</p>
<p [style.color]="color" [style.font-size.px]="size">...</p>
<p [ngClass]="{ big: isBig, small: !isBig }">...</p>
<p [ngStyle]="{ 'background-color': bg }">...</p>""",
        "syntax_lang": "html",
        "programs": [{
            "file": "dynamic-style.component.ts", "kind": "component",
            "actions": [["click", "#temp"], ["click", "#size"]],
            "action_notes": ["Click **Toggle temperature**.", "Click **Bigger text**."],
            "code": r"""import { Component, computed, signal } from '@angular/core';
import { NgClass, NgStyle } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [NgClass, NgStyle],
  template: `
    <!-- class binding: add the "hot" class only when isHot() is true -->
    <p [class.hot]="isHot()">Tea is {{ isHot() ? 'hot' : 'cold' }}</p>

    <!-- NgClass with an object: several classes at once -->
    <p [ngClass]="{ big: size() > 16, small: size() <= 16 }">Size {{ size() }}px</p>

    <!-- style binding with a unit -->
    <p [style.font-size.px]="size()">This text resizes</p>

    <!-- NgStyle with an object -->
    <p [ngStyle]="{ color: textColor(), 'font-weight': 'bold' }">Colour: {{ textColor() }}</p>

    <button id="temp" (click)="isHot.set(!isHot())">Toggle temperature</button>
    <button id="size" (click)="size.update(s => s + 4)">Bigger text</button>
  `,
  styles: `
    .hot { color: crimson; }
    .big { text-decoration: underline; }
  `,
})
export class DynamicStyleComponent {
  isHot = signal(true);
  size = signal(14);
  // computed: derived value that updates automatically
  textColor = computed(() => (this.isHot() ? 'crimson' : 'royalblue'));
}
""",
        }],
        "tamil": [
            "பொங்கல் அன்று வீட்டு வாசலில் கோலம் போடுகிறோம். சாதாரண நாட்களில் சிறிய கோலம்; பண்டிகை நாளில் வண்ணக் கோலம். "
            "வாசல் அதே வாசல்தான், ஆனால் நாளுக்கு ஏற்ப அதன் தோற்றம் மாறுகிறது.",
            "அதுபோல HTML element அதேதான்; `[class.hot]` அல்லது `[style.color]` மூலம் நிலைக்கு (state) ஏற்ப அதன் "
            "நிறம், அளவு, வடிவம் தானாக மாறும். நிலை மாறினால் தோற்றமும் உடனே மாறும் - நாம் கையால் DOM-ஐ மாற்ற வேண்டியதில்லை.",
        ],
        "mistakes": [
            "Using `[class]=\"'a b'\"` and accidentally removing other classes; prefer `[class.name]` for single classes.",
            "Forgetting units, e.g. `[style.font-size]=\"16\"` instead of `[style.font-size.px]=\"16\"`.",
            "Forgetting to import `NgClass` / `NgStyle` in a standalone component.",
            "Writing inline styles for everything instead of using CSS classes.",
        ],
        "interview": [
            ("What are structural vs attribute directives?", "Structural directives add/remove elements (`@if`, `@for`); attribute directives change an element's look or behaviour (`NgClass`)."),
            ("`[ngClass]` vs `[class.x]`?", "`[class.x]` toggles one class with a boolean; `[ngClass]` handles many classes via object, array or string."),
            ("Is `*ngIf` still valid?", "Yes but deprecated in favour of `@if`; new code should use the control flow blocks."),
            ("How do you bind a CSS unit?", "Add the unit after the style name, e.g. `[style.width.px]` or `[style.height.%]`."),
        ],
        "exercises": [
            "Make a dark/light theme toggle that changes the background and text colour of a card.",
            "Highlight the row of a list item when the mouse clicks on it (use `[class.selected]`).",
            "Create a progress bar whose width is bound to a number from an input slider.",
        ],
    },
    # ------------------------------------------------------------------ 08
    {
        "slug": "Signals", "title": "Signals (signal, computed, effect)", "level": B,
        "summary": "Angular's modern reactive state: writable signals, derived values and side effects.",
        "definition": [
            "A **signal** is a box that holds a value and tells Angular whenever the value changes. You **read** it by "
            "calling it like a function (`count()`) and **write** with `.set()` or `.update()`. Because Angular knows "
            "exactly which templates read which signals, only the parts that need to change are refreshed.",
            "`computed()` creates a read-only signal **derived** from other signals (it recalculates automatically and "
            "caches the result). `effect()` runs code (a side effect, like logging or saving) whenever the signals it "
            "reads change.",
        ],
        "diagram": {"type": "flow", "caption": "Change flows automatically from source signals to derived values and the screen",
                    "steps": [("price, qty", "signal()"), ("total", "computed()"), ("Template", "{{ total() }}"), ("effect()", "side effects")]},
        "syntax": """const count = signal(0);          // create
count();                          // read -> 0
count.set(5);                     // replace
count.update(c => c + 1);         // change based on old value
const double = computed(() => count() * 2);
effect(() => console.log(count()));""",
        "programs": [{
            "file": "cart-signals.component.ts", "kind": "component",
            "actions": [["click", "#inc"], ["click", "#inc"], ["click", "#dec"]],
            "action_notes": ["Click **+** twice.", "Click **-** once."],
            "code": r"""import { Component, computed, effect, signal, untracked } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <h3>Idli Order</h3>
    <button id="dec" (click)="dec()">-</button>
    <strong>{{ plates() }}</strong>
    <button id="inc" (click)="inc()">+</button>

    <p>Price per plate: ₹{{ price }}</p>
    <p>Total: ₹{{ total() }}</p>

    <h4>Change history (written by an effect)</h4>
    <ul>
      @for (h of history(); track $index) { <li>{{ h }}</li> }
    </ul>
  `,
})
export class CartSignalsComponent {
  price = 30;
  plates = signal(1); // writable signal

  // computed: derived, read-only, cached
  total = computed(() => this.plates() * this.price);

  history = signal<string[]>([]);

  constructor() {
    // effect: runs once now and again whenever plates() changes
    effect(() => {
      const message = `plates = ${this.plates()}`;
      // untracked: do not re-run this effect when history changes
      untracked(() => this.history.update((h) => [...h, message]));
    });
  }

  inc() { this.plates.update((n) => n + 1); }
  dec() { this.plates.update((n) => Math.max(1, n - 1)); }
}
""",
        }],
        "tamil": [
            "இட்லிக் கடையில் நீங்கள் ஆர்டர் செய்யும் தட்டுகளின் எண்ணிக்கையை (plates) மாற்றினால், பில் தொகை "
            "(total) தானாகவே மாறுகிறது. கடைக்காரர் ஒவ்வொரு முறையும் புதிதாகக் கணக்குப் போட வேண்டியதில்லை - ஏனெனில் "
            "'தட்டு × விலை' என்ற சூத்திரம் அவர் மனதில் இருக்கிறது.",
            "`signal` = தட்டுகளின் எண்ணிக்கை. `computed` = பில் தொகை (தானாக மாறும்). `effect` = ஒவ்வொரு ஆர்டர் "
            "மாற்றத்தையும் நோட்டுப் புத்தகத்தில் எழுதி வைப்பது போன்ற கூடுதல் வேலை.",
        ],
        "mistakes": [
            "Forgetting the parentheses when reading a signal (`count` vs `count()`).",
            "Mutating an array/object inside a signal (`list().push(x)`); create a new one with `update` instead.",
            "Setting signals inside `computed()`; computed must be pure.",
            "Overusing `effect()` to copy state between signals; use `computed()` instead.",
        ],
        "interview": [
            ("What is a signal?", "A reactive value container; reading it in a template or computed registers a dependency so Angular updates only what changed."),
            ("`computed` vs `effect`?", "`computed` derives a value and returns a signal; `effect` performs a side effect and returns nothing."),
            ("`set` vs `update`?", "`set` assigns a new value; `update` receives the old value and returns the new one."),
            ("How are signals different from RxJS Observables?", "Signals always have a current value and are synchronous; Observables are streams over time. They interoperate via `toSignal` and `toObservable`."),
        ],
        "exercises": [
            "Create a `quantity` and `price` signal and a `computed` total including 18% GST.",
            "Use `effect` to save a counter value into `localStorage` every time it changes.",
            "Build a to-do counter showing the number of completed tasks with `computed`.",
        ],
    },
    # ------------------------------------------------------------------ 09
    {
        "slug": "Component_Communication", "title": "Component Communication (input, output, model)", "level": B,
        "summary": "Pass data down with input(), send events up with output(), and sync with model().",
        "definition": [
            "Components rarely work alone. A **parent** passes data to a **child** using an **input** and the child "
            "tells the parent something happened using an **output** event. The rule of thumb is: *data goes down, "
            "events go up*.",
            "Modern Angular uses the functions `input()`, `input.required()` and `output()`. `model()` creates a "
            "writable input that also emits changes, so the parent can use two-way binding `[(name)]`.",
        ],
        "diagram": {"type": "rows", "caption": "Data goes down, events go up",
                    "rows": [{"title": "Parent -> Child", "steps": ["Parent", "[title]=\"...\"", "Child input()"]},
                             {"title": "Child -> Parent", "steps": ["Child output()", "(liked)=\"...\"", "Parent method"]},
                             {"title": "Two-way", "steps": ["Parent signal", "[(count)]", "Child model()"]}]},
        "syntax": """// child
title  = input.required<string>();   // value from parent
liked  = output<string>();           // event to parent
count  = model(0);                   // two-way value

// parent template
<app-child [title]="x" (liked)="onLiked($event)" [(count)]="total" />""",
        "programs": [{
            "file": "like-button.component.ts", "kind": "component",
            "actions": [["click", "app-like-button button"], ["click", "app-stepper .plus"], ["click", "app-stepper .plus"]],
            "action_notes": ["Click the **Like** button.", "Click the stepper's **+** twice."],
            "code": r"""import { Component, input, model, output, signal } from '@angular/core';

// ---- Child 1: input() and output() ----
@Component({
  selector: 'app-like-button',
  template: `<button (click)="liked.emit(title())">Like "{{ title() }}"</button>`,
})
export class LikeButtonComponent {
  title = input.required<string>(); // data coming IN from the parent
  liked = output<string>();         // events going OUT to the parent
}

// ---- Child 2: model() = two-way binding ----
@Component({
  selector: 'app-stepper',
  template: `
    <button class="minus" (click)="count.set(count() - 1)">-</button>
    {{ count() }}
    <button class="plus" (click)="count.set(count() + 1)">+</button>
  `,
})
export class StepperComponent {
  count = model(0);
}

// ---- Parent ----
@Component({
  selector: 'app-root',
  imports: [LikeButtonComponent, StepperComponent],
  template: `
    <app-like-button title="Angular Basics" (liked)="onLiked($event)" />
    <p>Last liked: {{ last() || 'nothing yet' }}</p>

    <app-stepper [(count)]="total" />
    <p>Parent sees total = {{ total() }}</p>
  `,
})
export class AppComponent {
  last = signal('');
  total = signal(0);

  onLiked(title: string) {
    this.last.set(title);
  }
}
""",
        }],
        "tamil": [
            "ஒரு வீட்டில் அம்மா (parent) சமையலறையில் இருக்கும் குழந்தைக்கு (child) 'அரை கிலோ அரிசி எடுத்து வா' என்று "
            "சொல்கிறார் - இது **input** (மேலிருந்து கீழே தகவல்). குழந்தை அரிசியுடன் வந்து 'எடுத்துவிட்டேன்!' என்று "
            "குரல் கொடுக்கிறது - இது **output** (கீழிருந்து மேலே நிகழ்வு).",
            "இருவரும் ஒரே எண்ணை (எ.கா. மீதமுள்ள அரிசி அளவு) பகிர்ந்து புதுப்பித்துக்கொண்டால் அது **model()** - "
            "இருவழி இணைப்பு.",
        ],
        "mistakes": [
            "Trying to change an input's value inside the child; inputs are read-only (use `model()` if the child must write).",
            "Forgetting `()` when reading a signal input: `title` vs `title()`.",
            "Using `$event` wrongly; for `output<string>()`, `$event` is the emitted string.",
            "Passing data up by changing the parent's object from the child (hard-to-trace bugs). Emit an event instead.",
        ],
        "interview": [
            ("How does a parent pass data to a child?", "With property binding to an `input()` of the child, e.g. `<app-child [title]=\"t\" />`."),
            ("How does a child notify its parent?", "By emitting an `output()` event that the parent handles with `(eventName)=\"handler($event)\"`."),
            ("What is `input.required`?", "An input that the parent must provide; the compiler errors if it is missing."),
            ("What is `model()`?", "A signal that works as an input and an output at once, enabling `[(prop)]` two-way binding."),
            ("Old vs new syntax?", "Older code uses `@Input()` / `@Output() EventEmitter` decorators; both still work, but functions are recommended."),
        ],
        "exercises": [
            "Create a `rating-star` child that takes a `value` input and emits a `rated` event when a star is clicked.",
            "Make a `todo-item` child that receives a task object and emits `delete` with the task id.",
            "Use `model()` to build a `toggle-switch` that parents can bind with `[(on)]`.",
        ],
    },
    # ------------------------------------------------------------------ 10
    {
        "slug": "Pipes", "title": "Pipes", "level": B,
        "summary": "Format data in templates with built-in pipes and write your own custom pipe.",
        "definition": [
            "A **pipe** transforms a value for display, without changing the original data. You write it in the "
            "template with the `|` symbol: `{{ name | uppercase }}`. Pipes can take arguments after a colon "
            "and can be chained.",
            "Angular has many built-in pipes: `date`, `currency`, `percent`, `uppercase`, `lowercase`, `slice`, `json`, "
            "`async` and more. You can create a **custom pipe** with the `@Pipe` decorator and a `transform` method.",
        ],
        "diagram": {"type": "flow", "caption": "A pipe sits between the raw value and the screen",
                    "steps": [("1299.5", "raw value"), ("currency:'INR'", "pipe"), ("₹1,299.50", "displayed")]},
        "syntax": """{{ value | pipeName }}
{{ value | pipeName:arg1:arg2 }}
{{ today | date:'dd MMM yyyy' | uppercase }}   // chained

@Pipe({ name: 'myPipe' })
export class MyPipe implements PipeTransform {
  transform(value: string, arg = 1): string { return ...; }
}""",
        "programs": [{
            "file": "pipes-demo.component.ts", "kind": "component",
            "code": r"""import { CurrencyPipe, DatePipe, JsonPipe, PercentPipe, SlicePipe, UpperCasePipe } from '@angular/common';
import { Component, Pipe, PipeTransform } from '@angular/core';

// A custom pipe: shortens long text
@Pipe({ name: 'truncate' })
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 10): string {
    return value.length > limit ? value.slice(0, limit) + '...' : value;
  }
}

@Component({
  selector: 'app-root',
  imports: [CurrencyPipe, DatePipe, JsonPipe, PercentPipe, SlicePipe, UpperCasePipe, TruncatePipe],
  template: `
    <p>Upper: {{ course | uppercase }}</p>
    <p>Price: {{ price | currency: 'INR' : 'symbol' : '1.2-2' }}</p>
    <p>Date: {{ launch | date: 'dd MMM yyyy' }}</p>
    <p>Discount: {{ discount | percent }}</p>
    <p>First two: {{ cities | slice: 0 : 2 }}</p>
    <p>Truncated: {{ about | truncate: 14 }}</p>
    <p>Chained: {{ launch | date: 'MMMM' | uppercase }}</p>
    <pre>{{ student | json }}</pre>
  `,
})
export class PipesDemoComponent {
  course = 'angular pipes';
  price = 1299.5;
  launch = new Date(2026, 0, 26); // 26 January 2026
  discount = 0.256;
  cities = ['Chennai', 'Madurai', 'Trichy', 'Salem'];
  about = 'Pipes transform values for display';
  student = { name: 'Arun', marks: [82, 91] };
}
""",
        }],
        "tamil": [
            "காய்கறிக் கடையில் தக்காளி கிலோ ₹40 என்று கடைக்காரர் மனதில் இருக்கிறது. ஆனால் பில்லில் 'தக்காளி - 2 கிலோ - "
            "₹80.00' என்று அழகாக வடிவமைத்து எழுதுகிறார். தக்காளியின் உண்மையான விலை மாறவில்லை; காட்டும் விதம் மட்டுமே மாறியது.",
            "**Pipe** அதே வேலையைச் செய்கிறது. தரவு (data) அப்படியே இருக்கும்; திரையில் காட்டும்போது தேதி, பணம், "
            "சதவீதம் என்று அழகாக மாற்றிக் காட்டும்.",
        ],
        "mistakes": [
            "Forgetting to import the pipe (e.g. `CurrencyPipe`) in a standalone component's `imports`.",
            "Using a pipe to change the original data; pipes only change what is displayed.",
            "Making a pipe impure or heavy; calling slow code inside `transform` runs often.",
            "Wrong arguments order for `currency` (`code:display:digitsInfo`).",
        ],
        "interview": [
            ("What is a pipe?", "A template feature that transforms a value for display, using `|`."),
            ("Pure vs impure pipes?", "Pure pipes run only when their input reference changes (default, fast); impure pipes run on every change detection."),
            ("How do you create a custom pipe?", "Use `@Pipe({name})` on a class implementing `PipeTransform` with a `transform` method, and import it where needed."),
            ("Pipe vs a method call in the template?", "Pure pipes are cached and only recalculated when inputs change; a method call runs on every change detection."),
        ],
        "exercises": [
            "Display a list of prices in INR using `currency` and sort them in the component.",
            "Write a custom `initials` pipe: 'Arun Kumar' -> 'AK'.",
            "Show today's date in three different formats using the `date` pipe.",
        ],
    },
]
