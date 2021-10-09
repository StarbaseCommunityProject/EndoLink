import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from "@angular/forms";
import { AuthenticationService } from '../../../services/authentication/authentication.service';

@Component({
  selector: 'app-sign-up-dialog',
  templateUrl: './sign-up-dialog.component.html',
  styleUrls: ['./sign-up-dialog.component.scss']
})
export class SignUpDialogComponent implements OnInit {

  signUpForm: FormGroup;

  constructor( private formBuilder: FormBuilder,
               private authenticationService: AuthenticationService ) {
    // TODO add validators
    this.signUpForm = this.formBuilder.group( {
      username: [''],
      email: [''],
      password: [''],
      passwordRepeat: [''],
    } )
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
