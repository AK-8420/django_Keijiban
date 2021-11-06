from django.views.generic import ListView, DetailView
from .models import Category, Thread, Tag, Post


class Index(ListView):
    model = Thread

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["sum_thread"] = 11111111111
        ctxt["category"] = {
            "雑談",
            "質問",
            "その他",
        }
        return ctxt


class ThreadView(DetailView):
    model = Thread