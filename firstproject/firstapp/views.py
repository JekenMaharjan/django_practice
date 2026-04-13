from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template import loader
from .models import Member
from .forms import ReservationForm

# Create your views here.

# Main Page
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

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

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))

def form(request):
    form = ReservationForm()
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success!")
    
    return render(request, 'index.html', {'form' : form })

