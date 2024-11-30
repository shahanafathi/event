     
from django.shortcuts import render, redirect,HttpResponse
from .models import Event, EventRegistration

# Home Page with Event List
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# Event Details Page
def event_detail(request, event_id):
    event = Event.objects.filter(id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

# Event Creation (Admin Only)

def create_event(request):
    if request.user.is_superuser:
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            date = request.POST.get("date")
            time = request.POST.get("time")
            location = request.POST.get("location")
            # Save event
            Event.objects.create(
                title=title,
                description=description,
                date=date,
                time=time,
                location=location,
                created_by=request.user,
            )
            return redirect('event_list')
        return render(request, 'events/create_event.html')
    else:
        return redirect('event_list')

# Event Registration

def register_event(request, event_id):
    event = Event.objects.filter(id=event_id)
    if not EventRegistration.objects.filter(user=request.user, event=event).exists():
        EventRegistration.objects.create(user=request.user, event=event)
    return redirect('event_detail', event_id=event.id)
