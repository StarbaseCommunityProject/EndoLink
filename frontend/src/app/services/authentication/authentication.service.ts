import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import {
  LogInErrorResponse,
  LogInResponse,
  SignUpErrorResponse,
  SignUpResponse
} from '../../types/authentication.types';
import { BehaviorSubject } from 'rxjs';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { IndexedDbService } from '../indexed-db/indexed-db.service';
import { User } from '../../types/user.types';
import { AuthenticatedHttpClient } from './authenticated-http-client.class';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  apiUrl = environment.apiUrl;

  user: BehaviorSubject<User | null>
    = new BehaviorSubject<User | null>( null );
  accessToken: BehaviorSubject<string | null>
    = new BehaviorSubject<string | null>( null );
  refreshToken: BehaviorSubject<string | null>
    = new BehaviorSubject<string | null>( null );

  constructor( private httpClient: HttpClient,
               private authenticatedHttpClient: AuthenticatedHttpClient,
               private indexedDbService: IndexedDbService ) { }

  async signUp( username: string,
                email: string,
                password: string )
    : Promise<SignUpResponse | SignUpErrorResponse>
  {
    return this.httpClient.post( `${ this.apiUrl }/api/register`, { username, email, password } )
      .toPromise()
      .then( httpResponse => {
        const { user, jwt } = httpResponse as SignUpResponse;

        this.user.next( user )
        this.accessToken.next( jwt.access )
        this.refreshToken.next( jwt.refresh )

        this.indexedDbService.setMultiple( [
          { key: 'accessToken', val: jwt.access },
          { key: 'refreshToken', val: jwt.refresh }
        ] )
          .then( () => {
            console.warn( 'saved token information' );
          } )
        return httpResponse as SignUpResponse;
      } )
      .catch( ( httpResponse: HttpErrorResponse ) => {
        throw { status: httpResponse.status, message: httpResponse.message } as SignUpErrorResponse;
      } );
  }

  async logIn( username: string,
               password: string )
    : Promise<LogInResponse | LogInErrorResponse>
  {
    return this.httpClient.post( `${ this.apiUrl }/api/token`, { username, password } )
      .toPromise()
      .then( httpResponse => {
        const { access, refresh } = httpResponse as LogInResponse;

        this.accessToken.next( access )
        this.refreshToken.next( refresh )

        this.indexedDbService.setMultiple( [
          { key: 'accessToken', val: access },
          { key: 'refreshToken', val: refresh }
        ] )
          .then( () => {
            console.warn( 'saved token information' );
          } )
        this.getCurrentUser().then( user => this.user.next( user ) )
        return httpResponse as LogInResponse;
      } )
      .catch( ( httpResponse: HttpErrorResponse ) => {
        throw { status: httpResponse.status, message: httpResponse.message } as LogInErrorResponse;
      } );
  }

  getCurrentUser()
    : Promise<User>
  {
    return this.authenticatedHttpClient.get( 'api/current_user' ).then( response => {
      console.log( response );
      return response as User;
    } );
  }

}
