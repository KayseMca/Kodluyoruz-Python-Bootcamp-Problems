import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, filter } from 'rxjs/operators';
import { IMovie } from '../models/movie-models';
import { Observable, of } from 'rxjs';
// import { map } from 'rxjs/operator';

@Injectable({
  providedIn: 'root'
})
export class MoviesHttpService {

  constructor(private http: HttpClient) { }

  getTop100Movies(): Observable<any> {
    // TODO:
    // There are 250 movies in the dataset (top250movies.json)
    // This method should return an Observable that emits the first 100 movies (indexes from 1 to 100)
    return this.http.get<any>('/assets/top250movies.json').pipe(
      map(res=> res.filter(data=>{
        return data['index']<=100
      }))
    )
  }
}
