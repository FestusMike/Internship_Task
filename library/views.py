from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Categories retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Category created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Category retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Category updated successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Category deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Books retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Book created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Book retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Book updated successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Book deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)

class BooksByCategoryView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Book.objects.filter(category=category_id)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data:
            return Response({
                'status': 'success',
                'message': f'Books listed for category ID {kwargs["category_id"]}',
                'data': response.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'error',
                'message': 'No books found for this category',
            }, status=status.HTTP_404_NOT_FOUND)
