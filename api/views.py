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

#Get Data
class GetDataStrategy(ABC):
    @abstractmethod
    def get(self,request):
        pass

class GetAllData(ModelBuilder, GetDataStrategy):

    def get(self,request):
        queryset = self.model.objects.all() #self.model = la clase (digamos Article) de BaseView. self.model.model la 
        serializer = self.model_serializer(queryset, many=True)
        return Response(serializer.data)
        
class GetDataFilteredByPk(ModelBuilder, GetDataStrategy):
    def get(self,filter_field,request,*args, **kwargs):
        queryset = self.model.objects.filter(**{filter_field: kwargs['pk']})
        serializer = self.model_serializer(queryset, many=True)
        return Response(serializer.data)

#Post Data
class PostDataStrategy(ABC):
    @abstractmethod
    def post(self,request):
        pass

class PostData(ModelBuilder, PostDataStrategy):
    def post(self,request):
        serializer = self.model_serializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Put Data
    
class PutDataStrategy(ABC):
    @abstractmethod
    def put(self, request):
        pass

class PutData(ModelBuilder, PutDataStrategy):
    def put(self,request,*args, **kwargs):
        data = request.data
        view_object_instance = self.model.objects.get(id=kwargs['pk'])
        serializer = self.model_serializer(instance=view_object_instance, data = data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

#Delete Data

class DeleteDataStrategy(ABC):
    @abstractmethod
    def delete():
        pass

class DeleteData(ModelBuilder, DeleteDataStrategy):
    def delete(self, request,*args, **kwargs):
        queryset = self.model.objects.get(id=kwargs['pk'])
        queryset.delete()
        return Response("Matateeee")    

#View Handler

class ViewHandler(APIView):
    model = None
    model_serializer = None
    strategy_get_method = None
    strategy_post_method = None
    strategy_put_method = None
    strategy_delete_method = None

    def perform_post_data_strategy(self,request):
        return self.get_post_strategy().post(request)

    def perform_get_data_strategy(self,request,*args, **kwargs):        
        return self.get_get_strategy().get(request,*args, **kwargs)
    
    def perform_put_data_strategy(self,request,*args, **kwargs):
        return self.get_put_strategy().put(request,*args, **kwargs)
    
    def perform_delete_data_strategy(self,request,*args,**kwargs):
        return self.get_delete_strategy().delete(request,*args,**kwargs)
    
    #Getters

    def get_model(self):
        return self.model
    
    def get_model_serializer(self):
        return self.model_serializer
    
    def get_get_strategy(self):
        return self.strategy_get_method(self.get_model(), self.get_model_serializer())
    
    def get_post_strategy(self):
        return self.strategy_post_method(self.get_model(),self.get_model_serializer())
    
    def get_put_strategy(self):
        return self.strategy_put_method(self.get_model(), self.get_model_serializer())
    
    def get_delete_strategy(self):
        return self.strategy_delete_method(self.get_model(), self.get_model_serializer())
    
#Article Classes

class ArticleView(ViewHandler):
    model = Article
    model_serializer = ArticleSerializer
    
class AllArticlesView(ArticleView):
    strategy_get_method = GetAllData
    strategy_post_method = PostData

    def get(self, request, *args, **kwargs):
        return self.perform_get_data_strategy(request, *args, **kwargs)
    
    def post(self,request):
        return self.perform_post_data_strategy(request)

class SingleArticleView(ArticleView):
    strategy_get_method = GetDataFilteredByPk
    strategy_put_method = PutData
    strategy_delete_method = DeleteData
    filter_field = "id"
    def get(self, request, *args, **kwargs):
        return self.perform_get_data_strategy(self.filter_field,request, *args, **kwargs) #In summary, the reason your code works without error is because the arguments passed to perform_get_data_strategy match the expected method signatures of GetAllData.get and GetDataFilteredByPk.get appropriately.

    def put(self,request, *args, **kwargs):
        return self.perform_put_data_strategy(request,*args, **kwargs)
    
    def delete(self,request, *args, **kwargs):
        return self.perform_delete_data_strategy(request,*args,**kwargs)
    
#Paragraph Classes

class ParagraphView(ViewHandler):
    model = Paragraph
    model_serializer = ParagraphsSerializer

class AllParagraphsView(ParagraphView):
    strategy_get_method = GetAllData
    strategy_post_method = PostData
    def get(self, request, *args, **kwargs):
        return self.perform_get_data_strategy(request, *args, **kwargs)
    
    def post(self,request):
        return self.perform_post_data_strategy(request)

class ParagraphsFromArticleView(ParagraphView):
    strategy_get_method = GetDataFilteredByPk
    filter_field = "articleId_id"
    def get(self, request, *args, **kwargs):
        return self.perform_get_data_strategy(self.filter_field,request, *args, **kwargs)

class SingleParagraphView(ParagraphView):
    strategy_get_method = GetDataFilteredByPk
    strategy_put_method = PutData
    strategy_delete_method = DeleteData
    filter_field = "id"
    
    def get(self, request, *args, **kwargs):
        return self.perform_get_data_strategy(self.filter_field,request, *args, **kwargs)
    
    def put(self,request, *args, **kwargs):
        return self.perform_put_data_strategy(request,*args, **kwargs)

    def delete(self,request, *args, **kwargs):
        return self.perform_delete_data_strategy(request,*args,**kwargs)

class ImageView(ViewHandler):
    model = Image
    model_serializer = ImageSerializer

class AllImagesView(ImageView):
    strategy_get_method = GetAllData
    strategy_post_method = PostData

    def get(self, request, *args, **kwargs):
        return self.perform_get_data_strategy(request, *args, **kwargs)
    
    def post(self,request):
        return self.perform_post_data_strategy(request)

