from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from base.models import *
from .serializer import *

class BaseView(APIView):
    model = None
    model_serializer = None

class GetAllAPIView(BaseView):
    def get(self, request):
        queryset = self.model.objects.all()
        serializer = self.model_serializer(queryset, many=True)
        return Response(serializer.data)

class GetDataFilteredByPk(BaseView):
    def get(self,request,*args, **kwargs):
        queryset = self.model.objects.filter(articleId_id=self.kwargs['pk'])
        serializer = self.model_serializer(queryset, many=True)
        return Response(serializer.data)

class GetAllArticlesView(GetAllAPIView):
    model = Article
    model_serializer = ArticleSerializer

class GetAllParagraphsView(GetAllAPIView):
    model = Paragraph
    model_serializer = ParagraphsSerializer

class GetParagraphsFromArticle(GetDataFilteredByPk):
    model = Paragraph
    model_serializer = ParagraphsSerializer

