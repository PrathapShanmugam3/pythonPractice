import { Component } from '@angular/core';

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
