import { AsyncPipe } from '@angular/common';
import { Component } from '@angular/core';
import { interval, map, take } from 'rxjs';

@Component({
  selector: 'app-root',
  imports: [AsyncPipe],
  // The async pipe subscribes and unsubscribes automatically
  template: `<p>{{ ticks$ | async }}</p>`,
})
export class TickerComponent {
  // emits 'Tick 1' ... 'Tick 5', one every 100 ms, then completes
  ticks$ = interval(100).pipe(
    take(5),
    map((i) => `Tick ${i + 1}`),
  );
}
