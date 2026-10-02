import { Component, computed, effect, signal, untracked } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <h3>Idli Order</h3>
    <button id="dec" (click)="dec()">-</button>
    <strong>{{ plates() }}</strong>
    <button id="inc" (click)="inc()">+</button>

    <p>Price per plate: ₹{{ price }}</p>
    <p>Total: ₹{{ total() }}</p>

    <h4>Change history (written by an effect)</h4>
    <ul>
      @for (h of history(); track $index) { <li>{{ h }}</li> }
    </ul>
  `,
})
export class CartSignalsComponent {
  price = 30;
  plates = signal(1); // writable signal

  // computed: derived, read-only, cached
  total = computed(() => this.plates() * this.price);

  history = signal<string[]>([]);

  constructor() {
    // effect: runs once now and again whenever plates() changes
    effect(() => {
      const message = `plates = ${this.plates()}`;
      // untracked: do not re-run this effect when history changes
      untracked(() => this.history.update((h) => [...h, message]));
    });
  }

  inc() { this.plates.update((n) => n + 1); }
  dec() { this.plates.update((n) => Math.max(1, n - 1)); }
}
