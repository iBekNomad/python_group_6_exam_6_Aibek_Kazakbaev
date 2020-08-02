from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.db.models import Q

from webapp.models import GuestBook
from .forms import GuestBookForm


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = GuestBook.objects.all()
    else:
        data = GuestBook.objects.filter(status='active')
    return render(request, 'index.html', context={
        'guestbooks': data
    })


def guestbook_view(request, pk):
    guestbook = get_object_or_404(GuestBook, pk=pk)
    context = {'guestbook': guestbook}
    return render(request, 'guestbook_view.html', context)


def guestbook_create_view(request):
    if request.method == "GET":
        form = GuestBookForm()
        return render(request, 'guestbook_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            GuestBook.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('index')
        else:
            return render(request, 'guestbook_create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def guestbook_update_view(request, pk):
    guestbook = get_object_or_404(GuestBook, pk=pk)
    if request.method == "GET":
        form = GuestBookForm(initial={
            'name': guestbook.name,
            'email': guestbook.email,
            'text': guestbook.text
        })
        return render(request, 'guestbook_update.html', context={
            'form': form,
            'guestbook': guestbook
        })
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            guestbook.name = form.cleaned_data['name']
            guestbook.email = form.cleaned_data['email']
            guestbook.text = form.cleaned_data['text']
            guestbook.save()
            return redirect('index')
        else:
            return render(request, 'guestbook_update.html', context={
                'guestbook': guestbook,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def guestbook_delete_view(request, pk):
    guestbook = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'guestbook_delete.html', context={'guestbook': guestbook})
    elif request.method == 'POST':
        guestbook.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def guestbook_search_view(request):
    query = request.GET.get('q')
    guest_object = GuestBook.objects.filter(
        Q(name__icontains=query)
    )
    context = {'guest_object': guest_object}
    return render(request, 'guestbook_view.html', context)
