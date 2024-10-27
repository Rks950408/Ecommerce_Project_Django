from django.shortcuts import render
from django.views import View
from .models import Products
from django.db.models import Count

def home(request):
    return render(request, 'app/home.html')

class CategoryView(View):
    def get(self, request, val):
        product=Products.objects.filter(category=val)
        title=Products.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, "app/category.html", locals())


class ProductDetails(View):
    def get(self,request,pk):
        return render(request,"app/productdetails.html",locals())