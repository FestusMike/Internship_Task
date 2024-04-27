from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Book


class BookCategoryAPITests(APITestCase):

    def test_create_category(self):
        url = reverse('category-list')
        data = {'name': 'Non-Fiction'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get(id=response.data['id']).name, 'Non-Fiction')

    def test_retrieve_category(self):
        category = Category.objects.create(name="Fiction")
        url = reverse('category-detail', args=[category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Fiction')

    def test_create_book(self):
        category = Category.objects.create(name="Fiction")
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'number_of_pages': 100,
            'description': 'New Description',
            'category': category.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_update_book_patch(self):
        category = Category.objects.create(name="Fiction")
        book = Book.objects.create(
            title="Sample Book",
            author="Author Name",
            number_of_pages=123,
            description="Sample Description",
            category=category
        )
        url = reverse('book-detail', args=[book.id])
        new_data = {'title': 'Updated Title'}
        response = self.client.patch(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, 'Updated Title')

    def test_delete_book(self):
        category = Category.objects.create(name="Fiction")
        book = Book.objects.create(
            title="Sample Book",
            author="Author Name",
            number_of_pages=123,
            description="Sample Description",
            category=category
        )
        url = reverse('book-detail', args=[book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books_by_category(self):
        category = Category.objects.create(name="Fiction")
        Book.objects.create(
            title="Sample Book",
            author="Author Name",
            number_of_pages=123,
            description="Sample Description",
            category=category
        )
        url = reverse("books-by-category", args=[category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  
        self.assertEqual(response.data[0]['title'], 'Sample Book')
