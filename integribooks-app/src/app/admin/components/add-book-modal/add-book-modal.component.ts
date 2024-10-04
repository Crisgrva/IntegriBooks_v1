import { Component, EventEmitter, Output, Input } from '@angular/core';
import { LibraryService } from '../../../library/library.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-add-book-modal',
  templateUrl: './add-book-modal.component.html',
  styleUrls: ['./add-book-modal.component.css'],
  standalone: true,
  imports: [FormsModule, CommonModule],
})
export class AddBookModalComponent {
  @Output() bookAdded = new EventEmitter<void>();
  @Output() modalClosed = new EventEmitter<void>();
  @Input() bookToEdit: { title: string; author: string; cover: string } | null =
    null;

  newBook: { title: string; author: string; cover: string } = {
    title: '',
    author: '',
    cover: '',
  };
  coverPreview: string | null = null;

  constructor(private libraryService: LibraryService) {}

  ngOnChanges() {
    if (this.bookToEdit) {
      this.newBook = { ...this.bookToEdit };
      this.coverPreview = this.newBook.cover;
    }
  }

  saveBook() {
    if (this.bookToEdit) {
      this.libraryService.updateBook(this.newBook).subscribe({
        next: () => {
          this.bookAdded.emit();
          this.closeModal();
        },
        error: (error) => {
          console.error('Error al actualizar el libro', error);
        },
      });
    } else {
      this.libraryService.addBook(this.newBook).subscribe({
        next: () => {
          this.bookAdded.emit();
          this.closeModal();
        },
        error: (error) => {
          console.error('Error al agregar el libro', error);
        },
      });
    }
  }

  closeModal() {
    this.modalClosed.emit();
    this.resetNewBookForm();
  }

  resetNewBookForm() {
    this.newBook = { title: '', author: '', cover: '' };
    this.coverPreview = null;
    this.bookToEdit = null;
  }

  updateCoverPreview() {
    this.coverPreview = this.newBook.cover;
  }
}
