from django.shortcuts import render, redirect
from django.contrib import messages
from seller.forms import UploadTextbookForm
from catalogue.models import Textbook


def sellInterface(request):
    
    return render(request, 'seller/interface.html')

def uploadText(request):
    if request.method == 'POST':
        form = UploadTextbookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tb = Textbook(booktitle = cd['title'], author = cd['author'], isbn = cd['isbn'], price = cd['price'])
            tb.save()
            booktitle = cd.get('title')
            messages.success(request, f'{booktitle} successfully uploaded to catalogue!')
            return redirect ('seller')

    else:
        form = UploadTextbookForm()
    return render(request, 'seller/uploadText.html', {'form': form})
