from django.shortcuts import render
from django.views.generic import TemplateView
#from bmi.py import BmiCalculator
from .bmi import BmiCalculator
from django.views import View

class HomePageView(TemplateView):
    template_name = 'calculator/calculator.html'
class BmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"calculator/calculator.html",{})
    def post(self,request,*args,**kwargs):
        print("lllllllllll",args)
        print("kkkkkk:",**kwargs)
        print("kkkkkkkkkllmmmmm",request.POST)
        weight=request.POST.get("weight")
        height=request.POST.get("height")
        calc=BmiCalculator()
        bmi=calc.bmi(height,weight)
        category=calc.bmi_description(bmi)
        return render(request,"calculator/calculator.html",{"bmi":bmi,"category":category})


        
        template_name = "calculator/calculator.html"



