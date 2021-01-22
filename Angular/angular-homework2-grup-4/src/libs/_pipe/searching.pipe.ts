import { Pipe, PipeTransform } from '@angular/core';
import { IMovie } from '../modules/movies/models/movie-models';

@Pipe({
  name: 'searching'
})

// KayseMca
// to filter datasource of the table I create custom pipe

export class SearchingPipe implements PipeTransform {

  transform(Movies:IMovie[], searchValue: string): IMovie[] {
    if(!Movies || !searchValue){
      return Movies
    }
    return Movies.filter(movie=>movie.name.toLowerCase().includes(searchValue.toLowerCase()))
  }

}
