import { Component, computed, signal } from '@angular/core';
import { NgClass, NgStyle } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [NgClass, NgStyle],
  template: `
    <!-- class binding: add the "hot" class only when isHot() is true -->
    <p [class.hot]="isHot()">Tea is {{ isHot() ? 'hot' : 'cold' }}</p>

    <!-- NgClass with an object: several classes at once -->
    <p [ngClass]="{ big: size() > 16, small: size() <= 16 }">Size {{ size() }}px</p>

    <!-- style binding with a unit -->
    <p [style.font-size.px]="size()">This text resizes</p>

    <!-- NgStyle with an object -->
    <p [ngStyle]="{ color: textColor(), 'font-weight': 'bold' }">Colour: {{ textColor() }}</p>

    <button id="temp" (click)="isHot.set(!isHot())">Toggle temperature</button>
    <button id="size" (click)="size.update(s => s + 4)">Bigger text</button>
  `,
  styles: `
    .hot { color: crimson; }
    .big { text-decoration: underline; }
  `,
})
export class DynamicStyleComponent {
  isHot = signal(true);
  size = signal(14);
  // computed: derived value that updates automatically
  textColor = computed(() => (this.isHot() ? 'crimson' : 'royalblue'));
}
