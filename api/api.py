from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import Portfolio,Portfolio_Item
import json
# Create your views here.

def create_portfolio(request):
    print("create_portfolio called")  # Debugging statement
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=400)
    
    else:
         
        data = json.loads(request.body)
        portfolio = portfolio.objects.create(
            title=data["title"],
            username=data["username"],
            body=data["body"],
        )

        for item in data["items"]:
            Portfolio_Item.objects.create(
                portfolio=portfolio,
                name=item["name"],
                description=item["description"],
                image_url=item["image_url"]
            )
            Portfolio_Item.save()
            portfolio.append(Portfolio_Item)      
              
        portfolio.save()

        return JsonResponse({"message": "Portfolio created successfully"}, status=201)

def product_grid(request):

    if request.method != "GET":
        return JsonResponse({"error": "Invalid request method"}, status=400)
    
    products = [   
        {"id": 1, "name":"shits and giggles", "img":"assets/example.jpeg"},
        {"id": 2, "name":"forgor bout this", "img":"assets/example.jpeg"},
        {"id": 3, "name":"does not exist" , "img":"assets/example.jpeg"}
    ]

    return JsonResponse(products, safe=False)