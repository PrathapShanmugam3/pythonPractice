import { HttpClient, provideHttpClient } from '@angular/common/http';
import { ApplicationConfig, Component, inject, Injectable, signal } from '@angular/core';

export const appConfig: ApplicationConfig = {
  providers: [provideHttpClient()], // enables HttpClient
};

interface Todo {
  id: number;
  title: string;
  done: boolean;
}

// All API calls live in a service
@Injectable({ providedIn: 'root' })
export class TodoApi {
  private http = inject(HttpClient);
  private base = 'https://api.example.com'; // replace with your real API

  list() {
    return this.http.get<Todo[]>(`${this.base}/todos`);
  }
  add(title: string) {
    return this.http.post<Todo>(`${this.base}/todos/add`, { title });
  }
  broken() {
    return this.http.get<Todo[]>(`${this.base}/broken`);
  }
}

@Component({
  selector: 'app-root',
  template: `
    <button id="load" (click)="load()">Load todos</button>
    <button id="add" (click)="add()">Add todo</button>
    <button id="broken" (click)="callBroken()">Call broken URL</button>

    @if (loading()) { <p>Loading...</p> }
    @if (error()) { <p>Error: {{ error() }}</p> }

    <ul>
      @for (t of todos(); track t.id) {
        <li>{{ t.done ? '[x]' : '[ ]' }} {{ t.title }}</li>
      }
    </ul>
  `,
})
export class TodoApiComponent {
  private api = inject(TodoApi);
  todos = signal<Todo[]>([]);
  loading = signal(false);
  error = signal('');

  load() {
    this.loading.set(true);
    this.error.set('');
    this.api.list().subscribe({
      next: (data) => {
        this.todos.set(data);
        this.loading.set(false);
      },
      error: () => {
        this.error.set('Could not load todos');
        this.loading.set(false);
      },
    });
  }

  add() {
    this.api.add('Buy jasmine flowers').subscribe((todo) => this.todos.update((list) => [...list, todo]));
  }

  callBroken() {
    this.error.set('');
    this.api.broken().subscribe({ error: () => this.error.set('Server returned an error (500)') });
  }
}
