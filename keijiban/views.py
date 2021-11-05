from django.views.generic import TemplateView
import datetime

class BoardPage(TemplateView):
    template_name = "Board.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["sum_thread"] = 11111111111
        ctxt["category"] = {
            "雑談",
            "質問",
            "その他",
        }
        return ctxt


class Thread(TemplateView):
    template_name = "Thread.html"