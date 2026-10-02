import { Component, inject, signal } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [ReactiveFormsModule],
  template: `
    <h3>Student Profile</h3>
    <form [formGroup]="form" (ngSubmit)="submit()">
      <input id="name" formControlName="name" placeholder="Name" />
      @if (form.controls.name.touched && form.controls.name.invalid) { <small>Name needs 3+ letters.</small> }

      <input id="email" formControlName="email" placeholder="Email" />
      @if (form.controls.email.dirty && form.controls.email.invalid) { <small>Enter a valid email.</small> }

      <select formControlName="city">
        <option>Chennai</option>
        <option>Madurai</option>
        <option>Coimbatore</option>
      </select>

      <button type="submit" [disabled]="form.invalid">Save</button>
    </form>

    <p>Form status: {{ form.status }}</p>
    @if (saved()) { <pre>{{ saved() }}</pre> }
  `,
})
export class ReactiveFormComponent {
  private fb = inject(FormBuilder);

  // The form model lives in the class and is fully typed
  form = this.fb.nonNullable.group({
    name: ['', [Validators.required, Validators.minLength(3)]],
    email: ['', [Validators.required, Validators.email]],
    city: ['Chennai'],
  });

  saved = signal('');

  submit() {
    if (this.form.valid) {
      this.saved.set(JSON.stringify(this.form.getRawValue()));
    }
  }
}
