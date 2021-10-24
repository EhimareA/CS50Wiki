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


def entry(request, title):
    entries = util.list_entries()
    print(entries)
    if title in entries:
        page = util.get_entry(title)
        print(page)
        html = markdown2.markdown(page)
        print(html)
        content = html
    else:
        content = "<h2>Entry does not exist</h2>"
    return render(request, "encyclopedia/entry.html", {"title": title,
    "content": content})

