'''
Métodos HTTP Correspondentes
List View:

GET api/users/: Retorna a lista de todos os usuários.
POST api/users/: Cria um novo usuário.
Detail View:

GET api/users/<id>/: Retorna os detalhes de um usuário específico.
PUT api/users/<id>/: Atualiza um usuário específico.
PATCH api/users/<id>/: Atualiza parcialmente um usuário específico.
DELETE api/users/<id>/: Exclui um usuário específico.
'''
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Author
from .serializers import BookSerializer
from rest_framework import status

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

@api_view(['GET','PUT','DELETE'])
def book_detail_view(request,pk):
    ...
    

@api_view(['GET','POST'])
def author_list_view(request):
    ...

@api_view(['GET','PUT','DELETE'])
def author_detail_view(request,pk):
    ...    



