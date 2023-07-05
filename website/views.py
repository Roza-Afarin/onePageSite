from django.shortcuts import render

# Create your views here.
def home_index(request):
    return render(request,'index.html')

def kitchensink_index(request):
    return render(request,'kitchensink.html')

def content_index(request):
    return render(request,'content.html')

def pricing_index(request):
    return render(request,'pricing.html')

def register_index(request):
    return render(request,'register.html')

def terms_index(request):
    return render(request,'terms.html')