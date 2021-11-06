from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

'''
# ListViewは一覧を簡単に作るためのView
class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = Post

# DetailViewは詳細を簡単に作るためのView
class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    model = Post
    '''

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