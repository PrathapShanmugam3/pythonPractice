import { AfterViewInit, Component, inject, Injectable, input, OnChanges, OnDestroy, OnInit, signal, SimpleChanges } from '@angular/core';

// A tiny service so we can SEE the order of the hooks on screen
@Injectable({ providedIn: 'root' })
export class LogService {
  logs = signal<string[]>([]);
  add(message: string) {
    this.logs.update((l) => [...l, message]);
  }
}

@Component({
  selector: 'app-tea-card',
  template: `<p>Tea: {{ name() }}</p>`,
})
export class TeaCardComponent implements OnChanges, OnInit, AfterViewInit, OnDestroy {
  name = input.required<string>();
  private log = inject(LogService);

  constructor() {
    this.log.add('constructor');
  }
  ngOnChanges(changes: SimpleChanges) {
    this.log.add(`ngOnChanges -> ${changes['name'].currentValue}`);
  }
  ngOnInit() {
    this.log.add('ngOnInit');
  }
  ngAfterViewInit() {
    this.log.add('ngAfterViewInit');
  }
  ngOnDestroy() {
    this.log.add('ngOnDestroy');
  }
}

@Component({
  selector: 'app-root',
  imports: [TeaCardComponent],
  template: `
    <button id="rename" (click)="tea.set('Ginger Tea')">Rename tea</button>
    <button id="toggle" (click)="show.set(!show())">{{ show() ? 'Remove' : 'Show' }} card</button>

    @if (show()) { <app-tea-card [name]="tea()" /> }

    <h4>Hook log</h4>
    <ol>
      @for (l of logger.logs(); track $index) { <li>{{ l }}</li> }
    </ol>
  `,
})
export class LifecycleLoggerComponent {
  logger = inject(LogService);
  show = signal(true);
  tea = signal('Masala Tea');
}
