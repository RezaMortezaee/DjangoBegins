from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord
from . import forms
from first_app.forms import NewuserForm
# from first_app.forms import forms

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request,'first_app/index.html', context=date_dict)

def show_form(request):
    form = forms.FormName()

    if request.method=='POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME:"+form.cleaned_data['name'])
            print("EMAIL:"+form.cleaned_data['email']) 
            print("TEXT:"+form.cleaned_data['text'])    
            print(form.cleaned_data)
    return render(request, 'first_app/form_page.html', {'form':form}) 

def users(request):

    form = NewuserForm() 

    if request.method == "POST":
        form = NewuserForm(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            raise EnvironmentError('Form is invalid')

    return render(request, 'first_app/signup.html', {'form':form})
