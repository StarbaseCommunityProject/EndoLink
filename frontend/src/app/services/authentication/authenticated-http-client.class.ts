import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { IndexedDbService } from '../indexed-db/indexed-db.service';
import { environment } from '../../../environments/environment';

interface RequestOptions {
  headers?: HttpHeaders;
  observe?: 'body';
  params?: HttpParams;
  reportProgress?: boolean;
  responseType?: 'json';
  withCredentials?: boolean;
  body?: any;
}

@Injectable()
export class AuthenticatedHttpClient {

  constructor( private httpClient: HttpClient,
               private indexedDbService: IndexedDbService ) {
  }

  async appendAuthorizationHeader( options?: RequestOptions ): Promise<Partial<RequestOptions>> {
    // TODO check if accessToken is still valid, replace or log out if not
    return this.indexedDbService.get( 'accessToken' ).then( accessToken => {
      if ( options && 'headers' in options ) {
        options.headers?.append( 'Authorization', `Bearer ${ accessToken }` );
        return options;
      } else {
        return { headers: new HttpHeaders( { Authorization: `Bearer ${ accessToken }` } ) };
      }
    } );
  }

  public async get<T>( endpoint: string, options?: RequestOptions ): Promise<T> {
    options = await this.appendAuthorizationHeader( options );
    return this.httpClient.get<T>( `${ environment.apiUrl }/${ endpoint }`, options ).toPromise();
  }
}
