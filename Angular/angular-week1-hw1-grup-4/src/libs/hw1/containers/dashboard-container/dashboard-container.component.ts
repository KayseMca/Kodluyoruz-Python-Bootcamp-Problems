import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { title } from 'process';
import { ElementAst } from '@angular/compiler';
import { stringify } from '@angular/compiler/src/util';

@Component({
  selector: 'app-dashboard-container',
  templateUrl: './dashboard-container.component.html',
  styleUrls: ['./dashboard-container.component.scss']
})
export class DashboardContainerComponent implements OnInit {
  cards: { title: string, body: string }[];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    //Loading posts from jsonplaceholder.typicode
    this.http.get("https://jsonplaceholder.typicode.com/comments").subscribe((comments: any) => {
      console.log(comments) // See incoming data in the browser console and remove this log
      // TODO: set cards array with valid objects
      // this.cards = comments. ... map? reduce? filter?
      this.cards = comments.map((data)=>{
        // console.log(data)
        return {
            ['title']:data['name'],
            ['body']:data['body']
          }
        
      })

    })
  }

}
