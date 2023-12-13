from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add(request):
    if request.method == 'POST':
        post = forms.CategoryForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('add_category')
    else:
        post =forms.CategoryForm()
    return render(request,'add_category.html',{'form':post})
    