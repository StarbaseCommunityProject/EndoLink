import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthenticationService } from '../../../services/authentication/authentication.service';
import { PasswordErrorStateMatcher, passwordValidator } from '../../validators/authentication.validators';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-sign-up-dialog',
  templateUrl: './sign-up-dialog.component.html',
  styleUrls: ['./sign-up-dialog.component.scss']
})
export class SignUpDialogComponent implements OnInit {

  @ViewChild('pictureInput') pictureInput: any;

  signUpForm: FormGroup;
  logInForm: FormGroup;
  passwordErrorStateMatcher = new PasswordErrorStateMatcher()

  avatarPreview: string | ArrayBuffer | null = null;

  constructor( private formBuilder: FormBuilder,
               private authenticationService: AuthenticationService,
               private dialogRef: MatDialogRef<SignUpDialogComponent> ) {
    this.signUpForm = this.formBuilder.group( {
      picture: new FormControl( null ),
      username: new FormControl( null, [ Validators.required, Validators.nullValidator ] ),
      email: new FormControl( null, [ Validators.required, Validators.email ] ),
      password: new FormControl( null, [ Validators.required ] ),
      passwordRepeat: new FormControl( null ),
    }, { validators: passwordValidator } );

    this.logInForm = this.formBuilder.group( {
      username: new FormControl( null, [ Validators.required, Validators.nullValidator ] ),
      password: new FormControl( null, [ Validators.required, Validators.nullValidator ] ),
    } );

    this.signUpForm.valueChanges.subscribe( async formChange => {
      if ( formChange.picture && '0' in this.pictureInput.nativeElement.files ) {
        this.getBase64Image( this.pictureInput.nativeElement.files[0] ).then( base64Image => {
          this.avatarPreview = base64Image;
        } );
      }
    } );
  }

  ngOnInit(): void {
  }

  submitSignUp(): void {
    const { username, email, password } = this.signUpForm.value;
    this.authenticationService.signUp( username, email, password, this.pictureInput.nativeElement.files )
      .then( response => {
        this.dialogRef.close();
      } )
      .catch( error => {
        console.warn( error );
      } );
  }

  submitLogIn(): void {
    const { username, password } = this.logInForm.value;
    this.authenticationService.logIn( username, password )
      .then( response => {
        this.dialogRef.close();
      } )
      .catch( error => {
        console.warn( error );
      } );
  }

  getBase64Image( image: File ): Promise<string | ArrayBuffer | null> {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL( image );
      reader.onload = () => resolve( reader.result );
      reader.onerror = error => reject(error);
    });
  }

}
