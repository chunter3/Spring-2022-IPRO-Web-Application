from django import forms


class UploadTextbookForm(forms.Form):

    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=20)
    isbn = forms.CharField(max_length=13)
    price = forms.DecimalField(max_digits=5, decimal_places=2)



    
        