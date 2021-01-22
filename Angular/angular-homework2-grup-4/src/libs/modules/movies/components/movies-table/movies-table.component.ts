import { ThrowStmt } from '@angular/compiler';
import { Component, Input, OnInit, SimpleChanges } from '@angular/core';
import { SearchingPipe } from 'src/libs/_pipe/searching.pipe';

@Component({
  selector: 'app-movies-table',
  templateUrl: './movies-table.component.html',
  styleUrls: ['./movies-table.component.scss'],
  providers:[SearchingPipe]
})
export class MoviesTableComponent implements OnInit {

  dataSource;
  displayedColumns;
  displayedColumnsWithoutPoster;

  private _tableData;
  public get tableData() {
    return this._tableData;
  }
  @Input()
  public set tableData(value) {
    if (!value || value.length == 0) return;
    this._tableData = value;
    this.dataSource = Object.values(value);
    
    this.displayedColumns = Object.keys(this.dataSource[0]);
    this.displayedColumnsWithoutPoster = Object.keys(this.dataSource[0]).filter((columnName) => columnName !== 'poster');
  }


  constructor() { }

  ngOnInit(): void {

  }
    
}


