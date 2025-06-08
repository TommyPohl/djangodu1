from django.shortcuts import render, get_object_or_404
from .models import Member

def home(request):
    return render(request, 'frameworks/home.html')

def about(request):
    return render(request, 'frameworks/about.html')

def contact(request):
    return render(request, 'frameworks/contact.html')

def members(request):
    members = Member.objects.all()
    return render(request, 'frameworks/members.html', {'members': members})

def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'frameworks/member_detail.html', {'member': member})