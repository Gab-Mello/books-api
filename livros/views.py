
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


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
    

