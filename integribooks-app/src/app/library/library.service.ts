import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class LibraryService {
  private apiUrl = 'http://127.0.0.1:5001/books'; // Reemplaza con la URL de tu API

  constructor(private http: HttpClient) {}

  getMostRecentBooks(): Observable<any> {
    return this.http.get(`${this.apiUrl}/recent`);
  }

  getBooks(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}`);
  }

  searchBooks(query: string): Observable<any[]> {
    const searchUrl = `${this.apiUrl}/search?q=${query}`; // Ajusta la URL según tu API
    return this.http.get<any[]>(searchUrl);
  }

  updateBook(book: any) {
    const newbook = {
      author: book.author,
      cover: book.cover,
      read: book.read,
      title: book.title,
    };
    const searchUrl = `${this.apiUrl}/${book.id}`;
    return this.http.put<any[]>(searchUrl, newbook);
  }
  addBook(book: any) {
    const searchUrl = `${this.apiUrl}`;
    return this.http.post<any[]>(searchUrl, book);
  }

  deleteBook(bookId: string): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${bookId}`);
  }
}
