from django.shortcuts import render
from django.http import JsonResponse
from django.views import  View
from  .products import products
from rest_framework.views import APIView
from rest_framework.response import Response
 
class MyRoutes(APIView):
    def get(self,request):
        return Response('Hello')
class ProductsView(APIView):
    def get(self,request,pk):
        product=None
        for i in products:
            if i['_id']==pk:
                product=i
                break
        if pk == "all":
            product = products
        return Response(product)
        

 