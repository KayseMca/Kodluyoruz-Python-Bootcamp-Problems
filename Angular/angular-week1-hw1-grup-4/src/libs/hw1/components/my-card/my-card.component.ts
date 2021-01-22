import { Component, Input, OnInit } from '@angular/core';

export interface Card{
  postId: number;
  id:number;
  name: string;
  email: string;
  body: string ;
}
@Component({
  selector: 'app-my-card',
  templateUrl: './my-card.component.html',
  styleUrls: ['./my-card.component.scss']
})
export class MyCardComponent implements OnInit {

  // TODO: define @Input(s) here
  @Input() card:Card

  constructor() { }

  ngOnInit(): void {
    console.log(this.card)
  }
}
