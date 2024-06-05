from django.urls import path,include
from . import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Books Api",
      default_version='v1',
      description="It's an API for books and authors management",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="gabrielpontemello1@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('books/', views.book_list_view), 
    path('books/<int:pk>/',views.book_detail_view),
    path('authors/',views.author_list_view),
    path('authors/<int:pk>',views.author_detail_view),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')

]
