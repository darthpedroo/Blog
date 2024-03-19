from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('articles/',views.AllArticlesView.as_view()),
    path('articles/<str:pk>',views.SingleArticleView.as_view()),
    path('paragraphs/', views.AllParagraphsView.as_view()),
    path('paragraphs/<str:pk>', views.ParagraphsFromArticleView.as_view()),
    path('paragraph/<str:pk>',views.SingleParagraphView.as_view()),
    path('test/', views.AllImagesView.as_view(),)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Para las imagenes