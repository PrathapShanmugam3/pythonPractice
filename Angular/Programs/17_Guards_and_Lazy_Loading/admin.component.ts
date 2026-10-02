import { Component } from '@angular/core';

// This file is loaded lazily by guarded-app.component.ts
@Component({
  selector: 'app-admin',
  template: `
    <h2>Admin Panel</h2>
    <p>This page was lazy loaded after the guard allowed you in.</p>
  `,
})
export class AdminComponent {}
