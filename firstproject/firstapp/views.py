from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template import loader
from .models import Member

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")

class HelloEthiopia(View):
    def get(self, request):
        return HttpResponse("Hello Ethiopia")

def my_first(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

# Main Page
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())