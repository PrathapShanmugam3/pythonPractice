import { Component, computed, inject, Injectable, signal } from '@angular/core';

// A service: ONE shared instance for the whole app (providedIn: 'root')
@Injectable({ providedIn: 'root' })
export class CartService {
  private readonly items = signal<string[]>([]);

  readonly list = this.items.asReadonly(); // others can read, but not change directly
  readonly count = computed(() => this.items().length);

  add(item: string) {
    this.items.update((current) => [...current, item]);
  }

  clear() {
    this.items.set([]);
  }
}

// Component 1 writes to the cart
@Component({
  selector: 'app-product-list',
  template: `
    @for (p of products; track p) {
      <button (click)="cart.add(p)">Add {{ p }}</button>
    }
  `,
})
export class ProductListComponent {
  products = ['Idli Batter', 'Filter Coffee Powder'];
  cart = inject(CartService); // dependency injection
}

// Component 2 reads the SAME cart
@Component({
  selector: 'app-cart-badge',
  template: `
    <p>Cart items: {{ cart.count() }}</p>
    <ul>
      @for (item of cart.list(); track $index) { <li>{{ item }}</li> }
    </ul>
  `,
})
export class CartBadgeComponent {
  cart = inject(CartService);
}

@Component({
  selector: 'app-root',
  imports: [ProductListComponent, CartBadgeComponent],
  template: `
    <h2>Online Grocery</h2>
    <app-product-list />
    <app-cart-badge />
  `,
})
export class AppComponent {}
