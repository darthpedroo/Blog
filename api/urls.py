from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.GetAllArticlesView.as_view()),
    path('paragraphs/', views.GetAllParagraphsView.as_view()),
    path('paragraphs/<str:pk>', views.GetParagraphsFromArticle.as_view())
    
]