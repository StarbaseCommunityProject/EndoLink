import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

  footerItems = [{name: "About us", link: "/about"}, {name: "Cookie Policy", link: "/cookies"}, {name: "Privacy Policy", link: "/privacy"}]

  constructor() { }

  ngOnInit(): void {
  }

}
