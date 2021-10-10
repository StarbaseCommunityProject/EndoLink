import {
  AbstractControl,
  FormControl,
  FormGroupDirective,
  NgForm,
  ValidationErrors,
  ValidatorFn
} from '@angular/forms';
import { ErrorStateMatcher } from '@angular/material/core';

export const passwordValidator: ValidatorFn = ( form: AbstractControl ):  ValidationErrors | null => {
  const { password, passwordRepeat } = form.value;
  return password === passwordRepeat
    ? null
    : { error: 'Passwords do not match' }
}

export class PasswordErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const invalidCtrl = !!(control?.invalid && control?.parent?.dirty);
    const invalidParent = !!(control?.parent?.invalid && control?.parent?.dirty);
    return !!control?.touched && ( invalidCtrl || invalidParent );
  }
}
