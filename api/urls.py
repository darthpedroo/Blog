from django.urls import path
from . import views

urlpatterns = [
    #path('articles/', views.GetAllArticlesView.as_view()),
    #path('paragraphs/', views.GetAllParagraphsView.as_view()),
   # path('paragraph/<str:pk>', views.GetParagraphsFromArticle.as_view()),
  #  path('test/', views.Article.as_view()),
    path('articles/',views.AllArticlesView.as_view()),
    path('articles/<str:pk>',views.SingleArticleView.as_view()),
    path('paragraphs/', views.AllParagraphsView.as_view()),
    path('paragraphs/<str:pk>', views.ParagraphsFromArticleView.as_view()),
    path('paragraph/<str:pk>',views.SingleParagraphView.as_view()),
]