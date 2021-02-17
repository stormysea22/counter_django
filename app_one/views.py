from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return redirect("/session")

def session(request):
    num_visit= request.session.get('num_visit', 1)
    request.session['num_visit']= num_visit + 1

    context = {
        'num_visit' : num_visit,
    }
    return render(request, "index.html", context)
    
def destroy_session(request):
    del request.session['num_visit']
    return redirect('/')
