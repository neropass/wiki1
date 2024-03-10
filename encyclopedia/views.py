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
        return None
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
            result = get_article(request, title)
            if result is None:
                sub = []
                for word in util.list_entries():
                    if title.lower() in word.lower():
                        sub.append(word)
                return render(request, "encyclopedia/results.html", {
                            "entries": sub,
                            "title": title,
                            "form": form
                        })
            else:
                return result
    else:
        form = SearchForm()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": form
    })
