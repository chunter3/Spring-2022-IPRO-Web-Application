from tkinter import W
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import ReportFraudForm, UserRegisterForm
from users.models import Fraud, WishList


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect ('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def userAcct(request):
    
    return render(request, 'users/home.html')

             
def wishlist(request):

    if request.user.is_authenticated:

        username = request.user.username
        wishlist = WishList.objects.filter(username__contains=username).last()
        
        return render(request, 'users/wishlist.html', {'wishlist': wishlist})

    else:
        messages.error(request, f'This account is not authorized. Returning to login')
        return redirect('login')

def reportFraud(request):

    if request.method == 'POST':
        form = ReportFraudForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            msg = Fraud(username = cd['username'], report = cd['report'])
            msg.save()
            messages.success(request, f'Thank you. We will look into it')
            return redirect ('account')

    else:
        form = ReportFraudForm()
    return render(request, 'users/fraud.html', {'form': form})








 



