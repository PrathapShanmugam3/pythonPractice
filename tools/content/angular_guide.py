"""Angular combined guide: detailed Beginner/Intermediate topics + condensed Advanced/Master topics."""
from ._dsl import apply_extras, topics
from .angular_extras import EXTRAS
from . import angular as _angular  # applies extras to the detailed topics
from .angular_beginner import TOPICS as B
from .angular_intermediate import TOPICS as I

EXTRA = topics([
    ("A", "HTTP Interceptors and Error Handling",
     "An **interceptor** is a function that sees every HTTP request/response. Use it to add auth tokens, log, show a global loader or handle errors in one place. Register with `provideHttpClient(withInterceptors([...]))`.",
     """export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthService).token();
  return next(token ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } }) : req);
};
provideHttpClient(withInterceptors([authInterceptor]))"""),
    ("A", "Advanced RxJS Operators",
     "Flatten inner Observables with `switchMap` (cancel old), `mergeMap` (parallel), `concatMap` (queue), `exhaustMap` (ignore new). Combine streams with `combineLatest` / `forkJoin`; tame events with `debounceTime` and `distinctUntilChanged`; recover with `catchError` / `retry`.",
     """search.valueChanges.pipe(
  debounceTime(300), distinctUntilChanged(),
  switchMap(term => api.search(term).pipe(catchError(() => of([]))))
)"""),
    ("A", "State Management (Signals, Services, NgRx)",
     "Start simple: a service holding `signal`s, exposing read-only signals and update methods (a *store*). When many features share complex state, use **NgRx** (actions, reducers, selectors, effects) or **NgRx SignalStore** for predictable, debuggable state.",
     """@Injectable({ providedIn: 'root' })
export class TodoStore {
  private _todos = signal<Todo[]>([]);
  readonly todos = this._todos.asReadonly();
  readonly doneCount = computed(() => this._todos().filter(t => t.done).length);
  add(t: Todo) { this._todos.update(l => [...l, t]); }
}"""),
    ("A", "Change Detection and OnPush",
     "Change detection decides when to refresh templates. `ChangeDetectionStrategy.OnPush` re-checks a component only when an input reference changes, an event fires inside it, an async pipe/signal it reads updates, or you call `markForCheck()`. Combine OnPush + signals + immutable data for speed.",
     """@Component({ changeDetection: ChangeDetectionStrategy.OnPush, ... })
export class RowComponent { row = input.required<Row>(); }"""),
    ("A", "Advanced Dependency Injection",
     "Use `InjectionToken` for non-class values (config, API URL), `useClass` / `useValue` / `useFactory` providers to swap implementations, and component-level `providers` to get one instance per component. Injectors form a hierarchy: element -> environment -> root.",
     """export const API_URL = new InjectionToken<string>('API_URL');
providers: [{ provide: API_URL, useValue: 'https://api.example.com' }]
const url = inject(API_URL);"""),
    ("A", "Deferrable Views and Performance",
     "`@defer` lazy-loads part of a template (on viewport, idle, interaction, timer) with `@placeholder`, `@loading`, `@error` blocks. Other wins: `@for` with `track`, OnPush, lazy routes, `NgOptimizedImage`, pure pipes and bundle analysis.",
     """@defer (on viewport) { <app-heavy-chart /> }
@placeholder { <p>Chart loads when visible</p> }
@loading { <p>Loading...</p> }"""),
    ("A", "Testing Angular Apps",
     "Unit-test services as plain classes, test components with `TestBed` and `ComponentFixture`, mock HTTP with `provideHttpClientTesting`, and run end-to-end tests with Playwright or Cypress. Angular 21 uses Vitest by default for new projects.",
     """it('adds numbers', () => {
  const calc = new CalculatorService();
  expect(calc.add(2, 3)).toBe(5);
});"""),
    ("A", "SSR, Hydration and SEO",
     "**Server-Side Rendering** renders HTML on the server for faster first paint and SEO; **hydration** reuses that HTML in the browser instead of rebuilding it. Add with `ng add @angular/ssr`. Guard browser-only APIs with `isPlatformBrowser` or `afterNextRender`.",
     "ng add @angular/ssr\nprovideClientHydration(withEventReplay())"),
    ("A", "Animations and UI Libraries",
     "Use CSS transitions with `animate.enter` / `animate.leave` for enter-leave effects (the older `@angular/animations` package is deprecated). **Angular Material** and **CDK** provide accessible buttons, dialogs, tables, forms and overlays.",
     "ng add @angular/material"),
    ("M", "Real Project 1: Task Manager",
     "Build a task app with standalone components, a signal-based `TaskStore`, reactive forms (add task with validation), `@for` lists with filters (All/Active/Done), `computed` counts, routing (`/tasks`, `/tasks/:id`) and `localStorage` persistence through an `effect`.",
     "ng new task-manager --style=css\ncd task-manager && ng g c tasks/task-list && ng g s tasks/task-store"),
    ("M", "Real Project 2: Product Catalog with API",
     "Create a shop front-end: product list from a REST API (`HttpClient` + service), search with `debounceTime` + `switchMap`, product detail route, cart signal with total using `computed`, an auth interceptor and lazy loaded `/admin`. Deploy to Netlify, Firebase Hosting or Azure Static Web Apps.",
     ""),
    ("M", "Architecture and Best Practices",
     "Organise by **feature folders**, use smart (container) vs dumb (presentational) components, keep logic in services, use strict TypeScript and `strictTemplates`, prefer signals + OnPush, name consistently, lint with ESLint, format with Prettier, and keep components small.",
     "src/app/\n  core/      (singletons: auth, interceptors)\n  shared/    (reusable UI, pipes)\n  features/\n    tasks/   (components, store, routes)"),
    ("M", "Security and Accessibility",
     "Angular sanitizes bindings to stop **XSS**; never bypass with `bypassSecurityTrust*` on user data. Store tokens carefully (prefer HttpOnly cookies), validate on the server, and enable CSP. Accessibility: semantic HTML, labels, keyboard focus, `aria-*`, colour contrast.",
     "<button type=\"button\" aria-label=\"Close dialog\" (click)=\"close()\">x</button>"),
    ("M", "Build, Deploy and CI/CD",
     "`ng build` creates optimised files in `dist/`. Deploy to any static host (Nginx, Netlify, Vercel, Firebase, GitHub Pages, S3+CloudFront); serve `index.html` for unknown paths. Automate with CI: install, lint, test, build, deploy.",
     "ng build --configuration production\nnpx http-server dist/my-app/browser -p 8080"),
])

