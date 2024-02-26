from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from base.models import *
from .serializer import *
from rest_framework import status
from abc import ABC, abstractmethod

class ModelBuilder():
    def __init__(self,model,model_serializer):
        self.model = model
        self.model_serializer = model_serializer


class GetDataStrategy(ABC):
    @abstractmethod
    def get(self,request):
        pass

class GetAllData(ModelBuilder, GetDataStrategy):

    def get(self,request):
        queryset = self.model.objects.all() #self.model = la clase (digamos Article) de BaseView. self.model.model la 
        serializer = self.model_serializer(queryset, many=True)
        return Response(serializer.data)
        
class GetDataFilteredByPk(GetDataStrategy):
    def get(self,request,*args, **kwargs):
        queryset = self.model.objects.filter(articleId_id=self.kwargs['pk'])
        serializer = self.model_serializer(queryset, many=True)
        return Response(serializer.data)

class ArticleView(APIView):
    model = Article
    model_serializer = ArticleSerializer

    get_strategy = GetAllData(model,model_serializer)

    def get(self,request):
        return self.get_strategy.get(request)


