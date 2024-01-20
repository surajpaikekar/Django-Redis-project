from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe

# Create your views here.
def home(request):
    return HttpResponse('home page')

def recipe(request):
    if request.method == 'POST':
        data = request.POST

        recipe_name = data.get('recipe_name')
        description = data.get('description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=description,
            recipe_image=recipe_image
        )
        return redirect('/recipes/')
    return render(request, 'recipe.html')