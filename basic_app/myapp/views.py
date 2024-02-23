from django.shortcuts import redirect, render


# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact_us(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about.html')
    
# External path
def ExternalPageView(request):
    External_URL = "https://google.com";
    return redirect(External_URL)

#relative path
def RelativePageView(request):
    return redirect("www.google.com")
