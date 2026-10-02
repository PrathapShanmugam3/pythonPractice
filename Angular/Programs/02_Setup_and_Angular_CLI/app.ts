import {
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
