
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a list of all Book instances",
    responses={200: BookSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new Book instance",
    request_body=BookSerializer,
    responses={201: BookSerializer, 400: 'Bad Request'}
)
@api_view(['GET','POST'])
def book_list_view(request):
    if request.method == 'GET':
        
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a specific Book instance",
    responses={200: BookSerializer(many=False)}
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a specific Book instance",
    request_body=BookSerializer,
    responses={200: BookSerializer, 400: 'Bad Request'}
)
@swagger_auto_schema(
    method='patch',
    operation_description="Partially update a specific Book instance",
    request_body=BookSerializer,
    responses={200: BookSerializer, 400: 'Bad Request'}
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a specific Book instance",
    responses={204: 'No Content', 404: 'Not Found'}
)
@api_view(['GET','PUT','DELETE','PATCH'])
def book_detail_view(request,pk):
    try:
        item = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        serializer = BookSerializer(item)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'PATCH':
        serializer = BookSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a list of all Author instances",
    responses={200: BookSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new Author instance",
    request_body=BookSerializer,
    responses={201: BookSerializer, 400: 'Bad Request'}
)
@api_view(['GET','POST'])
def author_list_view(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve an specific Author instance",
    responses={200: BookSerializer(many=False)}
)
@swagger_auto_schema(
    method='put',
    operation_description="Update an specific Author instance",
    request_body=BookSerializer,
    responses={200: BookSerializer, 400: 'Bad Request'}
)
@swagger_auto_schema(
    method='patch',
    operation_description="Partially update an specific Author instance",
    request_body=BookSerializer,
    responses={200: BookSerializer, 400: 'Bad Request'}
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete an specific Author instance",
    responses={204: 'No Content', 404: 'Not Found'}
)
@api_view(['GET','PUT','DELETE','PATCH'])
def author_detail_view(request,pk):
    try:
        item = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        serializer = AuthorSerializer(item)
        return Response(serializer.data)
        
    if request.method == 'PUT':
        serializer = AuthorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    if request.method == 'PATCH':
        serializer = AuthorSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

