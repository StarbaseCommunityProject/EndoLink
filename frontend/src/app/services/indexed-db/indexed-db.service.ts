import { Injectable } from '@angular/core';
import { openDB, OpenDBCallbacks } from 'idb';

@Injectable({
  providedIn: 'root'
})
export class IndexedDbService {

  indexedDb: any;
  storeName = "endolink"

  constructor() {
  }

  init(): void {
    if ( !( 'indexedDB' in window ) ) {
      alert( 'IndexedDB is not supported in your browser!\n' +
        'For user authentication to work it is recommended to use a Chromium-based browser or the latest version of Firefox.\n' +
        'If you\'re seeing this error while using Internet Explorer, you deserve nothing less.' );
    }

    this.indexedDb = openDB( this.storeName, 1, {
      upgrade( db ): void {
        db.createObjectStore( 'keyval' );
      }
    } );
  }

  async get( key: string ): Promise<any> {
    return ( await this.indexedDb ).get( 'keyval', key );
  }

  async set( key: string, val: any ): Promise<any> {
    return ( await this.indexedDb ).put( 'keyval', val, key );
  }

  async setMultiple( pairs: { key: string, val: any }[] ): Promise<any> {
    pairs.map( async pair => {
      return ( await this.indexedDb ).put( 'keyval', pair.val, pair.key )
    } );
    return Promise.all( pairs );
  }


  async delete( key: string ): Promise<any> {
    return ( await this.indexedDb ).delete( 'keyval', key );
  }

  async clear(): Promise<any> {
    return ( await this.indexedDb ).clear( 'keyval' );
  }

  async keys(): Promise<any> {
    return ( await this.indexedDb ).getAllKeys( 'keyval' );
  }

}
