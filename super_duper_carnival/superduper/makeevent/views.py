from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

def make(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            obj = Event()
            obj.name = form.cleaned_data['name']
            obj.date = form.cleaned_data['date']
            obj.class_name = form.cleaned_data['class_name']
            obj.class_letter = form.cleaned_data['class_letter']
            #finally save the object in db
            obj.save()
            if next:
                return redirect(next)
            return redirect("/")
    else:
        form = EventForm(request.GET)
    return render(request, 'makeevent/index.html', context={
        'form': form
    })
