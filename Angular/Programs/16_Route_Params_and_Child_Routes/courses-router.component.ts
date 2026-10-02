import { ApplicationConfig, Component, computed, input } from '@angular/core';
import { provideRouter, RouterLink, RouterOutlet, Routes, withComponentInputBinding, withHashLocation } from '@angular/router';

const COURSES = [
  { id: 1, title: 'Angular Basics' },
  { id: 2, title: 'TypeScript Deep Dive' },
];

// Parent layout: its own <router-outlet> shows the child routes
@Component({
  selector: 'app-courses-layout',
  imports: [RouterOutlet],
  template: `<h2>Courses</h2><router-outlet />`,
})
export class CoursesLayoutComponent {}

@Component({
  selector: 'app-course-list',
  imports: [RouterLink],
  template: `
    <ul>
      @for (c of courses; track c.id) {
        <li><a [routerLink]="[c.id]" [queryParams]="{ tab: 'syllabus' }">{{ c.title }}</a></li>
      }
    </ul>
  `,
})
export class CourseListComponent {
  courses = COURSES;
}

@Component({
  selector: 'app-course-detail',
  imports: [RouterLink],
  template: `
    <h3>Course #{{ id() }}: {{ course()?.title ?? 'Unknown' }}</h3>
    <p>Showing tab: {{ tab() }}</p>
    <a routerLink="/courses">Back to list</a>
  `,
})
export class CourseDetailComponent {
  // Filled from the URL thanks to withComponentInputBinding()
  id = input.required<string>();   // path param  :id
  tab = input('overview');         // query param ?tab=
  course = computed(() => COURSES.find((c) => c.id === Number(this.id())));
}

const routes: Routes = [
  { path: '', redirectTo: 'courses', pathMatch: 'full' },
  {
    path: 'courses',
    component: CoursesLayoutComponent,
    children: [
      { path: '', component: CourseListComponent },
      { path: ':id', component: CourseDetailComponent },
    ],
  },
];

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes, withComponentInputBinding(), withHashLocation())],
};

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  template: `<router-outlet />`,
})
export class AppComponent {}
