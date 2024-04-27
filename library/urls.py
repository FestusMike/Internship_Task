from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDeleteView,
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
    BooksByCategoryView,
)

urlpatterns = [
    path("categories", CategoryListCreateView.as_view(), name="category-list"),
    path(
        "categories/<uuid:pk>",
        CategoryRetrieveUpdateDeleteView.as_view(),
        name="category-detail",
    ),
    path("books", BookListCreateView.as_view(), name="book-list"),
    path(
        "books/<uuid:pk>", BookRetrieveUpdateDestroyView.as_view(), name="book-detail"
    ),
    path(
        "categories/<uuid:category_id>/books",
        BooksByCategoryView.as_view(),
        name="books-by-category",
    ),
]
