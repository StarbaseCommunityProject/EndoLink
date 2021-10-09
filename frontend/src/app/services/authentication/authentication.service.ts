import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { SignUpErrorResponse, SignUpResponse, User } from '../../types/authentication.types';
import { BehaviorSubject, Observable } from 'rxjs';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  apiUrl = environment.apiUrl;

  // TODO implement and save tokens to IndexedDB for persistence across browser sessions
  user: BehaviorSubject<User | null>
    = new BehaviorSubject<User | null>( null );
  accessToken: BehaviorSubject<string | null>
    = new BehaviorSubject<string | null>( null );
  refreshToken: BehaviorSubject<string | null>
    = new BehaviorSubject<string | null>( null );

  constructor( private httpClient: HttpClient ) { }

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
        return httpResponse as SignUpResponse;
      } )
      .catch( ( httpResponse: HttpErrorResponse ) => {
        throw { status: httpResponse.status, message: httpResponse.message } as SignUpErrorResponse
      } );
  }

}
