from django.shortcuts import render, redirect
import markdown2
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import util

def index(request):
    print(util.list_entries())
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


'''def convert(html):
    html = convert(entry)
    return html'''



def entry(request, title):

    page = util.get_entry(title)
    with open('entry.md', 'r') as f:
        text = f.read()
        html = markdown2.markdown(text)

    with open('entry.html', 'w') as f:
        f.write(html)
        print(html)


