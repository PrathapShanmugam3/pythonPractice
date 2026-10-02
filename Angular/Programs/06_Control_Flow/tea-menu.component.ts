import { Component, signal } from '@angular/core';

interface Tea {
  name: string;
  price: number;
  available: boolean;
}

@Component({
  selector: 'app-root',
  template: `
    <button (click)="open.set(!open())">{{ open() ? 'Close' : 'Open' }} shop</button>

    @if (open()) {
      <h3>Today's Menu</h3>
      <ul>
        @for (item of menu; track item.name; let i = $index) {
          <li>
            {{ i + 1 }}. {{ item.name }} - ₹{{ item.price }}
            @switch (item.available) {
              @case (true) { (available) }
              @case (false) { (sold out) }
            }
          </li>
        } @empty {
          <li>No items today</li>
        }
      </ul>
    } @else {
      <p>The shop is closed.</p>
    }
  `,
})
export class TeaMenuComponent {
  open = signal(false);
  menu: Tea[] = [
    { name: 'Filter Coffee', price: 20, available: true },
    { name: 'Masala Tea', price: 15, available: true },
    { name: 'Badam Milk', price: 30, available: false },
  ];
}
