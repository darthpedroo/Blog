from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view(["GET"])
def get_all_articles(request):
    return Response("Me gusta el pene")

