from django.shortcuts import render
from .api import get_category_articles


def index(request):
    return render(request, "index.html")


def _render_category(request, category: str):
    try:
        articles = get_category_articles(category=category, country="us")
    except Exception as e:
        return render(
            request,
            "news.html",
            {"articles": [], "error": f"{type(e).__name__}: {e}", "category": category},
        )

    normalized = []
    for a in articles:
        normalized.append(
            {
                "title": a.get("title") or "Untitled",
                "description": a.get("description") or "No description available.",
                "image": a.get("urlToImage") or "",
                "url": a.get("url") or "#",
                "author": a.get("author") or "Unknown",
                "published_at": a.get("publishedAt") or "",
            }
        )

    return render(
        request,
        "news.html",
        {"articles": normalized, "error": "", "category": category},
    )


def business(request):
    return _render_category(request, "business")


def health(request):
    return _render_category(request, "health")


def science(request):
    return _render_category(request, "science")


def technology(request):
    return _render_category(request, "technology")


def general(request):
    return _render_category(request, "general")


def entertainment(request):
    return _render_category(request, "entertainment")


def sports(request):
    return _render_category(request, "sports")
