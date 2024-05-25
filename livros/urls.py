from django.urls import path,include
from . import views

urlpatterns = [
    path('books/', views.book_list_view), 
    path('books/<int:pk>/',views.book_detail_view),
    path('authors/',views.author_list_view),
    path('authors/<int:pk>',views.author_detail_view),
]
