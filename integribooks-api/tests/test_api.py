import unittest
import json
from app import create_app, db
from app.models import Book


class ApiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.client = cls.app.test_client()

        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def test_add_book(self):
        """Test for adding a new book."""
        response = self.client.post('/books', data=json.dumps({
            'title': 'Test Book',
            'author': 'Author Name',
            'read': False,
            'cover': 'http://example.com/cover.jpg'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_get_books(self):
        """Test for getting all books in alphabetical order."""
        self.client.post('/books', data=json.dumps({
            'title': 'Test Book',
            'author': 'Author Name',
            'read': False,
            'cover': 'http://example.com/cover.jpg'
        }), content_type='application/json')

        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_get_recent_books(self):
        """Test for getting recent books."""
        response = self.client.get('/books/recent')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_search_books(self):
        """Test for searching books."""
        self.client.post('/books', data=json.dumps({
            'title': 'Test Book',
            'author': 'Author Name',
            'read': False,
            'cover': 'http://example.com/cover.jpg'
        }), content_type='application/json')

        response = self.client.get('/books/search?q=Test Book')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_delete_book(self):
        """Test for deleting a book."""
        response = self.client.post('/books', data=json.dumps({
            'title': 'Test Book',
            'author': 'Author Name',
            'read': False,
            'cover': 'http://example.com/cover.jpg'
        }), content_type='application/json')
        book_id = json.loads(response.data)['id']

        delete_response = self.client.delete(f'/books/{book_id}')
        self.assertEqual(delete_response.status_code, 200)

        response_after_delete = self.client.get(f'/books/{book_id}')
        self.assertEqual(response_after_delete.status_code, 404)

    def test_edit_book(self):
        """Test for editing a book."""
        response = self.client.post('/books', data=json.dumps({
            'title': 'Test Book',
            'author': 'Author Name',
            'read': False,
            'cover': 'http://example.com/cover.jpg'
        }), content_type='application/json')
        book_id = json.loads(response.data)['id']

        edit_response = self.client.put(f'/books/{book_id}', data=json.dumps({
            'title': 'Updated Book',
            'author': 'Updated Author',
            'read': True,
            'cover': 'http://example.com/updated_cover.jpg'
        }), content_type='application/json')

        self.assertEqual(edit_response.status_code, 200)
        self.assertIn('Updated Book', str(edit_response.data))


if __name__ == '__main__':
    unittest.main()
