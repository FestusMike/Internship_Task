from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Book

class TestModels(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_book_creation(self):
        category = Category.objects.create(name="Test Category")
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            number_of_pages=100,
            description="Test Description",
            category=category,
        )
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.category.name, "Test Category")


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_category_list_view(self):
        response = self.client.get(reverse("category-list"))
        self.assertEqual(response.status_code, 200)

    def test_category_create_view(self):
        data = {"name": "Test Category"}
        response = self.client.post(reverse("category-list"), data)
        self.assertEqual(response.status_code, 201)

    def test_book_list_view(self):
        response = self.client.get(reverse("book-list"))
        self.assertEqual(response.status_code, 200)

    def test_book_create_view(self):
        category = Category.objects.create(name="Test Category")
        data = {
            "title": "Test Book",
            "author": "Test Author",
            "number_of_pages": 100,
            "description": "Test Description",
            "category": category.id,
        }
        response = self.client.post(reverse("book-list"), data)
        self.assertEqual(response.status_code, 201)