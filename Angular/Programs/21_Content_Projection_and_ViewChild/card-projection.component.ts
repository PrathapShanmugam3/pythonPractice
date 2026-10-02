import { Component, ElementRef, signal, viewChild } from '@angular/core';

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
