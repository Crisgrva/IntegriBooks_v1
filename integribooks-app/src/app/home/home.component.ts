import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { BookComponent } from '../library/components/book/book.component';
import { LibraryService } from '../library/library.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterModule, BookComponent, CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
  host: { class: 'w-full flex-1' },
})
export class HomeComponent {
  mostRecentBooks: any[] = [];
  isLoading = true;

  constructor(private libraryService: LibraryService) {}

  ngOnInit(): void {
    this.libraryService.getMostRecentBooks().subscribe(
      (data) => {
        this.mostRecentBooks = data;
        this.isLoading = false;
      },
      (error) => {
        console.error('Error al obtener los libros más recientes', error);
        this.isLoading = false;
      }
    );
  }
}
