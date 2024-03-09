from django.shortcuts import render
from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label="Search")

from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm()
    })

def get_article(request, title):
    result = util.get_entry(title)
    if result is None:
        return render(request, "encyclopedia/error.html", {
                "title": title,
                "form": SearchForm()
            })
    return render(request, "encyclopedia/article.html", {
            "title": title,
            "entry": markdown2.markdown(result),
            "form": SearchForm()
        })

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["search"]
            return get_article(request, title)
    else:
        form = SearchForm()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": form
    })

