from django.shortcuts import redirect, render
from .models import BankAccount
from .forms import BankAccountForm

# Create your views here.

def user_list(request):
    users = BankAccount.objects.all()
    return render(request, 'user_list.html', {'users': users})


def create_account(request):
    if request.method == 'POST':
        form = BankAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the page where all users are listed
    else:
        form = BankAccountForm()
    return render(request, 'create_account.html', {'form': form})

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
