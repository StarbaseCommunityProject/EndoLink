import { Component, OnInit } from '@angular/core';

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
  constructor() { }

  ngOnInit(): void {
  }

}
