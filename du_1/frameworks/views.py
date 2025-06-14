from django.shortcuts import render, get_object_or_404
from .models import Member
from django.http import HttpResponse

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

def get_param(request):
    jmeno = request.GET.get('jmeno', 'Neznámý')
    return HttpResponse(f"Zadané jméno je: {jmeno}")

def category(request):
    kategorie = request.GET.get('kategorie')  # nebo None
    return render(request, 'frameworks/category.html', {'kategorie': kategorie})


def feedback(request):
    if request.method == 'POST':
        jmeno = request.POST.get('jmeno')
        zprava = request.POST.get('zprava')

        print(f"Zpětná vazba od {jmeno}: {zprava}")

        return HttpResponseRedirect('/feedback/?success=1')

    success = request.GET.get('success') == '1'

    return render(request, 'frameworks/feedback.html', {'success': success})