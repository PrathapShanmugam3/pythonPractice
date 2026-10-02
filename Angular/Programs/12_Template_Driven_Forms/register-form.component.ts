import { Component } from '@angular/core';
import { FormsModule, NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [FormsModule],
  template: `
    <h3>Course Registration</h3>
    <form #f="ngForm" (ngSubmit)="submit(f)">
      <label>Name
        <input id="name" name="name" [(ngModel)]="model.name" required minlength="3" #nameCtrl="ngModel" />
      </label>
      @if (nameCtrl.invalid && (nameCtrl.dirty || nameCtrl.touched)) {
        <small>
          @if (nameCtrl.errors?.['required']) { Name is required. }
          @if (nameCtrl.errors?.['minlength']) { Use at least 3 letters. }
        </small>
      }

      <label>Email
        <input id="email" name="email" type="email" [(ngModel)]="model.email" required email />
      </label>

      <button type="submit" [disabled]="f.invalid">Register</button>
    </form>

    <p>Form valid: {{ f.valid }}</p>
    @if (message) { <p>{{ message }}</p> }
  `,
})
export class RegisterFormComponent {
  model = { name: '', email: '' };
  message = '';

  submit(form: NgForm) {
    this.message = `Registered ${form.value.name} (${form.value.email})`;
    form.resetForm();
  }
}
