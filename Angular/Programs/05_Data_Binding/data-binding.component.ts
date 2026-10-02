import { Component } from '@angular/core';
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
