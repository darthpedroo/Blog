from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from base.models import *
from .serializer import *


class GetAll:
    def __init__(self, model, modelSerializer):
        self.model = model.objects.all()
        self.modelSerializer = modelSerializer(self.model, many=True)
    
    def return_view(self):
        return Response(self.modelSerializer.data)

@api_view(["GET"])
def get_all_articles(request):
    articles = GetAll(Article,ArticleSerializer)
    return articles.return_view()

@api_view(["GET"])
def get_all_paragraphs(request):
    paragraphs = GetAll(Paragraph, ParagraphsSerializer)
    return paragraphs.return_view()


@api_view(["GET"])
def get_all_paragraphs_from_article(request,article_pk):
    
    paragraphs = Paragraph.objects.filter(articleId_id=article_pk)
    serializer = ParagraphsSerializer(paragraphs, many=True)
    
    return Response(serializer.data)