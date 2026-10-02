"""Extra sections for Angular topics, aligned with angular_guide order (22 detailed + 14 condensed).

Tuple: (syntax, real_world_en, real_world_ta, pros, cons, new_features)
 - ta is "" for the first 22 topics (their Tamil text already exists in the topic content).
 - pros / cons are separated by " | ".
"""
EXTRAS = [
    # 01 Introduction
    ("", "Think of a railway station display board: only the train timings change on the screen, the whole building is not rebuilt. An Angular single page app refreshes only the part of the page that changed.", "",
     "Complete framework (router, forms, HTTP) | Strong TypeScript tooling | Backed by Google, long-term support | Good for large teams", "Steeper learning curve than React or Vue | More boilerplate to learn | Larger initial bundle for tiny apps",
     "Standalone components are the default (v19+) | Signals for reactivity | New `@if/@for` control flow | Zoneless change detection (default in new v21 apps) | Vite/esbuild based builds"),
    # 02 Setup & CLI
    ("", "Opening a new shop: instead of arranging the building, electricity and shelves yourself, a contractor sets everything up in a day. `ng new` is that contractor.", "",
     "One command scaffolds a whole project | Generators keep a consistent structure | Built-in dev server, build and test commands", "Needs Node.js and many npm packages | First install can be slow",
     "Application builder uses esbuild + Vite (very fast builds) | `ng new` creates standalone apps | Vitest is the default test runner in v21"),
    # 03 TypeScript
    ("", "At a ration shop, rice is measured in kilograms and oil in litres. If someone asks for 'two litres of rice', the shopkeeper stops the mistake immediately. Types do the same for your code before it runs.", "",
     "Catches bugs at compile time | Great autocomplete and refactoring | Self-documenting code", "Extra compile step | Types can be verbose in complex cases | Types vanish at runtime",
     "`satisfies` operator | Standard decorators (TS 5) | `const` type parameters | Inferred type predicates | Node.js can run simple TypeScript directly (type stripping)"),
    # 04 Components
    ("", "A wedding hall has separate teams for catering, decoration and reception; each handles only its own job. Each Angular component handles one part of the screen.", "",
     "Reusable building blocks | Easy to test in isolation | Scoped styles avoid CSS clashes", "Too many tiny components can add overhead | Need to import each component where it is used",
     "Standalone by default (no NgModule) | Self-closing tags like `<app-card />` | `host` metadata replaces `@HostBinding`/`@HostListener`"),
    # 05 Data binding
    ("", "At a tea stall you tell the master 'less sugar' and read the price board. Information flows both ways: the board shows data to you, and your order goes back to the master.", "",
     "Less manual DOM code | View always matches data | Declarative and readable", "Wrong brackets cause confusing errors | Heavy logic in templates hurts performance",
     "`@let` template variables | Signal-based `model()` for two-way binding | Stricter template type checking"),
    # 06 Control flow
    ("", "At a cinema counter: if tickets are available you sell, else you show 'House Full'; for every person in the queue you do the same steps; if nobody is in the queue you show 'No show'. That is `@if`, `@for`, `@empty`.", "",
     "No imports needed | Cleaner syntax than `*ngIf`/`*ngFor` | Faster (built into the compiler) | `track` improves list performance", "`track` is mandatory in `@for` | Older code must be migrated",
     "Stable since v18 | `*ngIf`, `*ngFor` deprecated | Automatic migration: `ng generate @angular/core:control-flow`"),
    # 07 Directives & styling
    ("", "During Pongal the same doorstep gets a bigger, colourful kolam. The door is the same; only the look changes with the occasion. Class and style bindings change the look with the state.", "",
     "Dynamic UI without touching the DOM | Simple `[class.x]` syntax | Works with signals", "Inline styles are hard to maintain | NgClass/NgStyle need imports",
     "Prefer `[class]` and `[style]` bindings over NgClass/NgStyle in new code | Directive composition API (`hostDirectives`)"),
    # 08 Signals
    ("", "At an idli shop, when you change the number of plates the bill total updates by itself, because the formula 'plates x price' is already known. A signal is the number of plates and `computed` is the bill.", "",
     "Fine-grained updates (fast) | Simple mental model | No subscriptions to manage | Works without Zone.js", "Different from RxJS, so two models to learn | Effects can be overused",
     "Signals stable (v17-v20) | `linkedSignal` and `resource` (v19) | Signal-based inputs, outputs and queries | Experimental Signal Forms (v21)"),
    # 09 Communication
    ("", "A mother (parent) asks a child to bring half a kilo of rice (input); the child comes back and shouts 'got it!' (output). Data flows down, events flow up.", "",
     "Clear one-way data flow | Type-safe inputs/outputs | Required inputs checked at compile time", "Deep trees cause prop drilling (use services) | Overusing two-way binding hides data flow",
     "Function-based `input()`, `output()`, `model()` (stable v19) | Old `@Input/@Output` still supported"),
    # 10 Pipes
    ("", "A vegetable shop keeps tomato price as 40 in the ledger but prints '₹40.00 per kg' on the bill. The data is unchanged; only the display format changes. That is a pipe.", "",
     "Reusable formatting | Pure pipes are cached | Keeps components clean", "Impure pipes can slow the app | Locale data must be configured for other regions",
     "All built-in pipes are standalone | `toSignal` often replaces the `async` pipe | `@let` can store pipe results"),
    # 11 Services & DI
    ("", "A whole village shares one public water tap. A service is that single shared tap; dependency injection is the municipality bringing the connection to your home.", "",
     "Shared logic and state | Easy to mock in tests | Loose coupling", "Singletons can hide global state | Wrong provider scope causes confusing bugs",
     "`inject()` function (replaces constructor injection) | `provideAppInitializer` | Tree-shakable `providedIn: 'root'`"),
    # 12 Template-driven forms
    ("", "A railway reservation form is printed with boxes for name and age. If you hand it over with the name box empty, the counter rejects it. Required/minlength attributes act like that counter clerk.", "",
     "Fast to write for simple forms | Little TypeScript code | Familiar HTML validation attributes", "Hard to test | Not suitable for dynamic or large forms | Logic spread across the template",
     "Signal Forms (experimental in v21) aim to simplify form handling | Unified control state events (v18)"),
    # 13 Reactive forms
    ("", "Before printing wedding invitations you plan every field and rule with the designer first; the printer just follows. Reactive forms define the rules in code first, the template follows.", "",
     "Explicit and testable | Strongly typed | Great for dynamic forms (FormArray) | Observable `valueChanges`", "More code than template-driven | Steeper learning curve",
     "Typed forms (v14) | `FormRecord` | `events` stream on controls (v18) | Signal Forms experimental"),
    # 14 Validation
    ("", "When opening a bank account you type the password twice. A rule that compares both fields tells you 'passwords do not match'. That is a cross-field validator.", "",
     "Reusable rules | Cross-field checks | Async validators for server checks", "Group errors are easy to forget to display | Complex validators need good tests",
     "Typed validators with typed forms | Schema based validation in experimental Signal Forms"),
    # 15 Routing
    ("", "Koyambedu bus stand is one station, but each platform number leads to a different bus. A URL is the platform number; the matching component is the bus.", "",
     "Deep links and browser back/forward work | Lazy loading support | Guards and resolvers built in", "Misconfigured routes are hard to debug | Hash vs path URLs need server setup",
     "Standalone `provideRouter` | View transitions (`withViewTransitions`) | Functional guards | `redirectTo` can be a function (v18.1)"),
    # 16 Params
    ("", "A postal address 'Anna Nagar / house 12': the area is the layout and 12 is the changing part (parameter). A query parameter is a note like 'urgent'.", "",
     "Shareable URLs | Params bound directly to inputs | Nested layouts via child routes", "Params are always strings | Easy to forget outlet in parent routes",
     "`withComponentInputBinding()` binds params, query and data to inputs | Router state signals (`toSignal`)"),
    # 17 Guards & lazy loading
    ("", "At a temple special-darshan entrance the staff checks your ticket (guard). Prasadam for each shrine is cooked only when devotees arrive there (lazy loading).", "",
     "Smaller first load | Central access control | Redirects with UrlTree", "Guards are not real security | Lazy chunks add a small delay on first visit",
     "Functional guards (`CanActivateFn`) | `canMatch` | `@defer` for lazy template parts | Prefetching with `withPreloading`"),
    # 18 HttpClient
    ("", "In a restaurant you order masala dosa (request); the kitchen prepares it and sends it (response). While waiting you see 'preparing' (loading); if batter is over you are told (error).", "",
     "Typed requests/responses | Interceptors | Easy testing with mocks | Works with RxJS", "Observables must be subscribed | Boilerplate for loading/error states",
     "`provideHttpClient(withFetch())` | Functional interceptors | `httpResource` (experimental) for signal-based requests"),
    # 19 RxJS
    ("", "Sun TV live is always streaming; you see it only when you switch the TV on (subscribe) and it stops when you switch off (unsubscribe). Filtering ads is `filter`, converting each scene to Tamil is `map`.", "",
     "Powerful operators | Cancellable async work | Great for events and streams", "Steep learning curve | Easy to leak subscriptions | Overkill for simple state",
     "`toSignal` / `toObservable` interop | `takeUntilDestroyed` | `rxResource`"),
    # 20 Lifecycle
    ("", "A tea shop's day: open the shop (`ngOnInit`), update the price board when prices change (`ngOnChanges`), and at night switch off the stove and wash the vessels (`ngOnDestroy`).", "",
     "Clear points to start/stop work | Prevents memory leaks when used correctly", "Many hooks to remember | Wrong hook choice causes ExpressionChanged errors",
     "`afterNextRender` / `afterEveryRender` | `DestroyRef.onDestroy` | Effects often replace some hooks"),
    # 21 Content projection
    ("", "You buy an empty gift box: the shop gives the box, lid and ribbon, and you choose what to put inside. `<ng-content>` is the space for your items.", "",
     "Flexible wrapper components | Multiple slots with `select` | Keeps components generic", "Projected content is created even if not shown | Harder to type-check than inputs",
     "Signal queries `viewChild()` / `contentChild()` (stable v19) | `ngProjectAs`"),
    # 22 Custom directives
    ("", "A teacher uses a yellow highlighter on any book line. The text does not change; only the look does. An attribute directive works like that highlighter on any element.", "",
     "Reusable behaviour | No template needed | Composable with `hostDirectives`", "Can hide behaviour from template readers | Over-engineering risk",
     "`host` metadata object | Directive composition API | Signal inputs for directives"),
    # 23 Interceptors
    ("", "Every parcel leaving a courier office passes one counter where the company stamps it. An HTTP interceptor stamps every request (token, logging) in one place.", "ஒரு கூரியர் அலுவலகத்திலிருந்து வெளியே செல்லும் ஒவ்வொரு பார்சலும் ஒரே கவுண்டரில் முத்திரை பெறுகிறது. அதுபோல HTTP interceptor ஒவ்வொரு request-க்கும் token, log போன்றவற்றை ஒரே இடத்தில் சேர்க்கிறது.",
     "One place for cross-cutting HTTP logic | Keeps services clean | Easy global error handling", "Order of interceptors matters | Can hide side effects",
     "Functional interceptors with `withInterceptors` | Works with `withFetch()`"),
    # 24 Advanced RxJS
    ("", "In a search box, you only want the result for the latest word typed, not for each letter. `switchMap` cancels the old request, like a waiter forgetting the old order when you change it.", "தேடல் பெட்டியில் கடைசியாக தட்டச்சு செய்த சொல்லுக்கான முடிவு மட்டுமே தேவை. `switchMap` பழைய request-ஐ நிறுத்திவிடும் - ஆர்டரை மாற்றினால் சர்வர் பழைய ஆர்டரை மறந்துவிடுவது போல.",
     "Handles races and cancellation | Concise async pipelines", "Choosing the wrong flattening operator causes bugs | Hard to debug",
     "`debounce` and `resource` helpers with signals | RxJS 7 tree-shakable imports"),
    # 25 State management
    ("", "A shop keeps one common stock register that billing, store room and owner all read. A signal store is that single register for the whole app.", "ஒரு கடையில் பில்லிங், கிடங்கு, உரிமையாளர் அனைவரும் பார்க்கும் ஒரே பொது இருப்புப் பதிவேடு இருக்கும். Signal store என்பது முழு செயலிக்கும் அந்த ஒரே பதிவேடு.",
     "Predictable data flow | Easy debugging (NgRx DevTools) | Simple signal stores need little code", "NgRx adds boilerplate | Over-engineering small apps",
     "NgRx SignalStore | `linkedSignal` | `resource` API for async state"),
    # 26 Change detection
    ("", "A supervisor checks only the counters where something changed instead of walking through the whole mall every minute. OnPush checks only changed components.", "ஒவ்வொரு நிமிடமும் முழு வணிக வளாகத்தையும் சுற்றாமல், மாற்றம் நடந்த கவுண்டர்களை மட்டும் மேற்பார்வையாளர் பார்ப்பது போல OnPush மாற்றமுள்ள component-ஐ மட்டும் சரிபார்க்கும்.",
     "Big performance gains | Predictable updates | Works great with signals", "Mutating objects breaks updates | Needs immutable thinking",
     "Zoneless change detection (stable, default in new v21 apps) | Signals drive updates"),
    # 27 Advanced DI
    ("", "A school office can give the same form (token) to every class but each class may fill it with different rules (providers). Tokens let you swap implementations easily.", "பள்ளி அலுவலகம் எல்லா வகுப்புக்கும் ஒரே படிவத்தை (token) கொடுக்கும்; ஆனால் ஒவ்வொரு வகுப்பும் தன் விதிகளுடன் நிரப்பலாம். Token மூலம் செயலாக்கத்தை எளிதாக மாற்றலாம்.",
     "Swappable implementations | Better testing | Scoped instances", "Complex injector trees are hard to reason about", "`provideAppInitializer` | `EnvironmentProviders` | Simplified `inject()` options"),
    # 28 Defer
    ("", "A bakery bakes special cakes only when a customer actually orders them, not all day in advance. `@defer` loads heavy parts only when needed.", "பேக்கரி சிறப்பு கேக்குகளை வாடிக்கையாளர் ஆர்டர் செய்யும்போது மட்டுமே தயாரிக்கிறது. `@defer` கனமான பகுதிகளை தேவைப்படும்போது மட்டுமே ஏற்றுகிறது.",
     "Smaller initial bundle | Declarative lazy loading | Built-in placeholder/loading states", "Layout shift if placeholders are not sized | Needs triggers designed carefully",
     "Incremental hydration (v19) | New triggers: viewport, idle, interaction, hover, timer"),
    # 29 Testing
    ("", "Before a bus leaves, the mechanic checks brakes, lights and horn. Automated tests are that checklist run on every build.", "பேருந்து புறப்படும் முன் மெக்கானிக் பிரேக், விளக்கு, ஹாரன் ஆகியவற்றைச் சோதிக்கிறார். Automated tests ஒவ்வொரு build-க்கும் அந்தச் சோதனைப் பட்டியலை இயக்குகின்றன.",
     "Safe refactoring | Catches regressions | Documents behaviour", "Takes time to write | Brittle tests if overly coupled to the DOM",
     "Vitest default in v21 | Zoneless testing support | Jasmine/Karma deprecated"),
    # 30 SSR
    ("", "A restaurant serves a ready-made plate (server rendered page) instead of making the guest cook; hydration is the guest only adding the final seasoning.", "உணவகம் விருந்தினரை சமைக்கச் சொல்லாமல் தயாரான தட்டை (server-rendered page) பரிமாறுகிறது; hydration என்பது விருந்தினர் கடைசி மசாலா மட்டும் சேர்ப்பது.",
     "Faster first paint | Better SEO | Better perceived performance", "More complex hosting | Browser-only APIs need guards",
     "Incremental hydration | Event replay | Route-level render modes (SSR/SSG/CSR) | Hybrid rendering"),
    # 31 Animations
    ("", "Temple lamps fade softly instead of switching on suddenly. Animations make UI changes feel smooth.", "கோயில் தீபங்கள் திடீரென எரியாமல் மெதுவாக ஒளிர்கின்றன. Animation UI மாற்றங்களை மென்மையாக உணரச் செய்கிறது.",
     "Smoother UX | CSS-based animations are fast", "Overuse distracts and hurts accessibility", "`animate.enter` / `animate.leave` (v20.2) | `@angular/animations` deprecated"),
    # 32 Real project 1
    ("", "A shop owner's daily to-do board: add job, mark done, filter pending. A task manager app follows the same flow.", "கடை உரிமையாளரின் தினசரி வேலைப் பலகை: வேலை சேர், முடிந்ததாகக் குறி, நிலுவையில் உள்ளவற்றை வடிகட்டு. Task manager app அதே வழியில் செயல்படும்.",
     "Practises components, forms, routing, signals together", "Needs planning to avoid messy structure", "Use standalone components, signals and zoneless for a modern setup"),
    # 33 Real project 2
    ("", "An online grocery store lists products from a server, searches quickly and keeps a cart. This project practices API integration end to end.", "ஆன்லைன் மளிகைக் கடை சேவையகத்திலிருந்து பொருட்களைப் பட்டியலிட்டு, விரைவாகத் தேடி, கூடை வைத்திருக்கும். இந்த project API இணைப்பை முழுமையாகப் பயிற்சி செய்ய உதவும்.",
     "Real-world API practice | Covers search, cart, auth", "Needs a backend or mock API", "Use `httpResource` / `resource` and signal stores"),
    # 34 Architecture
    ("", "A hospital has separate wards, a common pharmacy and shared admin. Feature folders, shared and core modules mirror that layout.", "மருத்துவமனையில் தனித் தனி வார்டுகள், பொது மருந்தகம், பொது நிர்வாகம் இருப்பது போல feature, shared, core folders அமைக்கப்படுகின்றன.",
     "Easier onboarding | Scales with team size | Predictable structure", "Over-structuring small apps wastes time", "Standalone APIs remove NgModule boilerplate | `ng generate` uses modern defaults"),
    # 35 Security
    ("", "A jewellery shop checks every customer at the door and locks valuables, even when the staff is honest. Angular sanitises HTML by default, but you must still validate on the server.", "நகைக்கடை நேர்மையான ஊழியர்கள் இருந்தாலும் வாசலில் சோதனை செய்து நகைகளைப் பூட்டி வைக்கிறது. Angular HTML-ஐ தானாக சுத்தப்படுத்தினாலும் server-இல் சரிபார்ப்பு அவசியம்.",
     "XSS protection by default | Built-in sanitisation | CSP friendly", "Bypassing sanitisation re-opens risks", "Trusted Types support | Stricter template checks"),
    # 36 Build & deploy
    ("", "A caterer packs the finished food in boxes and delivers it to the venue. `ng build` packs your app; hosting delivers it to users.", "சமையல்காரர் தயாரான உணவைப் பெட்டிகளில் அடைத்து நிகழ்ச்சி இடத்துக்கு அனுப்புகிறார். `ng build` செயலியை தொகுக்கிறது; hosting அதைப் பயனர்களுக்கு வழங்குகிறது.",
     "Optimised, tree-shaken bundles | Works on any static host | Easy CI/CD", "SPA needs rewrite rules for deep links", "esbuild builder | Prerendering/SSG | Faster builds with caching"),
]