INTERVIEW = [
    ("What are standalone components?", "Components that declare their own `imports` and need no NgModule; the default since Angular 19."),
    ("Signals vs RxJS?", "Signals hold synchronous state with fine-grained updates; RxJS models asynchronous streams. Convert with `toSignal` / `toObservable`."),
    ("Explain change detection.", "Angular checks bindings to update the DOM. Zone.js (or signals in zoneless mode) triggers it; OnPush limits checks to changed inputs/signals/events."),
    ("`switchMap` vs `mergeMap`?", "`switchMap` cancels the previous inner request (search-as-you-type); `mergeMap` runs all in parallel."),
    ("How does lazy loading work?", "Routes use `loadComponent` / `loadChildren` with dynamic `import()`, so the bundler creates a separate chunk downloaded on demand."),
    ("What is an injection token?", "A key for providing and injecting values that are not classes."),
    ("Template-driven vs reactive forms?", "Template-driven: simple, directive-based. Reactive: explicit model in TypeScript, typed, testable, scalable."),
    ("How do you optimise performance?", "OnPush, signals, `@for` track, lazy loading, `@defer`, image optimisation, avoiding heavy template functions, bundle analysis."),
    ("How do you share data between unrelated components?", "A shared service (signals or BehaviorSubject), router state, or a state library like NgRx."),
    ("What is hydration?", "Reusing server-rendered DOM in the browser instead of re-rendering, after SSR."),
]

PROJECTS = [
    "Task Manager with filters, forms and localStorage",
    "Product catalog with search, cart and API integration",
    "Blog with routing, lazy loaded admin and auth guard",
    "Dashboard with charts, `@defer` and signal store",
    "Real-time chat using WebSocket + RxJS",
]


apply_extras(EXTRA, EXTRAS[len(B) + len(I):])


def build():
    detailed = []
    for t in B + I:
        main = next((p for p in t.get("programs", []) if p["kind"] != "support"), None)
        detailed.append({
            "level": t["level"], "title": t["title"], "text": t["definition"],
            "code": (main["code"] if main else t.get("syntax", "")),
            "lang": "typescript", "mistakes": t["mistakes"][:3], "interview": t["interview"][:3],
            "exercises": t["exercises"], "syntax": t.get("syntax", ""), "syntax_lang": t.get("syntax_lang", "typescript"),
            "real_en": t["real_en"], "tamil": t["tamil"], "pros": t["pros"], "cons": t["cons"], "new": t["new"],
        })
    return {"name": "Angular", "lang": "typescript", "topics": detailed + EXTRA,
            "interview": INTERVIEW, "projects": PROJECTS}
