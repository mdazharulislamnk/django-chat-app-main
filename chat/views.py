from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Message

def home(request):
    # Renders the form where the user enters room_name and username
    return render(request, 'home.html')

def checkview(request):
    # Handles the home form submit: create/get room and carry username to room via querystring
    if request.method == 'POST':
        room_name = request.POST.get('room_name', '').strip()
        username = request.POST.get('username', 'Anonymous').strip() or 'Anonymous'
        if not room_name:
            return redirect('home')
        room, _ = Room.objects.get_or_create(name=room_name)
        return redirect(f"/room/{room.name}/?username={username}")
    return redirect('home')

def room(request, name):
    # Shows messages and injects username so the hidden field is populated (no Anonymous)
    room = get_object_or_404(Room, name=name)
    messages = room.messages.order_by('created_at')
    username = request.GET.get('username', 'Anonymous').strip() or 'Anonymous'
    ctx = {
        'room': room.name,
        'room_details': room,
        'username': username,
        'messages': messages,
    }
    return render(request, 'room.html', ctx)

def get_messages(request, room):
    # Returns messages for AJAX polling in room.html
    room_obj = get_object_or_404(Room, name=room)
    data = [
        {'user': m.author, 'value': m.content, 'date': m.created_at.strftime('%Y-%m-%d %H:%M')}
        for m in room_obj.messages.order_by('created_at')
    ]
    return JsonResponse({'messages': data})

def send(request):
    # Saves a new message posted via AJAX; uses provided username
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        username = request.POST.get('username', 'Anonymous').strip() or 'Anonymous'
        content = request.POST.get('message', '').strip()
        if room_id and content:
            room = get_object_or_404(Room, pk=room_id)
            Message.objects.create(room=room, author=username, content=content)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'invalid'}, status=400)
