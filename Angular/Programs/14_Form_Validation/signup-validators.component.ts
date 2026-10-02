import { Component } from '@angular/core';
import { AbstractControl, FormControl, FormGroup, ReactiveFormsModule, ValidationErrors, ValidatorFn, Validators } from '@angular/forms';

// 1. Custom validator for ONE control: returns null (valid) or an error object
const noSpaces: ValidatorFn = (control: AbstractControl): ValidationErrors | null =>
  /\s/.test(control.value) ? { spaces: true } : null;

// 2. Cross-field validator for the WHOLE group
const passwordsMatch: ValidatorFn = (group: AbstractControl): ValidationErrors | null => {
  const password = group.get('password')?.value;
  const confirm = group.get('confirm')?.value;
  return password === confirm ? null : { mismatch: true };
};

@Component({
  selector: 'app-root',
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form">
      <input id="username" formControlName="username" placeholder="Username" />
      @if (form.controls.username.errors?.['spaces']) { <small>No spaces allowed.</small> }

      <input id="password" type="password" formControlName="password" placeholder="Password" />
      @if (form.controls.password.errors?.['minlength']) { <small>Minimum 6 characters.</small> }

      <input id="confirm" type="password" formControlName="confirm" placeholder="Confirm" />
      @if (form.errors?.['mismatch'] && form.controls.confirm.dirty) { <small>Passwords do not match.</small> }
    </form>
    <p>{{ form.valid ? 'Form is valid' : 'Form is invalid' }}</p>
  `,
})
export class SignupValidatorsComponent {
  form = new FormGroup(
    {
      username: new FormControl('', { nonNullable: true, validators: [Validators.required, noSpaces] }),
      password: new FormControl('', { nonNullable: true, validators: [Validators.required, Validators.minLength(6)] }),
      confirm: new FormControl('', { nonNullable: true }),
    },
    { validators: passwordsMatch },
  );
}
