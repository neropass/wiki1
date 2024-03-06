from django.shortcuts import render

from . import util
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_article(request, title):
    result = util.get_entry(title)
    if result is None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    return render(request, "encyclopedia/article.html",{
        "title": title,
        "entry": markdown2.markdown(result)
    })