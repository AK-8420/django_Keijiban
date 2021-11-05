from django.views.generic import TemplateView
import datetime

class BoardPage(TemplateView):
    template_name = "Board.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["date"] = datetime.date.today()
        return ctxt