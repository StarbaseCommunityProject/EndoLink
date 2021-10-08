import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from "@angular/forms";

@Component({
  selector: 'app-sign-up-dialog',
  templateUrl: './sign-up-dialog.component.html',
  styleUrls: ['./sign-up-dialog.component.scss']
})
export class SignUpDialogComponent implements OnInit {

  signUpForm: FormGroup;

  constructor( private formBuilder: FormBuilder ) {
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
    console.log(this.signUpForm.value);
  }

}
