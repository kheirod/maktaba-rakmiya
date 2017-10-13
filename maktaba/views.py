from django.shortcuts import render


# Create your views here.
def home(request) :
    title = "Welcome "

    context = {

        "templates_titel": title
    }

    return render(request,"home.html",context)

def novels(request) :
    
    return render(request,"Novels.html",{})
    
def Educational(request) :
    
    return render(request,"Educational.html",{})
    