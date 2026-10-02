import { ApplicationConfig, Component } from '@angular/core';
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
