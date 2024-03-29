from rest_framework import serializers
from base.models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
    
class ParagraphsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
