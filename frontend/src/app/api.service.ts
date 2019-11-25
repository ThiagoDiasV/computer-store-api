import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class ApiService {

  private apiRoot = 'https://silvertec.herokuapp.com/';

  constructor(private http: HttpClient) { }


  getOrders() {
    return this.http.get(this.apiRoot.concat('orders/'));
  }

  getComputers() {
    return this.http.get(this.apiRoot.concat('computers/'));
  }

  getUsers() {
    return this.http.get(this.apiRoot.concat('users/'));
  }

  getProcessors() {
    return this.http.get(this.apiRoot.concat('processors/'));
  }

  getMotherboards() {
    return this.http.get(this.apiRoot.concat('motherboards/'));
  }

  getMemories() {
    return this.http.get(this.apiRoot.concat('memories/'));
  }

  getGraphicCards() {
    return this.http.get(this.apiRoot.concat('graphiccards/'));
  }

}