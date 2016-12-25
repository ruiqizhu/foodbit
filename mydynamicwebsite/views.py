from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from backend.models import *
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class HomePage(View):
    def get(self, request):
        # all_foodevents = FoodEvent.objects.all()
        # context = {'all_foodevents': all_foodevents}
        return render(request, 'index.html')

class FoodForm(View):
    def get(self, request):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        all_foodevents = FoodEvent.objects.all()
        context = {'all_foodevents': all_foodevents}
        return render(request, 'foodform.html')

    def post(self, request):
        #from . import firebaseconnect
        title = request.POST.get("title")
        name = request.POST.get("name")
        location = request.POST.get("location")
        time = request.POST.get("time")
        organization = request.POST.get("organization")
        foodtype = request.POST.get("foodtype")
        description = request.POST.get("description")
        if request.POST.get("image") == "":
            image = "http://trichilofoods.com/site/wp-content/uploads/2015/06/veggies.jpg"
        else:
            image = request.POST.get("image")
        print(request.POST.get("image"))
        new_post = FoodEvent(title=title, name=name, location=location, time=time,
             organization=organization, foodtype=foodtype, description=description, image=image
             )
        new_post.save()

        """foodInfo = {
        'title': title,
        'name': name,
        'location': location,
        'time': time,
        'organization': organization
        }
        firebaseconnect.upload(foodInfo)"""
        return HttpResponseRedirect('/foodlist')
        

class FoodList(View):
    def get(self, request):
        context = {}
        context["allFood"] = FoodEvent.objects.all()[::-1]
        return render(request, 'foodlist.html', context)

    def post(self, request):
        id = request.POST.get("id")
        foodevent = FoodEvent.objects.get(id=id)
        foodevent.delete()
        return HttpResponseRedirect('/foodlist')











