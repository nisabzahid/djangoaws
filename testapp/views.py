from django.shortcuts import render
from .forms import MyForm

# Create your views here.
def home(request):

    form = MyForm(request.POST, request.FILES)
    print(form, "hello")
    if request.method == "POST" and form.is_valid():
        form.save()
        print(form, "hello2")
    return render(request, "home.html", {"form": form})