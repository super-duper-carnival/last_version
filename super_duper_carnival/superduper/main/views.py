from django.shortcuts import render
from makeevent.models import Event

def view_events(request):
    data = []
    for i in range(len(Event.objects.all())):
        data.append([Event.objects.all()[i].name, Event.objects.all()[i].date, Event.objects.all()[i].class_name ,Event.objects.all()[i].class_letter])
    return render(request, 'main/index.html', {
        'data': data
    })
