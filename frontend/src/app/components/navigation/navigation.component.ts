import { Component, OnInit } from '@angular/core';
import { MatDialog } from "@angular/material/dialog";
import { SignUpDialogComponent } from "../dialogs/sign-up-dialog/sign-up-dialog.component";

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
  ]
  constructor( public dialog: MatDialog ) { }

  ngOnInit(): void {
  }

  openSignUpDialog(): void {
    this.dialog.open(SignUpDialogComponent, {
      width: '450px',
      data: {}
    });
  }

}
