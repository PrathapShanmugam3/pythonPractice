import { Component, Directive, input, output, signal } from '@angular/core';

// An attribute directive: adds hover highlighting to ANY element
@Directive({
  selector: '[appHighlight]',
  host: {
    '(mouseenter)': 'enter()',
    '(mouseleave)': 'leave()',
    // style binding on the host element
    '[style.background-color]': 'active() ? color() : null',
  },
})
export class HighlightDirective {
  color = input('yellow', { alias: 'appHighlight' }); // <li appHighlight="lightgreen">
  hoverChange = output<boolean>();                     // tell the parent about hover
  active = signal(false);

  enter() {
    this.active.set(true);
    this.hoverChange.emit(true);
  }
  leave() {
    this.active.set(false);
    this.hoverChange.emit(false);
  }
}

@Component({
  selector: 'app-root',
  imports: [HighlightDirective],
  template: `
    <ul>
      @for (item of items; track item) {
        <li appHighlight="lightgreen" (hoverChange)="onHover(item, $event)">{{ item }}</li>
      }
    </ul>
    <p>Hovered: {{ hovered() || 'nothing' }}</p>
  `,
})
export class AppComponent {
  items = ['Idli', 'Filter Coffee', 'Vada'];
  hovered = signal('');

  onHover(item: string, isOver: boolean) {
    this.hovered.set(isOver ? item : '');
  }
}
