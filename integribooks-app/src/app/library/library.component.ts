import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BookComponent } from './components/book/book.component';
import { LibraryService } from './library.service';
import { Subject } from 'rxjs';
import { debounceTime, distinctUntilChanged } from 'rxjs/operators';

@Component({
  selector: 'app-library',
  standalone: true,
  imports: [FormsModule, CommonModule, BookComponent],
  templateUrl: './library.component.html',
  styleUrl: './library.component.css',
})
export class LibraryComponent {
  books: any[] = [];
  searchQuery: string = '';
  isLoading = true;

  private searchSubject = new Subject<string>();

  constructor(private libraryService: LibraryService) {}

  ngOnInit(): void {
    this.getBooks();

    this.searchSubject
      .pipe(debounceTime(500), distinctUntilChanged())
      .subscribe((query) => {
        this.performSearch(query);
      });
  }

  getBooks(): void {
    this.isLoading = true;
    this.libraryService.getBooks().subscribe({
      next: (books) => {
        this.books = books;
      },
      error: (error) => {
        console.error('Error fetching books', error);
      },
      complete: () => {
        console.log('Completed');
      },
    });
  }

  onSearchInput(query: string): void {
    this.searchSubject.next(query);
  }

  performSearch(query: string): void {
    if (query) {
      this.isLoading = true;
      this.libraryService.searchBooks(query).subscribe({
        next: (data) => {
          this.books = data;
          this.isLoading = false;
        },
        error: (error) => {
          console.error('Error al buscar libros', error);
          this.isLoading = false;
        },
        complete: () => {
          console.log('Búsqueda completada');
        },
      });
    } else {
      this.getBooks();
    }
  }
}
