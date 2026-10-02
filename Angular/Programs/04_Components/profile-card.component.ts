import { Component } from '@angular/core';

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
