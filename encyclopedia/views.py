from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_article(request, title):
    return render(request, "encyclopedia/article.html",{
        "title": title,
        "entry": util.get_entry(title)
    })