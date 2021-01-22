import { Component, OnDestroy, OnInit, SimpleChanges } from '@angular/core';
import { FormControl } from '@angular/forms';
import { combineLatest, of, Subscription } from 'rxjs';
import { debounceTime, startWith } from 'rxjs/operators';
import { IMovie } from '../../models/movie-models';
import { MoviesHttpService } from '../../services/movies-http.service';

@Component({
  selector: 'app-movies-table-container',
  templateUrl: './movies-table-container.component.html',
  styleUrls: ['./movies-table-container.component.scss']
})
export class MoviesTableContainerComponent implements OnInit, OnDestroy {

  movies: IMovie[];
  search:String
  subscriptions: Subscription = new Subscription();

  constructor(private moviesHttpService: MoviesHttpService) { }

  ngOnInit(): void {
    
    // this.moviesHttpService.getTop100Movies().subscribe(data=>{
    //   this.movies = data
    // })
    this.subscriptions.add(
      this.moviesHttpService.getTop100Movies().subscribe(data=>{
        this.movies = data
        console.log(this.movies.length)
      })
    )
    
  }

  ngOnDestroy() {
    this.subscriptions.unsubscribe();
  }

}
