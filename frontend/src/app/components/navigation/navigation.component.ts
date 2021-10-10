import { Component, OnInit } from '@angular/core';
import { MatDialog } from "@angular/material/dialog";
import { SignUpDialogComponent } from "../dialogs/sign-up-dialog/sign-up-dialog.component";
import { AuthenticationService } from '../../services/authentication/authentication.service';
import { User } from '../../types/user.types';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent implements OnInit {

  buttons = [
    {name: "Stocks", link: "link1"},
    {name: "Ships", link: "link2"},
    {name: "Market", link: "link3"},
    {name: "Factions", link: "link4"}
  ];
  user: User | null = null;

  constructor( private dialog: MatDialog,
               private authenticationService: AuthenticationService ) {
    this.authenticationService.user.subscribe( user => this.user = user );
  }

  ngOnInit(): void {
  }

  openSignUpDialog(): void {
    this.dialog.open( SignUpDialogComponent, {
      width: '450px',
      data: {}
    } );
  }

}
