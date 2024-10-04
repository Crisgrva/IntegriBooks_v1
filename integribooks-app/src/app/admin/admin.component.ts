import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { LibraryService } from '../library/library.service';
import { debounceTime, distinctUntilChanged, Subject } from 'rxjs';
import { AddBookModalComponent } from './components/add-book-modal/add-book-modal.component';

@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [CommonModule, FormsModule, AddBookModalComponent],
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.css',
})
export class AdminComponent {
  books: any[] = []; // Almacena los libros obtenidos
  searchQuery: string = ''; // Para almacenar el texto de búsqueda
  isLoading = true; // Bandera para manejar el estado de carga
  isAddBookModalOpen: boolean = false;
  selectedBook: { title: string; author: string; cover: string } | null = null;

  private searchSubject = new Subject<string>();

  constructor(private libraryService: LibraryService) {}

  ngOnInit(): void {
    this.getBooks(); // Llamar a la API para obtener libros al cargar el componente

    this.searchSubject
      .pipe(
        debounceTime(500), // Espera 500 ms antes de hacer la búsqueda
        distinctUntilChanged() // Evita búsquedas repetidas si el término no ha cambiado
      )
      .subscribe((query) => {
        this.performSearch(query);
      });
  }

  // Método para abrir el modal
  openAddBookModal() {
    this.isAddBookModalOpen = true;
  }

  closeAddBookModal() {
    this.isAddBookModalOpen = false;
  }

  onBookAdded() {
    this.getBooks();
  }

  deleteBook(bookId: string) {
    const confirmDelete = confirm('Are you sure you want to delete this book?');
    if (confirmDelete) {
      this.libraryService.deleteBook(bookId).subscribe({
        next: () => {
          this.books = this.books.filter((book) => book.id !== bookId);
          alert('Book deleted successfully.');
        },
        error: (error) => {
          console.error('Error deleting book', error);
          alert('An error occurred while deleting the book.');
        },
      });
    }
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

  openEditBookModal(book: { title: string; author: string; cover: string }) {
    this.selectedBook = book;
    this.isAddBookModalOpen = true;
  }
}
