from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MealsData
from .serializer import MealsDataSerializer


# Create your views here.

@api_view(["GET","POST","PUT"])
def MealsApi(request):

    mealsData = MealsData.objects.all()
    if request.method == "GET":
      data =   MealsDataSerializer(mealsData,many=True)
      return Response({"Meals":data.data})
    

    elif request.method == "POST":
     requestdata = MealsDataSerializer(data=request.data)

     if requestdata.is_valid():
       requestdata.save()
       return Response(requestdata.data)
     return Response("CreatedSuccesfull")

    elif request.method == "DELETE":
      objectdelete = MealsData.get(id=id)