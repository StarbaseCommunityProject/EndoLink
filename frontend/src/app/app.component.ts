import { Component, OnInit } from '@angular/core';
import { IndexedDbService } from './services/indexed-db/indexed-db.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {

  constructor( private indexedDbService: IndexedDbService ) {
    this.indexedDbService.init();
  }

  ngOnInit(): void {
  }

}
