from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils.timezone import make_naive

from webapp.models import GuestBook
from .forms import GuestBookForm, BROWSER_DATETIME_FORMAT


def index_view(request):
    data = GuestBook.objects.all()
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
            guestbook = GuestBook.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
                status=form.cleaned_data['status'],
                created_at=form.cleaned_data['created_at']
            )
            return redirect('guestbook_view', pk=guestbook.pk)
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
            'text': guestbook.text,
            'status': guestbook.status,
            'created_at': make_naive(guestbook.created_at).strftime(BROWSER_DATETIME_FORMAT)
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
            guestbook.status = form.cleaned_data['status']
            guestbook.created_at = form.cleaned_data['created_at']
            guestbook.save()
            return redirect('guestbook_view', pk=guestbook.pk)
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
