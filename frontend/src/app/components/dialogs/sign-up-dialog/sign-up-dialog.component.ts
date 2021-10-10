import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthenticationService } from '../../../services/authentication/authentication.service';
import { PasswordErrorStateMatcher, passwordValidator } from '../../validators/authentication.validators';

@Component({
  selector: 'app-sign-up-dialog',
  templateUrl: './sign-up-dialog.component.html',
  styleUrls: ['./sign-up-dialog.component.scss']
})
export class SignUpDialogComponent implements OnInit {

  signUpForm: FormGroup;
  passwordErrorStateMatcher = new PasswordErrorStateMatcher()

  constructor( private formBuilder: FormBuilder,
               private authenticationService: AuthenticationService ) {
    this.signUpForm = this.formBuilder.group( {
      username: new FormControl(null, [ Validators.required, Validators.nullValidator ] ),
      email: new FormControl( null, [ Validators.required, Validators.email ] ),
      password: new FormControl( null, [ Validators.required ] ),
      passwordRepeat: new FormControl( null ),
    }, { validators: passwordValidator } )
  }

  ngOnInit(): void {
  }

  submitSignUp(): void {
    const { username, email, password } = this.signUpForm.value;
    this.authenticationService.signUp( username, email, password )
      .then( response => {
        console.log( response );
      } )
      .catch( error => {
        console.warn( error );
      } );
  }

}
