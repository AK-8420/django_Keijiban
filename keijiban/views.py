from django.views.generic import ListView, DetailView, CreateView
from .models import Thread, Category, Tag, Post
from django import forms
from django.utils import timezone
from ipware import get_client_ip
from .functions import get


class Index(ListView):
    model = Thread
    paginated_by = 10


class CategoryView(DetailView):
    model = Category

    def get_query_set():
        return Category.objects.all().filter(pk = thread__category)


class ThreadView(DetailView):
    model = Thread



class ThreadForm(forms.ModelForm):
   class Meta:
       model = Thread
       fields=(
           'category',
           'title',
           )
       labels ={
           'category':'カテゴリ',
           'title':'タイトル',
       }

class PostForm(forms.ModelForm):
   class Meta:
       model=Post
       fields =(
           'name',
           'body',
           )
       labels= {
           'name':'名前',
           'body':'投稿内容',
       }

class Create(CreateView):
    model = Thread
    form_class = ThreadForm
    form_class2 = PostForm

    def get_context_data(self, **kwargs):
        context= CreateView.get_context_data(self, **kwargs)
        form = self.form_class(self.request.GET or None)
        form2 = self.form_class2(self.request.GET or None)
        context.update({'form':form})
        context.update({'form2':form2})
        return context

    def form_valid(self, form):
        t = form.save()
        # IPアドレスの取得　参考：https://qiita.com/3244/items/0b47d3ad91968fe15eb9
        client_addr, is_routable = get_client_ip(self.request, request_header_order=['X_FORWARDED_FOR', 'REMOTE_ADDR'])
        Post.objects.create(
            IPaddress = client_addr,
            ipID = get.hacshing(client_addr),
            created = timezone.now(),
            name = form.data.get('name'),
            body = form.data.get('body'),
            thread=t,
            )
        return CreateView.form_valid(self, form)