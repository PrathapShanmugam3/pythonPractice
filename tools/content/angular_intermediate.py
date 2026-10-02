"""Angular - Intermediate topics (11-22)."""

I = "Intermediate"

TOPICS = [
    # ------------------------------------------------------------------ 11
    {
        "slug": "Services_and_DI", "title": "Services and Dependency Injection", "level": I,
        "summary": "Share logic and data between components with injectable services.",
        "definition": [
            "A **service** is a plain class that holds logic or data you want to share (loading data, a shopping cart, "
            "logging). Components should focus on the screen; services do the real work.",
            "**Dependency Injection (DI)** means Angular creates the service for you and hands it over when a class asks "
            "for it with `inject(ServiceName)`. With `providedIn: 'root'` there is exactly **one shared instance** for the "
            "whole app, so every component sees the same data.",
        ],
        "diagram": {"type": "tree", "label": "Injector", "sub": "creates ONE CartService",
                    "children": [{"label": "ProductList", "sub": "inject(CartService)"},
                                 {"label": "CartBadge", "sub": "inject(CartService)"}],
                    "caption": "Both components receive the same service object, so they stay in sync."},
        "syntax": """@Injectable({ providedIn: 'root' })
export class DataService {
  getItems() { return ['a', 'b']; }
}

@Component({...})
export class MyComponent {
  private data = inject(DataService);   // ask Angular for it
}""",
        "programs": [{
            "file": "cart-service.component.ts", "kind": "component",
            "actions": [["click", "app-product-list button:nth-of-type(1)"], ["click", "app-product-list button:nth-of-type(1)"],
                        ["click", "app-product-list button:nth-of-type(2)"]],
            "action_notes": ["Click **Add Idli Batter** twice.", "Click **Add Filter Coffee Powder** once."],
            "code": r"""import { Component, computed, inject, Injectable, signal } from '@angular/core';

// A service: ONE shared instance for the whole app (providedIn: 'root')
@Injectable({ providedIn: 'root' })
export class CartService {
  private readonly items = signal<string[]>([]);

  readonly list = this.items.asReadonly(); // others can read, but not change directly
  readonly count = computed(() => this.items().length);

  add(item: string) {
    this.items.update((current) => [...current, item]);
  }

  clear() {
    this.items.set([]);
  }
}

// Component 1 writes to the cart
@Component({
  selector: 'app-product-list',
  template: `
    @for (p of products; track p) {
      <button (click)="cart.add(p)">Add {{ p }}</button>
    }
  `,
})
export class ProductListComponent {
  products = ['Idli Batter', 'Filter Coffee Powder'];
  cart = inject(CartService); // dependency injection
}

// Component 2 reads the SAME cart
@Component({
  selector: 'app-cart-badge',
  template: `
    <p>Cart items: {{ cart.count() }}</p>
    <ul>
      @for (item of cart.list(); track $index) { <li>{{ item }}</li> }
    </ul>
  `,
})
export class CartBadgeComponent {
  cart = inject(CartService);
}

@Component({
  selector: 'app-root',
  imports: [ProductListComponent, CartBadgeComponent],
  template: `
    <h2>Online Grocery</h2>
    <app-product-list />
    <app-cart-badge />
  `,
})
export class AppComponent {}
""",
        }],
        "tamil": [
            "ஒரு ஊரில் எல்லாரும் ஒரே பொதுக் குடிநீர்க் குழாயைப் பயன்படுத்துகிறார்கள். ஒவ்வொரு வீடும் தனியாக ஆழ்குழாய்க் கிணறு "
            "தோண்டத் தேவையில்லை. ஒரு வீட்டில் தண்ணீர் எடுத்தால் மற்ற வீடுகளுக்கும் அதே நீர்த்தொட்டியின் நிலை தெரியும்.",
            "**Service** அந்தப் பொதுக் குழாய் போல - ஒரே ஒரு பிரதி, எல்லா component-களும் பகிர்ந்துகொள்ளும். **Dependency "
            "Injection** என்பது குழாய் இணைப்பை உங்கள் வீடு வரை கொண்டுவந்து கொடுக்கும் நகராட்சி ஊழியர் போல; நாமே கிணறு தோண்ட "
            "வேண்டியதில்லை, `inject()` என்று கேட்டால் போதும்.",
        ],
        "mistakes": [
            "Creating a service with `new CartService()` instead of injecting it; you lose the shared instance.",
            "Forgetting `@Injectable({ providedIn: 'root' })`, which gives a \"No provider\" error.",
            "Putting HTTP calls and business logic inside components instead of services.",
            "Exposing a writable signal publicly so any component can change it unexpectedly.",
        ],
        "interview": [
            ("What is a service in Angular?", "A class that encapsulates reusable logic or state, injected into components and other services."),
            ("What is dependency injection?", "A design pattern where a class receives its dependencies from an injector instead of creating them itself."),
            ("What does `providedIn: 'root'` do?", "Registers the service in the root injector, creating a single app-wide instance (tree-shakable)."),
            ("`inject()` vs constructor injection?", "Both work. `inject()` is shorter, works in field initialisers and functions (guards, interceptors), and is the modern style."),
        ],
        "exercises": [
            "Create a `ThemeService` that stores 'light' or 'dark' and use it in two components.",
            "Make a `LoggerService` with `log(message)` and call it from three components.",
            "Add a `remove(item)` method to `CartService` and a remove button next to each item.",
        ],
    },
    # ------------------------------------------------------------------ 12
    {
        "slug": "Template_Driven_Forms", "title": "Template-Driven Forms", "level": I,
        "summary": "Build simple forms with ngModel, ngForm and built-in HTML validation attributes.",
        "definition": [
            "In a **template-driven form** you describe the form mostly in HTML. Add `FormsModule`, put `ngModel` and a "
            "`name` on each input, and Angular builds the form model behind the scenes.",
            "Add validation with HTML attributes like `required`, `minlength` and `email`. Template reference variables "
            "such as `#f=\"ngForm\"` and `#nameCtrl=\"ngModel\"` give you the state: `valid`, `invalid`, `dirty`, `touched` and `errors`. "
            "This style is good for small, simple forms.",
        ],
        "diagram": {"type": "flow", "caption": "Angular tracks each ngModel and the whole ngForm",
                    "steps": [("<input ngModel>", "user types"), ("NgModel", "value + validity"), ("NgForm", "whole form state"), ("(ngSubmit)", "your method")]},
        "syntax": """<form #f="ngForm" (ngSubmit)="save(f.value)">
  <input name="email" [(ngModel)]="model.email" required email #e="ngModel" />
  @if (e.invalid && e.touched) { <small>Invalid email</small> }
  <button [disabled]="f.invalid">Save</button>
</form>""",
        "syntax_lang": "html",
        "programs": [{
            "file": "register-form.component.ts", "kind": "component",
            "actions": [["fill", "#name", "Ra"], ["snap", "Name too short"], ["fill", "#name", "Ravi"],
                        ["fill", "#email", "ravi@example.com"], ["click", "button[type=submit]"], ["snap", "After submit"]],
            "action_notes": ["Type `Ra` in the name box (too short).", "Type a valid name and email, then click **Register**."],
            "code": r"""import { Component } from '@angular/core';
import { FormsModule, NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [FormsModule],
  template: `
    <h3>Course Registration</h3>
    <form #f="ngForm" (ngSubmit)="submit(f)">
      <label>Name
        <input id="name" name="name" [(ngModel)]="model.name" required minlength="3" #nameCtrl="ngModel" />
      </label>
      @if (nameCtrl.invalid && (nameCtrl.dirty || nameCtrl.touched)) {
        <small>
          @if (nameCtrl.errors?.['required']) { Name is required. }
          @if (nameCtrl.errors?.['minlength']) { Use at least 3 letters. }
        </small>
      }

      <label>Email
        <input id="email" name="email" type="email" [(ngModel)]="model.email" required email />
      </label>

      <button type="submit" [disabled]="f.invalid">Register</button>
    </form>

    <p>Form valid: {{ f.valid }}</p>
    @if (message) { <p>{{ message }}</p> }
  `,
})
export class RegisterFormComponent {
  model = { name: '', email: '' };
  message = '';

  submit(form: NgForm) {
    this.message = `Registered ${form.value.name} (${form.value.email})`;
    form.resetForm();
  }
}
""",
        }],
        "tamil": [
            "ரயில்வே முன்பதிவுப் படிவத்தை எடுத்துக்கொள்ளுங்கள். பெயர், வயது, பயண நாள் என்று ஒவ்வொரு கட்டமும் அச்சிடப்பட்ட "
            "காகிதம் அங்கேயே இருக்கிறது. பெயர் கட்டத்தை நிரப்பாமல் கவுண்டரில் கொடுத்தால், 'பெயர் எழுதுங்கள்' என்று உடனே திருப்பிக் "
            "கொடுத்துவிடுவார்கள்.",
            "Template-driven form-இல் படிவத்தின் அமைப்பு HTML-இலேயே இருக்கும் (`required`, `minlength`). எல்லாக் கட்டங்களும் "
            "சரியாக இருந்தால் மட்டுமே **Register** பொத்தான் வேலை செய்யும் - கவுண்டர் ஊழியர் சரிபார்த்த பிறகே ஏற்றுக்கொள்வது போல.",
        ],
        "mistakes": [
            "Forgetting the `name` attribute on an `ngModel` input; the control will not register in the form.",
            "Not importing `FormsModule`.",
            "Showing errors immediately on a pristine form; check `dirty` or `touched` first.",
            "Using template-driven forms for big, dynamic forms where reactive forms are easier to test.",
        ],
        "interview": [
            ("What are template-driven forms?", "Forms built mainly in the template with `ngModel`, where Angular creates the form model automatically."),
            ("Why is `name` needed on inputs inside a form?", "NgForm registers each `ngModel` control by its `name` attribute."),
            ("What do `dirty`, `touched`, `valid` mean?", "`dirty`: value changed; `touched`: input was focused then left; `valid`: all validators pass."),
            ("Template-driven vs reactive?", "Template-driven is simpler and implicit; reactive is explicit, more scalable and easier to unit-test."),
        ],
        "exercises": [
            "Build a feedback form with name, rating (select) and comments (required, minimum 10 characters).",
            "Disable the submit button until a 'I agree' checkbox is ticked.",
            "Show a red border on invalid inputs using `[class.invalid]`.",
        ],
    },
    # ------------------------------------------------------------------ 13
    {
        "slug": "Reactive_Forms", "title": "Reactive Forms", "level": I,
        "summary": "Define forms in TypeScript with FormGroup, FormControl and FormBuilder.",
        "definition": [
            "In **reactive forms** you create the form model in the **component class** using `FormGroup` and "
            "`FormControl` (or the shorter `FormBuilder`). The template simply connects to it with `[formGroup]` and "
            "`formControlName`. Everything is explicit, typed and easy to test.",
            "Use `fb.nonNullable.group({...})` to get strongly typed values. Validators are plain functions such as "
            "`Validators.required` and `Validators.email`. You can read the whole value with `form.value` or "
            "`form.getRawValue()` and react to changes with `valueChanges`.",
        ],
        "diagram": {"type": "flow", "caption": "The form model lives in TypeScript; the template only binds to it",
                    "steps": [("FormGroup", "in the class"), ("[formGroup] / formControlName", "template binding"), ("valid? value?", "read state"), ("onSubmit()", "save")]},
        "syntax": """form = inject(FormBuilder).nonNullable.group({
  name:  ['', [Validators.required, Validators.minLength(3)]],
  email: ['', [Validators.required, Validators.email]],
});

<form [formGroup]="form" (ngSubmit)="submit()">
  <input formControlName="name" />
</form>""",
        "programs": [{
            "file": "reactive-form.component.ts", "kind": "component",
            "actions": [["fill", "#name", "Meena"], ["fill", "#email", "not-an-email"], ["snap", "Invalid email"],
                        ["fill", "#email", "meena@example.com"], ["click", "button[type=submit]"], ["snap", "After submit"]],
            "action_notes": ["Fill in a name and an invalid email.", "Correct the email and click **Save**."],
            "code": r"""import { Component, inject, signal } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [ReactiveFormsModule],
  template: `
    <h3>Student Profile</h3>
    <form [formGroup]="form" (ngSubmit)="submit()">
      <input id="name" formControlName="name" placeholder="Name" />
      @if (form.controls.name.touched && form.controls.name.invalid) { <small>Name needs 3+ letters.</small> }

      <input id="email" formControlName="email" placeholder="Email" />
      @if (form.controls.email.dirty && form.controls.email.invalid) { <small>Enter a valid email.</small> }

      <select formControlName="city">
        <option>Chennai</option>
        <option>Madurai</option>
        <option>Coimbatore</option>
      </select>

      <button type="submit" [disabled]="form.invalid">Save</button>
    </form>

    <p>Form status: {{ form.status }}</p>
    @if (saved()) { <pre>{{ saved() }}</pre> }
  `,
})
export class ReactiveFormComponent {
  private fb = inject(FormBuilder);

  // The form model lives in the class and is fully typed
  form = this.fb.nonNullable.group({
    name: ['', [Validators.required, Validators.minLength(3)]],
    email: ['', [Validators.required, Validators.email]],
    city: ['Chennai'],
  });

  saved = signal('');

  submit() {
    if (this.form.valid) {
      this.saved.set(JSON.stringify(this.form.getRawValue()));
    }
  }
}
""",
        }],
        "tamil": [
            "திருமண அழைப்பிதழை அச்சடிக்கும் முன், மணமக்கள் பெயர், தேதி, மண்டபம் என்று எல்லா அமைப்பையும் முதலிலேயே வடிவமைப்பாளரிடம் "
            "திட்டமிட்டுக் கொடுப்போம்; அச்சகம் அதை அப்படியே பின்பற்றும். அச்சடித்த பின் காகிதத்தில் குழப்பம் வராது.",
            "Reactive form-உம் அப்படியே: படிவத்தின் முழு விதிகளையும் (எந்தக் கட்டம், என்ன சரிபார்ப்பு) TypeScript-இல் முன்கூட்டியே "
            "எழுதிவிடுகிறோம்; HTML அதைப் பின்பற்றுகிறது. பெரிய படிவங்களுக்கும் சோதனை செய்வதற்கும் இது எளிது.",
        ],
        "mistakes": [
            "Forgetting to import `ReactiveFormsModule` (error: Can't bind to 'formGroup').",
            "Using `formControlName` outside an element that has `[formGroup]`.",
            "Reading `form.value` when you need disabled controls too; use `getRawValue()`.",
            "Putting validation logic in the template instead of using validators.",
        ],
        "interview": [
            ("What are reactive forms?", "Forms whose model (FormGroup/FormControl) is created in the component class and bound to the template."),
            ("What is FormBuilder?", "A helper service with shorthand methods (`group`, `control`, `array`) to build form models."),
            ("What is `valueChanges`?", "An Observable that emits whenever a control or group value changes."),
            ("Why choose reactive forms?", "They are explicit, strongly typed, scalable (dynamic fields with FormArray) and easier to unit-test."),
        ],
        "exercises": [
            "Add a `phone` control that accepts exactly 10 digits using `Validators.pattern`.",
            "Show a live preview card using `form.valueChanges` (hint: `toSignal`).",
            "Add a `Reset` button that restores the default values with `form.reset()`.",
        ],
    },
    # ------------------------------------------------------------------ 14
    {
        "slug": "Form_Validation", "title": "Form Validation and Custom Validators", "level": I,
        "summary": "Write your own field validators and cross-field validators such as 'passwords must match'.",
        "definition": [
            "A **validator** is a function that checks a control and returns `null` if the value is fine, or an "
            "**error object** (like `{ spaces: true }`) if it is not. Built-in validators cover common cases; for "
            "everything else you write your own.",
            "A **cross-field validator** is attached to the whole `FormGroup` so it can compare several fields, for "
            "example *password* and *confirm password*. Errors then live on `form.errors` instead of on a single control.",
        ],
        "diagram": {"type": "flow", "caption": "Validators run whenever a value changes; errors are shown from `errors`",
                    "steps": [("value changes", ""), ("validator(control)", "your function"), ("null  /  {error: true}", "result"), ("template", "shows message")]},
        "syntax": """const noSpaces: ValidatorFn = (control) =>
  /\\s/.test(control.value) ? { spaces: true } : null;

new FormGroup({ ... }, { validators: passwordsMatch });   // group-level

form.controls.username.errors?.['spaces']
form.errors?.['mismatch']""",
        "programs": [{
            "file": "signup-validators.component.ts", "kind": "component",
            "actions": [["fill", "#username", "raj kumar"], ["snap", "Space in username"],
                        ["fill", "#username", "rajkumar"], ["fill", "#password", "secret1"], ["fill", "#confirm", "secret2"],
                        ["snap", "Passwords differ"], ["fill", "#confirm", "secret1"], ["snap", "All valid"]],
            "action_notes": ["Type a username containing a space.", "Use a valid username but two different passwords.", "Make the passwords match."],
            "code": r"""import { Component } from '@angular/core';
import { AbstractControl, FormControl, FormGroup, ReactiveFormsModule, ValidationErrors, ValidatorFn, Validators } from '@angular/forms';

// 1. Custom validator for ONE control: returns null (valid) or an error object
const noSpaces: ValidatorFn = (control: AbstractControl): ValidationErrors | null =>
  /\s/.test(control.value) ? { spaces: true } : null;

// 2. Cross-field validator for the WHOLE group
const passwordsMatch: ValidatorFn = (group: AbstractControl): ValidationErrors | null => {
  const password = group.get('password')?.value;
  const confirm = group.get('confirm')?.value;
  return password === confirm ? null : { mismatch: true };
};

@Component({
  selector: 'app-root',
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form">
      <input id="username" formControlName="username" placeholder="Username" />
      @if (form.controls.username.errors?.['spaces']) { <small>No spaces allowed.</small> }

      <input id="password" type="password" formControlName="password" placeholder="Password" />
      @if (form.controls.password.errors?.['minlength']) { <small>Minimum 6 characters.</small> }

      <input id="confirm" type="password" formControlName="confirm" placeholder="Confirm" />
      @if (form.errors?.['mismatch'] && form.controls.confirm.dirty) { <small>Passwords do not match.</small> }
    </form>
    <p>{{ form.valid ? 'Form is valid' : 'Form is invalid' }}</p>
  `,
})
export class SignupValidatorsComponent {
  form = new FormGroup(
    {
      username: new FormControl('', { nonNullable: true, validators: [Validators.required, noSpaces] }),
      password: new FormControl('', { nonNullable: true, validators: [Validators.required, Validators.minLength(6)] }),
      confirm: new FormControl('', { nonNullable: true }),
    },
    { validators: passwordsMatch },
  );
}
""",
        }],
        "tamil": [
            "வங்கியில் புதிய கணக்குத் தொடங்கும்போது, கடவுச்சொல்லை இரண்டு முறை எழுதச் சொல்வார்கள். இரண்டும் ஒன்றாக இல்லையென்றால் "
            "'பொருந்தவில்லை' என்று சொல்லி மீண்டும் எழுதச் சொல்வார்கள். ஒரே கட்டத்தை மட்டும் பார்த்து இதை முடிவு செய்ய முடியாது - "
            "இரண்டு கட்டங்களையும் ஒப்பிட வேண்டும்.",
            "தனிக் கட்டத்துக்கான விதி (இடைவெளி கூடாது) = custom validator. இரண்டு கட்டங்களை ஒப்பிடும் விதி = cross-field "
            "validator; அது முழு `FormGroup`-இல் இணைக்கப்படும்.",
        ],
        "mistakes": [
            "Returning `false` or `true` from a validator; it must return `null` or an error object.",
            "Putting a cross-field validator on one control, where it cannot see the other control.",
            "Showing all errors at once; show the first relevant message per field.",
            "Forgetting that group validators set `form.errors`, not the control's `errors`.",
        ],
        "interview": [
            ("What does a validator function return?", "`null` when valid, otherwise an object describing the error, e.g. `{ spaces: true }`."),
            ("How do you validate two fields together?", "Attach a validator to the parent `FormGroup` that reads both controls."),
            ("What is an async validator?", "A validator returning an Observable/Promise (e.g. check username availability on the server)."),
            ("How do you read errors in the template?", "`control.errors?.['key']` for a control, or `form.errors?.['key']` for a group."),
        ],
        "exercises": [
            "Write a `strongPassword` validator that needs a digit and an uppercase letter.",
            "Add a cross-field validator ensuring `endDate` is after `startDate`.",
            "Create a validator factory `forbiddenWord(word)` that rejects a given word in a comment box.",
        ],
    },
    # ------------------------------------------------------------------ 15
    {
        "slug": "Routing_Basics", "title": "Routing Basics", "level": I,
        "summary": "Navigate between pages with provideRouter, router-outlet and routerLink.",
        "definition": [
            "The **Angular Router** maps URLs to components, so a single-page app can still have many 'pages'. You "
            "define an array of **routes** (`path` + `component`), register it with `provideRouter(routes)`, place a "
            "`<router-outlet />` where the page should appear, and use `routerLink` for navigation without a reload.",
            "A route with `path: '**'` matches everything else and is perfect for a *404 Not Found* page. "
            "`routerLinkActive` adds a CSS class to the link of the page you are currently on.",
        ],
        "diagram": {"type": "flow", "caption": "URL -> matching route -> component rendered in <router-outlet>",
                    "steps": [("/about", "URL"), ("Routes[]", "match path"), ("AboutComponent", "chosen"), ("<router-outlet>", "shows it")]},
        "syntax": """const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent, title: 'About' },
  { path: '**', component: NotFoundComponent },
];

provideRouter(routes)           // in app.config.ts

<a routerLink="/about" routerLinkActive="active">About</a>
<router-outlet />""",
        "programs": [{
            "file": "router-basics.component.ts", "kind": "component",
            "actions": [["snap", "Home page"], ["click", "nav a:nth-of-type(2)"], ["snap", "After clicking About"],
                        ["click", "nav a:nth-of-type(3)"], ["snap", "After clicking a broken link"]],
            "action_notes": ["The app opens on the Home page.", "Click **About**.", "Click **Broken link**."],
            "code": r"""import { ApplicationConfig, Component } from '@angular/core';
import { provideRouter, RouterLink, RouterLinkActive, RouterOutlet, Routes, withHashLocation } from '@angular/router';

// Three simple "pages"
@Component({ selector: 'app-home', template: `<h2>Home</h2><p>Welcome to Koyambedu Bus Stand.</p>` })
export class HomeComponent {}

@Component({ selector: 'app-about', template: `<h2>About</h2><p>We run buses across Tamil Nadu.</p>` })
export class AboutComponent {}

@Component({ selector: 'app-not-found', template: `<h2>404 - Page not found</h2>` })
export class NotFoundComponent {}

// Route table: path -> component. '**' (wildcard) must be LAST.
const routes: Routes = [
  { path: '', component: HomeComponent, title: 'Home' },
  { path: 'about', component: AboutComponent, title: 'About' },
  { path: '**', component: NotFoundComponent },
];

// In a real app this lives in app.config.ts (withHashLocation is only to keep URLs simple here)
export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes, withHashLocation())],
};

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <nav>
      <a routerLink="/" routerLinkActive="active" [routerLinkActiveOptions]="{ exact: true }">Home</a> |
      <a routerLink="/about" routerLinkActive="active">About</a> |
      <a routerLink="/nowhere">Broken link</a>
    </nav>
    <router-outlet />
  `,
  styles: `.active { font-weight: bold; }`,
})
export class AppComponent {}
""",
        }],
        "tamil": [
            "கோயம்பேடு பேருந்து நிலையத்தை நினைத்துப் பாருங்கள். நிலையம் ஒன்றுதான்; ஆனால் 'மதுரை - நடைமேடை 5', 'கோவை - நடைமேடை 8' "
            "என்று ஒவ்வொரு நடைமேடைக்கும் ஒரு எண் உண்டு. அந்த எண்ணுக்குப் போனால் அந்த ஊருக்கான பேருந்து நிற்கும்.",
            "**Router** அந்த அறிவிப்புப் பலகை போல: URL (நடைமேடை எண்) → component (பேருந்து). இல்லாத எண்ணுக்குப் போனால் "
            "'அப்படி ஒரு நடைமேடை இல்லை' என்று காட்டும் - அதுதான் `**` route (404).",
        ],
        "mistakes": [
            "Forgetting `<router-outlet />`; routes match but nothing appears.",
            "Using `href=\"/about\"` instead of `routerLink`, which reloads the entire page.",
            "Placing the `**` wildcard route before other routes (it matches first).",
            "Forgetting to import `RouterLink` / `RouterOutlet` into a standalone component.",
        ],
        "interview": [
            ("What is the Angular Router?", "A library mapping URLs to components, enabling navigation in a single-page app without reloads."),
            ("`routerLink` vs `href`?", "`routerLink` navigates inside the SPA (no reload); `href` makes the browser request the page again."),
            ("What does `path: '**'` do?", "It is the wildcard route that matches any URL not matched earlier, used for a 404 page."),
            ("What is `routerLinkActive`?", "A directive that adds a CSS class to a link when its route is active."),
        ],
        "exercises": [
            "Create Home, Products and Contact pages with a navigation bar.",
            "Add a redirect: `{ path: 'home', redirectTo: '', pathMatch: 'full' }`.",
            "Highlight the active link using `routerLinkActive` and a CSS class.",
        ],
    },
    # ------------------------------------------------------------------ 16
    {
        "slug": "Route_Params_and_Child_Routes", "title": "Route Parameters, Query Params and Child Routes", "level": I,
        "summary": "Pass ids in URLs, read query strings and nest routes inside a layout.",
        "definition": [
            "A **route parameter** is a changing part of the URL, written `:id` in the path (`/courses/2`). **Query "
            "parameters** come after `?` (`/courses/2?tab=syllabus`). With `withComponentInputBinding()` the router "
            "passes both straight into component `input()`s - no `ActivatedRoute` needed.",
            "**Child routes** nest pages inside a parent layout: the parent has its own `<router-outlet />` and "
            "the `children` array decides what appears inside it.",
        ],
        "diagram": {"type": "tree", "label": "AppComponent", "sub": "router-outlet",
                    "children": [{"label": "CoursesLayout", "sub": "/courses  + router-outlet",
                                  "children": [{"label": "CourseList", "sub": "''"}, {"label": "CourseDetail", "sub": ":id"}]}],
                    "caption": "/courses/2?tab=syllabus -> CoursesLayout -> CourseDetail (id=2, tab=syllabus)"},
        "syntax": """{ path: 'courses', component: CoursesLayout, children: [
    { path: '',    component: CourseList },
    { path: ':id', component: CourseDetail },
] }

provideRouter(routes, withComponentInputBinding())

id  = input.required<string>();     // from :id
tab = input('overview');            // from ?tab=...

<a [routerLink]="['/courses', 2]" [queryParams]="{ tab: 'syllabus' }">""",
        "programs": [{
            "file": "courses-router.component.ts", "kind": "component",
            "actions": [["snap", "Course list"], ["click", "app-course-list li:nth-of-type(2) a"], ["snap", "Course detail"]],
            "action_notes": ["The list page opens first.", "Click the second course."],
            "code": r"""import { ApplicationConfig, Component, computed, input } from '@angular/core';
import { provideRouter, RouterLink, RouterOutlet, Routes, withComponentInputBinding, withHashLocation } from '@angular/router';

const COURSES = [
  { id: 1, title: 'Angular Basics' },
  { id: 2, title: 'TypeScript Deep Dive' },
];

// Parent layout: its own <router-outlet> shows the child routes
@Component({
  selector: 'app-courses-layout',
  imports: [RouterOutlet],
  template: `<h2>Courses</h2><router-outlet />`,
})
export class CoursesLayoutComponent {}

@Component({
  selector: 'app-course-list',
  imports: [RouterLink],
  template: `
    <ul>
      @for (c of courses; track c.id) {
        <li><a [routerLink]="[c.id]" [queryParams]="{ tab: 'syllabus' }">{{ c.title }}</a></li>
      }
    </ul>
  `,
})
export class CourseListComponent {
  courses = COURSES;
}

@Component({
  selector: 'app-course-detail',
  imports: [RouterLink],
  template: `
    <h3>Course #{{ id() }}: {{ course()?.title ?? 'Unknown' }}</h3>
    <p>Showing tab: {{ tab() }}</p>
    <a routerLink="/courses">Back to list</a>
  `,
})
export class CourseDetailComponent {
  // Filled from the URL thanks to withComponentInputBinding()
  id = input.required<string>();   // path param  :id
  tab = input('overview');         // query param ?tab=
  course = computed(() => COURSES.find((c) => c.id === Number(this.id())));
}

const routes: Routes = [
  { path: '', redirectTo: 'courses', pathMatch: 'full' },
  {
    path: 'courses',
    component: CoursesLayoutComponent,
    children: [
      { path: '', component: CourseListComponent },
      { path: ':id', component: CourseDetailComponent },
    ],
  },
];

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes, withComponentInputBinding(), withHashLocation())],
};

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  template: `<router-outlet />`,
})
export class AppComponent {}
""",
        }],
        "tamil": [
            "தபால் முகவரியை எடுத்துக்கொள்ளுங்கள்: 'அண்ணா நகர் / 12-ஆம் எண் வீடு'. 'அண்ணா நகர்' என்பது பெற்றோர் (layout) - அந்தப் "
            "பகுதியின் பொதுவான அமைப்பு. '12' என்பது மாறக்கூடிய பகுதி (`:id` parameter) - ஒவ்வொரு வீட்டுக்கும் வேறு எண்.",
            "கடைசியில் 'தபால் பெட்டி எண்: 5, அவசரம்' என்று கூடுதல் குறிப்பு எழுதுவது போல `?tab=syllabus` என்பது query parameter. "
            "முகவரி மாறினாலும் தபால்காரர் (router) சரியான வீட்டைக் கண்டுபிடிப்பார்.",
        ],
        "mistakes": [
            "Forgetting `withComponentInputBinding()`; inputs stay empty.",
            "Giving the parent route a component without a `<router-outlet />`; children never show.",
            "Reading `id` as a number; route params are always strings (convert with `Number()`).",
            "Using absolute links inside children by accident, or relative links from the wrong route.",
        ],
        "interview": [
            ("Route params vs query params?", "Route params are part of the path (`/courses/2`, required for matching); query params follow `?` (optional, e.g. filters)."),
            ("How do you read a route parameter?", "Via `input()` with `withComponentInputBinding()`, or `ActivatedRoute.paramMap` / `snapshot`."),
            ("What are child routes?", "Routes nested under a parent route; the parent's `<router-outlet />` displays them."),
            ("What does `pathMatch: 'full'` mean?", "The whole remaining URL must match the path, important for `''` redirects."),
        ],
        "exercises": [
            "Add a `/products/:id` route and show the product's name and price from an array.",
            "Add a `?sort=price` query parameter that sorts the course list.",
            "Create a `/admin` layout with child routes `users` and `settings`.",
        ],
    },
    # ------------------------------------------------------------------ 17
    {
        "slug": "Guards_and_Lazy_Loading", "title": "Route Guards and Lazy Loading", "level": I,
        "summary": "Protect pages with functional guards and load code only when a route is visited.",
        "definition": [
            "A **route guard** is a function that decides whether a navigation is allowed. `canActivate` runs before a "
            "route is entered; it returns `true` to allow, `false` to block, or a `UrlTree` to **redirect** (for "
            "example to a login page). Guards are plain functions that can use `inject()`.",
            "**Lazy loading** means the code of a page is downloaded only when the user first visits it, using "
            "`loadComponent` (or `loadChildren`). This makes the first load smaller and faster.",
        ],
        "diagram": {"type": "flow", "caption": "Navigation passes through the guard; the lazy chunk downloads only after approval",
                    "steps": [("click /admin", ""), ("canActivate", "guard"), ("logged in?", "yes"), ("download admin chunk", "lazy"), ("show page", "")]},
        "syntax": """export const authGuard: CanActivateFn = () => {
  const ok = inject(AuthService).loggedIn();
  return ok ? true : inject(Router).createUrlTree(['/login']);
};

{ path: 'admin',
  canActivate: [authGuard],
  loadComponent: () => import('./admin.component').then(m => m.AdminComponent) }""",
        "programs": [
            {"file": "guarded-app.component.ts", "kind": "component",
             "actions": [["click", "nav a:nth-of-type(2)"], ["snap", "Admin link while logged out (redirected)"],
                         ["click", "#login"], ["snap", "After logging in"]],
             "action_notes": ["Click **Admin** while logged out - the guard redirects to Login.", "Click **Log in** - you are taken to the lazy loaded Admin page."],
             "code": r"""import { ApplicationConfig, Component, inject, Injectable, signal } from '@angular/core';
import { CanActivateFn, provideRouter, Router, RouterLink, RouterOutlet, Routes, withHashLocation } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class AuthService {
  loggedIn = signal(false);
}

// Functional guard: true = allow, UrlTree = redirect
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);
  return auth.loggedIn() ? true : router.createUrlTree(['/login']);
};

@Component({ selector: 'app-home', template: `<h2>Home</h2><p>Public page.</p>` })
export class HomeComponent {}

@Component({
  selector: 'app-login',
  template: `
    <h2>Login required</h2>
    <button id="login" (click)="login()">Log in</button>
  `,
})
export class LoginComponent {
  private auth = inject(AuthService);
  private router = inject(Router);

  login() {
    this.auth.loggedIn.set(true);
    this.router.navigate(['/admin']);
  }
}

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  {
    path: 'admin',
    canActivate: [authGuard],
    // Lazy loaded: admin.component.ts becomes a separate JavaScript chunk
    loadComponent: () => import('./admin.component').then((m) => m.AdminComponent),
  },
];

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes, withHashLocation())],
};

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink],
  template: `
    <nav>
      <a routerLink="/">Home</a> |
      <a routerLink="/admin">Admin</a>
    </nav>
    <router-outlet />
  `,
})
export class AppComponent {}
"""},
            {"file": "admin.component.ts", "kind": "support",
             "code": r"""import { Component } from '@angular/core';

// This file is loaded lazily by guarded-app.component.ts
@Component({
  selector: 'app-admin',
  template: `
    <h2>Admin Panel</h2>
    <p>This page was lazy loaded after the guard allowed you in.</p>
  `,
})
export class AdminComponent {}
"""},
        ],
        "tamil": [
            "கோயிலில் சிறப்பு தரிசனத்துக்குச் செல்லும்போது வாசலில் உள்ள ஊழியர் உங்கள் டிக்கெட்டைப் பார்ப்பார். டிக்கெட் இருந்தால் "
            "உள்ளே அனுமதி; இல்லையென்றால் 'டிக்கெட் கவுண்டருக்குப் போங்கள்' என்று திருப்பி அனுப்புவார். அவர்தான் **route guard**; "
            "கவுண்டருக்கு அனுப்புவது = `UrlTree` redirect.",
            "ஒவ்வொரு சன்னதிக்கும் உரிய பிரசாதம் அந்தச் சன்னதிக்கு பக்தர் வந்த பிறகே தயாரிக்கப்பட்டால், சமையல்கூடம் "
            "வீணாகாது. அதுபோல **lazy loading** - பயனர் அந்தப் பக்கத்துக்குப் போனால் மட்டுமே அதன் code பதிவிறக்கம் ஆகும்.",
        ],
        "mistakes": [
            "Returning `false` from a guard without redirecting, leaving the user on a blank screen.",
            "Relying on guards for security. They only hide UI; the server must still check permissions.",
            "Using eager `component:` for big rarely-used pages instead of `loadComponent`.",
            "Calling `inject()` outside the guard's synchronous body (for example after `await`).",
        ],
        "interview": [
            ("What is a route guard?", "A function that controls navigation: `canActivate`, `canDeactivate`, `canMatch`, `resolve` etc."),
            ("How do you redirect from a guard?", "Return a `UrlTree` created with `router.createUrlTree([...])`."),
            ("What is lazy loading?", "Loading route code on demand through dynamic `import()`, reducing the initial bundle size."),
            ("`canActivate` vs `canMatch`?", "`canActivate` runs after the route matches; `canMatch` decides whether the route can match at all (and so whether lazy code is loaded)."),
        ],
        "exercises": [
            "Add a `canDeactivate` guard that asks for confirmation when leaving a form with unsaved changes.",
            "Make a `roleGuard` that allows only users whose role is 'admin'.",
            "Lazy load a `Reports` page and open the browser Network tab to see the extra chunk download.",
        ],
    },
    # ------------------------------------------------------------------ 18
    {
        "slug": "HttpClient_and_APIs", "title": "HttpClient and Working with APIs", "level": I,
        "summary": "Call REST APIs with HttpClient, handle loading and error states.",
        "definition": [
            "**HttpClient** is Angular's service for talking to servers over HTTP (REST APIs). Enable it with "
            "`provideHttpClient()`, inject it, and call `get`, `post`, `put`, `delete`. Each call returns an "
            "**Observable**: nothing is sent until you `subscribe`.",
            "Real apps always handle three states: **loading** (waiting), **success** (data arrived) and **error** "
            "(network or server failure). Put API calls in a **service**, and give request/response data a TypeScript "
            "interface.",
        ],
        "diagram": {"type": "flow", "caption": "Request goes out; the response (or error) comes back later",
                    "steps": [("Component", "load()"), ("Service", "http.get<Todo[]>"), ("Server / API", "JSON"), ("Observable", "next / error"), ("signal", "template updates")]},
        "syntax": """provideHttpClient()                       // app.config.ts

private http = inject(HttpClient);
this.http.get<Todo[]>(url).subscribe({
  next:  (data) => ...,
  error: (err)  => ...,
});
this.http.post<Todo>(url, body)""",
        "programs": [{
            "file": "todo-api.component.ts", "kind": "component", "expect_http_errors": True,
            "mocks": {
                "/todos/add": {"id": 3, "title": "Buy jasmine flowers", "done": False},
                "/broken": {"__status": 500, "body": {"message": "Server error"}},
                "/todos": [{"id": 1, "title": "Learn Angular", "done": True},
                           {"id": 2, "title": "Practice HttpClient", "done": False}],
            },
            "actions": [["click", "#load"], ["click", "#add"], ["snap", "After load + add"], ["click", "#broken"], ["snap", "After a failing request"]],
            "action_notes": ["Click **Load todos**, then **Add todo**.", "Click **Call broken URL** to see error handling."],
            "code": r"""import { HttpClient, provideHttpClient } from '@angular/common/http';
import { ApplicationConfig, Component, inject, Injectable, signal } from '@angular/core';

export const appConfig: ApplicationConfig = {
  providers: [provideHttpClient()], // enables HttpClient
};

interface Todo {
  id: number;
  title: string;
  done: boolean;
}

// All API calls live in a service
@Injectable({ providedIn: 'root' })
export class TodoApi {
  private http = inject(HttpClient);
  private base = 'https://api.example.com'; // replace with your real API

  list() {
    return this.http.get<Todo[]>(`${this.base}/todos`);
  }
  add(title: string) {
    return this.http.post<Todo>(`${this.base}/todos/add`, { title });
  }
  broken() {
    return this.http.get<Todo[]>(`${this.base}/broken`);
  }
}

@Component({
  selector: 'app-root',
  template: `
    <button id="load" (click)="load()">Load todos</button>
    <button id="add" (click)="add()">Add todo</button>
    <button id="broken" (click)="callBroken()">Call broken URL</button>

    @if (loading()) { <p>Loading...</p> }
    @if (error()) { <p>Error: {{ error() }}</p> }

    <ul>
      @for (t of todos(); track t.id) {
        <li>{{ t.done ? '[x]' : '[ ]' }} {{ t.title }}</li>
      }
    </ul>
  `,
})
export class TodoApiComponent {
  private api = inject(TodoApi);
  todos = signal<Todo[]>([]);
  loading = signal(false);
  error = signal('');

  load() {
    this.loading.set(true);
    this.error.set('');
    this.api.list().subscribe({
      next: (data) => {
        this.todos.set(data);
        this.loading.set(false);
      },
      error: () => {
        this.error.set('Could not load todos');
        this.loading.set(false);
      },
    });
  }

  add() {
    this.api.add('Buy jasmine flowers').subscribe((todo) => this.todos.update((list) => [...list, todo]));
  }

  callBroken() {
    this.error.set('');
    this.api.broken().subscribe({ error: () => this.error.set('Server returned an error (500)') });
  }
}
""",
        }],
        "tamil": [
            "நீங்கள் ஒரு உணவகத்தில் அமர்ந்து சர்வரிடம் 'ஒரு மசாலா தோசை' என்று ஆர்டர் கொடுக்கிறீர்கள் - இது **request**. சமையலறை "
            "(server) தோசை தயாரித்து அனுப்புகிறது - இது **response**. இது உடனே நடக்காது; நேரம் ஆகும் (asynchronous).",
            "காத்திருக்கும்போது 'தயாராகிக்கொண்டிருக்கிறது...' (loading). தோசை தயாராகிவிட்டால் தட்டில் வரும் (success). 'மாவு "
            "தீர்ந்துவிட்டது' என்றால் (error) நமக்குத் தெரிவிக்க வேண்டும். `HttpClient` இந்த சர்வர் வேலையைச் செய்கிறது.",
        ],
        "mistakes": [
            "Not subscribing (or not using `async` pipe / `toSignal`); an HTTP Observable does nothing until subscribed.",
            "Ignoring errors; always handle the `error` callback and show a message.",
            "Forgetting `provideHttpClient()` (error: No provider for HttpClient).",
            "Calling the API directly from many components instead of in a shared service.",
        ],
        "interview": [
            ("What is HttpClient?", "Angular's injectable service for HTTP requests, returning typed Observables."),
            ("Why must you subscribe to an HTTP call?", "Observables are lazy; the request is sent only on subscription."),
            ("How do you handle errors?", "Use the `error` callback in `subscribe`, or the RxJS `catchError` operator in the pipe."),
            ("How do you send headers or query params?", "Pass an options object: `http.get(url, { headers, params })`."),
        ],
        "exercises": [
            "Add a `delete(id)` method and a delete button for each todo.",
            "Show a spinner text while loading using `loading()`.",
            "Use `catchError` + `of([])` inside the service so the component never crashes on error.",
        ],
    },
    # ------------------------------------------------------------------ 19
    {
        "slug": "RxJS_Fundamentals", "title": "RxJS Fundamentals", "level": I,
        "summary": "Observables, subscribe, pipe, map/filter and the async pipe.",
        "definition": [
            "**RxJS** is a library for working with **streams of values over time**. An **Observable** describes a "
            "stream; nothing happens until you **subscribe**. **Operators** (`map`, `filter`, `take`...) are chained "
            "inside `pipe()` to transform the stream.",
            "In templates, the `async` pipe subscribes for you and unsubscribes automatically, so you avoid memory "
            "leaks. A **Subject** is an Observable you can push values into manually (useful for events).",
        ],
        "diagram": {"type": "flow", "caption": "Values flow through operators to the subscriber",
                    "steps": [("Source", "of(1..6)"), ("filter", "even only"), ("map", "x 10"), ("subscribe", "20, 40, 60")]},
        "syntax": """source$.pipe(
  filter(n => n % 2 === 0),
  map(n => n * 10),
).subscribe(value => console.log(value));

{{ source$ | async }}      // template: auto subscribe/unsubscribe""",
        "programs": [
            {"file": "rxjs-basics.ts", "kind": "script",
             "code": r"""// Run with: npx tsx rxjs-basics.ts
import { filter, interval, lastValueFrom, map, Observable, of, Subject, take, tap } from 'rxjs';

async function main() {
  // 1. Creation + operators in pipe()
  of(1, 2, 3, 4, 5, 6)
    .pipe(
      filter((n) => n % 2 === 0), // keep even numbers
      map((n) => n * 10), // multiply by 10
    )
    .subscribe((v) => console.log('even x10:', v));

  // 2. Build your own Observable (note the cleanup function)
  const greeting$ = new Observable<string>((subscriber) => {
    subscriber.next('Hello');
    subscriber.next('Angular');
    subscriber.complete();
    return () => console.log('cleanup done');
  });
  greeting$.subscribe({
    next: (v) => console.log('got:', v),
    complete: () => console.log('stream completed'),
  });

  // 3. Subject: push values manually; every subscriber receives them
  const bell$ = new Subject<string>();
  bell$.subscribe((m) => console.log('Student A heard:', m));
  bell$.subscribe((m) => console.log('Student B heard:', m));
  bell$.next('Class over!');

  // 4. Timed stream: 3 ticks, 50 ms apart, then it completes
  const last = await lastValueFrom(
    interval(50).pipe(
      take(3),
      map((i) => i + 1),
      tap((n) => console.log('tick', n)),
    ),
  );
  console.log('last tick was', last);
}

main();
"""},
            {"file": "ticker.component.ts", "kind": "component",
             "actions": [["wait", 900]],
             "action_notes": ["Wait about one second while the ticker runs."],
             "code": r"""import { AsyncPipe } from '@angular/common';
import { Component } from '@angular/core';
import { interval, map, take } from 'rxjs';

@Component({
  selector: 'app-root',
  imports: [AsyncPipe],
  // The async pipe subscribes and unsubscribes automatically
  template: `<p>{{ ticks$ | async }}</p>`,
})
export class TickerComponent {
  // emits 'Tick 1' ... 'Tick 5', one every 100 ms, then completes
  ticks$ = interval(100).pipe(
    take(5),
    map((i) => `Tick ${i + 1}`),
  );
}
"""},
        ],
        "tamil": [
            "சன் டிவி நேரலை ஒளிபரப்பு எப்போதும் ஓடிக்கொண்டே இருக்கிறது. நீங்கள் டிவியை ஆன் செய்தால்தான் (**subscribe**) அதைப் பார்க்க முடியும்; "
            "ஆஃப் செய்தால் (**unsubscribe**) உங்களுக்கு வருவது நின்றுவிடும். ஒளிபரப்பு = **Observable**.",
            "விளம்பர இடைவேளையை நீக்கிப் பார்க்க விரும்பினால் அது `filter`; ஒவ்வொரு காட்சியையும் தமிழில் மாற்றிப் பார்த்தால் அது `map`. "
            "இவை எல்லாம் ஒளிபரப்பு வரும் வழியிலேயே (`pipe`) நடக்கும்.",
        ],
        "mistakes": [
            "Forgetting to `subscribe`; nothing runs.",
            "Subscribing manually in components and never unsubscribing (memory leaks). Prefer `async` pipe, `toSignal` or `takeUntilDestroyed`.",
            "Nesting `subscribe` inside `subscribe`; use `switchMap` and friends instead.",
            "Confusing `of(1,2,3)` (three emissions) with `of([1,2,3])` (one array emission).",
        ],
        "interview": [
            ("What is an Observable?", "A lazy stream of zero or more values over time that a consumer can subscribe to."),
            ("Observable vs Promise?", "A Promise gives one value, is eager and cannot be cancelled; an Observable can emit many values, is lazy and cancellable."),
            ("What is a Subject?", "An Observable that is also an Observer: you call `next()` on it to multicast values to all subscribers."),
            ("What does the async pipe do?", "Subscribes to an Observable in the template, displays the latest value and unsubscribes on destroy."),
            ("What is an operator?", "A function used in `pipe()` that transforms, filters or combines streams, e.g. `map`, `filter`, `take`."),
        ],
        "exercises": [
            "Use `interval(1000)` with `take(10)` to build a countdown that prints 10 to 1.",
            "From `of(1..20)` keep numbers divisible by 3 and square them.",
            "Create a `Subject<string>` chat service and subscribe from two components.",
        ],
    },
    # ------------------------------------------------------------------ 20
    {
        "slug": "Lifecycle_Hooks", "title": "Component Lifecycle Hooks", "level": I,
        "summary": "Run code at the right moment: ngOnChanges, ngOnInit, ngAfterViewInit and ngOnDestroy.",
        "definition": [
            "Every component has a **life**: Angular creates it, updates it and finally destroys it. **Lifecycle hooks** "
            "are methods Angular calls at these moments. The most important are: `ngOnChanges` (an input changed), "
            "`ngOnInit` (ready - good place for setup), `ngAfterViewInit` (the view exists) and `ngOnDestroy` (cleanup).",
            "Use `constructor` only for injecting dependencies. Do initial work in `ngOnInit`, and release timers, "
            "event listeners and subscriptions in `ngOnDestroy` to avoid memory leaks.",
        ],
        "diagram": {"type": "flow", "caption": "Order of the most used hooks",
                    "steps": [("constructor", ""), ("ngOnChanges", "inputs set"), ("ngOnInit", "setup"), ("ngAfterViewInit", "view ready"), ("ngOnDestroy", "cleanup")]},
        "syntax": """export class MyComponent implements OnInit, OnDestroy {
  ngOnInit()    { /* load data, start timers */ }
  ngOnDestroy() { /* unsubscribe, clear timers */ }
}""",
        "programs": [{
            "file": "lifecycle-logger.component.ts", "kind": "component",
            "actions": [["click", "#rename"], ["click", "#toggle"]],
            "action_notes": ["Click **Rename tea**.", "Click **Remove card** to destroy the child."],
            "code": r"""import { AfterViewInit, Component, inject, Injectable, input, OnChanges, OnDestroy, OnInit, signal, SimpleChanges } from '@angular/core';

// A tiny service so we can SEE the order of the hooks on screen
@Injectable({ providedIn: 'root' })
export class LogService {
  logs = signal<string[]>([]);
  add(message: string) {
    this.logs.update((l) => [...l, message]);
  }
}

@Component({
  selector: 'app-tea-card',
  template: `<p>Tea: {{ name() }}</p>`,
})
export class TeaCardComponent implements OnChanges, OnInit, AfterViewInit, OnDestroy {
  name = input.required<string>();
  private log = inject(LogService);

  constructor() {
    this.log.add('constructor');
  }
  ngOnChanges(changes: SimpleChanges) {
    this.log.add(`ngOnChanges -> ${changes['name'].currentValue}`);
  }
  ngOnInit() {
    this.log.add('ngOnInit');
  }
  ngAfterViewInit() {
    this.log.add('ngAfterViewInit');
  }
  ngOnDestroy() {
    this.log.add('ngOnDestroy');
  }
}

@Component({
  selector: 'app-root',
  imports: [TeaCardComponent],
  template: `
    <button id="rename" (click)="tea.set('Ginger Tea')">Rename tea</button>
    <button id="toggle" (click)="show.set(!show())">{{ show() ? 'Remove' : 'Show' }} card</button>

    @if (show()) { <app-tea-card [name]="tea()" /> }

    <h4>Hook log</h4>
    <ol>
      @for (l of logger.logs(); track $index) { <li>{{ l }}</li> }
    </ol>
  `,
})
export class LifecycleLoggerComponent {
  logger = inject(LogService);
  show = signal(true);
  tea = signal('Masala Tea');
}
""",
        }],
        "tamil": [
            "ஒரு தேநீர்க் கடையின் நாளை நினைத்துப் பாருங்கள். காலையில் கடையைத் திறப்பது (`ngOnInit`) - அடுப்பு பற்றவைத்து, பால் "
            "வாங்கி வைப்பது. நாள் முழுவதும் விலை மாறினால் பலகையைப் புதுப்பிப்பது (`ngOnChanges`).",
            "இரவு கடையை மூடும்போது (`ngOnDestroy`) அடுப்பை அணைத்து, பாத்திரங்களைக் கழுவி, விளக்கை அணைக்க வேண்டும். இதைச் செய்யாவிட்டால் "
            "(unsubscribe, timer நிறுத்துதல்) மறுநாள் பிரச்சனை - அதுதான் memory leak.",
        ],
        "mistakes": [
            "Doing heavy work (like HTTP calls) in the constructor instead of `ngOnInit`.",
            "Forgetting to clean up intervals/subscriptions in `ngOnDestroy`.",
            "Accessing a child view in `ngOnInit`; it is only ready in `ngAfterViewInit`.",
            "Modifying state in `ngAfterViewInit` without care, leading to ExpressionChanged errors.",
        ],
        "interview": [
            ("Name the common lifecycle hooks in order.", "constructor, ngOnChanges, ngOnInit, ngDoCheck, ngAfterContentInit, ngAfterViewInit, ngOnDestroy."),
            ("Constructor vs ngOnInit?", "The constructor only creates the object and injects dependencies; `ngOnInit` runs after inputs are set and is where setup belongs."),
            ("When does ngOnChanges run?", "Before `ngOnInit` and whenever an input value changes."),
            ("How do you avoid memory leaks?", "Clean up in `ngOnDestroy`, use `async` pipe, `takeUntilDestroyed` or `DestroyRef.onDestroy`."),
        ],
        "exercises": [
            "Start a `setInterval` clock in `ngOnInit` and stop it in `ngOnDestroy`.",
            "Add `ngDoCheck` to the logger and observe how often it runs.",
            "Use `DestroyRef` (`inject(DestroyRef).onDestroy(...)`) instead of `ngOnDestroy`.",
        ],
    },
    # ------------------------------------------------------------------ 21
    {
        "slug": "Content_Projection_and_ViewChild", "title": "Content Projection and ViewChild", "level": I,
        "summary": "Build flexible wrapper components with ng-content and access elements with viewChild.",
        "definition": [
            "**Content projection** lets a component accept HTML from its parent and place it in 'slots', using "
            "`<ng-content>`. It is how you build reusable wrappers such as cards, dialogs and tabs. Use the `select` "
            "attribute to create several named slots.",
            "**viewChild()** gives a component a reference to an element or child component in its own template "
            "(marked with a template variable like `#box`). It is a signal, available once the view has rendered.",
        ],
        "diagram": {"type": "layers", "caption": "The parent's HTML is projected into the slots of <app-card>",
                    "layers": [("<app-card>", "wrapper component"), ("slot [card-title]", "-> <h3 card-title>Masala Dosa</h3>"),
                               ("slot (default)", "-> <p>Crispy dosa...</p>"), ("slot [card-footer]", "-> <small card-footer>₹60</small>")]},
        "syntax": """<!-- card.component template -->
<ng-content select="[card-title]" />
<ng-content />                       <!-- default slot -->

<!-- using it -->
<app-card><h3 card-title>Hi</h3> body text</app-card>

box = viewChild.required<ElementRef<HTMLInputElement>>('box');   // <input #box>""",
        "programs": [{
            "file": "card-projection.component.ts", "kind": "component",
            "actions": [["click", "#focus"]],
            "action_notes": ["Click **Focus the box**."],
            "code": r"""import { Component, ElementRef, signal, viewChild } from '@angular/core';

// A reusable wrapper with three slots
@Component({
  selector: 'app-card',
  template: `
    <div class="card">
      <header><ng-content select="[card-title]" /></header>
      <section><ng-content /></section>
      <footer><ng-content select="[card-footer]" /></footer>
    </div>
  `,
  styles: `.card { border: 1px solid #aaa; padding: 8px; border-radius: 6px; }`,
})
export class CardComponent {}

@Component({
  selector: 'app-root',
  imports: [CardComponent],
  template: `
    <app-card>
      <h3 card-title>Masala Dosa</h3>
      <p>Crispy dosa with potato filling.</p>
      <small card-footer>Price: ₹60</small>
    </app-card>

    <!-- #nameInput is a template reference variable used by viewChild -->
    <input #nameInput placeholder="Your name" />
    <button id="focus" (click)="focusInput()">Focus the box</button>
    <p>{{ status() }}</p>
  `,
})
export class AppComponent {
  nameInput = viewChild.required<ElementRef<HTMLInputElement>>('nameInput');
  status = signal('Not focused yet');

  focusInput() {
    const el = this.nameInput().nativeElement;
    el.focus();
    this.status.set(`Input focused: ${document.activeElement === el}`);
  }
}
""",
        }],
        "tamil": [
            "கடையில் ஒரு காலிப் பரிசுப் பெட்டி வாங்குகிறீர்கள். பெட்டியின் வடிவம், மூடி, ரிப்பன் எல்லாம் கடைக்காரர் தருகிறார்; உள்ளே என்ன "
            "வைக்க வேண்டும் என்பது உங்கள் விருப்பம் - இனிப்போ, துணியோ, புத்தகமோ.",
            "`<app-card>` அந்தப் பெட்டி; `<ng-content>` உள்ளே வைக்கும் இடங்கள் (மேலே தலைப்பு, நடுவில் பொருள், கீழே விலை). `viewChild` என்பது "
            "பெட்டிக்குள் இருக்கும் ஒரு குறிப்பிட்ட பொருளைத் தொட்டு எடுப்பது போல.",
        ],
        "mistakes": [
            "Reading `viewChild()` in the constructor or `ngOnInit`; it is only available after the view is created.",
            "Expecting `<ng-content>` to render conditionally; projected content is always created by the parent.",
            "Using `document.getElementById` instead of `viewChild`.",
            "Forgetting the `select` attribute so everything lands in the default slot.",
        ],
        "interview": [
            ("What is content projection?", "Passing template content from a parent into a child component's `<ng-content>` slots."),
            ("What is `viewChild`?", "A query that returns a child element/component from the component's own template."),
            ("`viewChild` vs `contentChild`?", "`viewChild` queries the component's own template; `contentChild` queries projected content passed in by the parent."),
            ("What is a template reference variable?", "A `#name` marker in the template giving access to an element or directive instance."),
        ],
        "exercises": [
            "Build a `tabs` wrapper that projects two panels.",
            "Create a modal wrapper with `header`, `body` and `footer` slots.",
            "Use `viewChild` to scroll a `div` to the top when a button is clicked.",
        ],
    },
    # ------------------------------------------------------------------ 22
    {
        "slug": "Custom_Directives", "title": "Custom Directives", "level": I,
        "summary": "Create your own attribute directives with inputs, outputs and host bindings.",
        "definition": [
            "A **custom directive** adds reusable behaviour to any existing element, without a template of its own. "
            "You create one with `@Directive` and a CSS-attribute **selector** such as `[appHighlight]`.",
            "The `host` property connects the directive to the element it sits on: `'(mouseenter)'` listens to events and "
            "`'[style.color]'` binds styles. Directives can also have `input()`s and `output()`s like components.",
        ],
        "diagram": {"type": "flow", "caption": "The directive attaches behaviour to a normal element",
                    "steps": [("<li appHighlight>", "plain element"), ("HighlightDirective", "listens + styles"), ("mouse enters", "event"), ("background changes", "result")]},
        "syntax": """@Directive({
  selector: '[appHighlight]',
  host: { '(mouseenter)': 'onEnter()', '[style.background-color]': 'color()' },
})
export class HighlightDirective {
  color = input('yellow', { alias: 'appHighlight' });
}

<li appHighlight="lightgreen">Idli</li>""",
        "programs": [{
            "file": "highlight.directive.ts", "kind": "component",
            "actions": [["hover", "li:nth-of-type(2)"]],
            "action_notes": ["Move the mouse over **Filter Coffee**."],
            "code": r"""import { Component, Directive, input, output, signal } from '@angular/core';

// An attribute directive: adds hover highlighting to ANY element
@Directive({
  selector: '[appHighlight]',
  host: {
    '(mouseenter)': 'enter()',
    '(mouseleave)': 'leave()',
    // style binding on the host element
    '[style.background-color]': 'active() ? color() : null',
  },
})
export class HighlightDirective {
  color = input('yellow', { alias: 'appHighlight' }); // <li appHighlight="lightgreen">
  hoverChange = output<boolean>();                     // tell the parent about hover
  active = signal(false);

  enter() {
    this.active.set(true);
    this.hoverChange.emit(true);
  }
  leave() {
    this.active.set(false);
    this.hoverChange.emit(false);
  }
}

@Component({
  selector: 'app-root',
  imports: [HighlightDirective],
  template: `
    <ul>
      @for (item of items; track item) {
        <li appHighlight="lightgreen" (hoverChange)="onHover(item, $event)">{{ item }}</li>
      }
    </ul>
    <p>Hovered: {{ hovered() || 'nothing' }}</p>
  `,
})
export class AppComponent {
  items = ['Idli', 'Filter Coffee', 'Vada'];
  hovered = signal('');

  onHover(item: string, isOver: boolean) {
    this.hovered.set(isOver ? item : '');
  }
}
""",
        }],
        "tamil": [
            "பள்ளியில் ஆசிரியர் ஒரு மஞ்சள் மார்க்கர் (highlighter) பேனாவை வைத்திருக்கிறார். எந்தப் புத்தகத்தின் எந்த வரியிலும் அதைப் "
            "பயன்படுத்தி முக்கியமான இடத்தை அடையாளம் காட்டலாம். வரியின் உள்ளடக்கம் மாறுவதில்லை; அதன் தோற்றம் மட்டும் மாறுகிறது.",
            "**Custom directive** அந்த மார்க்கர் பேனா: `appHighlight` என்று எந்த element மீதும் எழுதிவிட்டால் போதும், அதில் "
            "மவுஸ் வந்தால் நிறம் மாறும். ஒரு முறை எழுதி எங்கும் மறுபடி பயன்படுத்தலாம்.",
        ],
        "mistakes": [
            "Using a selector without brackets (`appHighlight` instead of `[appHighlight]`) so it matches an element name.",
            "Not prefixing the selector (use `app` or your own prefix) and clashing with HTML attributes.",
            "Manipulating `nativeElement.style` directly when a host binding would do.",
            "Forgetting to import the directive in the component that uses it.",
        ],
        "interview": [
            ("What is a directive?", "A class that adds behaviour to elements. Types: components, structural and attribute directives."),
            ("How is an attribute directive created?", "With `@Directive({ selector: '[name]' })`, using `host` bindings/listeners or `inject(ElementRef)`."),
            ("What does `host` do?", "It binds properties, attributes, styles and events on the element that hosts the directive."),
            ("Directive vs component?", "A component is a directive with a template; a directive has no template."),
        ],
        "exercises": [
            "Create `appAutoFocus` which focuses its element when the page loads.",
            "Write `appUppercase` that converts typed text in an input to capital letters.",
            "Build `appTooltip=\"text\"` that shows the text as the element's `title` attribute.",
        ],
    },
]
