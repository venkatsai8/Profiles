from django.shortcuts import render
from .forms import ProfileForm
from .models import ProfileModel

# Create your views here.
def Home(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request,"index.html",{'form':form, "obj":obj})
        else:
            return render(request, "index.html", {'form':form})
    else:
        form = ProfileForm()
    return render(request, "index.html", {'form':form})
