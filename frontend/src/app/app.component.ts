import { Component, OnInit } from '@angular/core';
import { IndexedDbService } from './services/indexed-db/indexed-db.service';
import { AuthenticationService } from './services/authentication/authentication.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {

  constructor( private indexedDbService: IndexedDbService,
               private authenticationService: AuthenticationService ) {
    this.indexedDbService.init().then( () => {
      this.indexedDbService.getMultiple( [ 'accessToken', 'refreshToken' ] ).then( tokens => {
        if ( 'accessToken' in tokens && tokens.accessToken ) {
          this.authenticationService.getCurrentUser().then( user => {
            this.authenticationService.user.next( user );
          } );
        }
      } );
    } );
  }

  ngOnInit(): void {
  }

}
