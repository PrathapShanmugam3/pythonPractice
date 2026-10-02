import { ApplicationConfig, Component, inject, Injectable, signal } from '@angular/core';
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
