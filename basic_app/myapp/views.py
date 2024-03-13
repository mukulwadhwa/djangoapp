from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import BankAccount
from .forms import BankAccountForm

# Create your views here.

def user_list(request):
    users = BankAccount.objects.all()
    return render(request, 'user_list.html', {'users': users})

def edit_bank_account(request, account_id):
    account = get_object_or_404(BankAccount, pk=account_id)
    
    if request.method == 'POST':
        form = BankAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            absolute_url = request.build_absolute_uri(reverse('user_list'))
            return redirect(absolute_url)
    else:
        form = BankAccountForm(instance=account)

    return render(request, 'edit_account.html', {'form': form, 'account': account})


def delete_bank_account(request, account_id):
    account = get_object_or_404(BankAccount, pk=account_id)
    if request.method == 'POST':
        account.delete()
        #Reverse function for absolute path
        absolute_url = request.build_absolute_uri(reverse('user_list'))
        return redirect(absolute_url)
        
    return render(request, 'delete_user.html', {'account': account})

    #RedirectView.as_view( url = "http://google.com")

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
