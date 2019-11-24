import { Component, OnInit } from '@angular/core';

import { ApiService } from './api.service';
import { Order, Computer, User, Processor, MotherBoard, Memory, GraphicCard} from './order.interface';
import { inspect } from 'util';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  orders: Order[];
  computers: Computer[];
  users: User[];
  processors: Processor[];
  motherboards: MotherBoard[];
  memories: Memory[];
  graphiccards: GraphicCard[];
  error: any;

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.api.getOrders().subscribe(
      (orders: Order[]) => this.orders = orders,
      (error: any) => this.error = error
    );
    this.api.getComputers().subscribe(
      (computers: Computer[]) => this.computers = computers,
      (error: any) => this.error = error
    );
    this.api.getProcessors().subscribe(
      (processors: Processor[]) => this.processors = processors,
      (error: any) => this.error = error
    );
    this.api.getMotherboards().subscribe(
      (motherboards: MotherBoard[]) => this.motherboards = motherboards,
      (error: any) => this.error = error
    );
    this.api.getMemories().subscribe(
      (memories: Memory[]) => this.memories = memories,
      (error: any) => this.error = error
    );
    this.api.getGraphicCards().subscribe(
      (graphiccards: GraphicCard[]) => this.graphiccards = graphiccards,
      (error: any) => this.error = error
    );
    this.api.getUsers().subscribe(
      (users: User[]) => this.users = users,
      (error: any) => this.error = error
    );
  }
}


