from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Thread, Tag, Post
from django import forms


class Index(ListView):
    model = Thread

#    def get_queryset(self):
#        return Thread.object.filter()


class ThreadView(DetailView):
    model = Thread


class ThreadForm(forms.ModelForm):
   class Meta:
       model = Thread
       fields=(
           'category',
           'title',
           )
       labels = [
           {'category':'カテゴリー'},
           {'title':'タイトル'},
           ]

class PostForm(forms.ModelForm):
   class Meta:
       model=Post
       fields =(
           'name',
           'body',
           )
       labels= [
           {'name':'名前'},
           {'body':'本文'},
           ]

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
        # form.cleaned_dataにフォームの入力内容が入っています
       data = form.cleaned_data
       text = data["text"]
       search = data["search"]
       replace = data["replace"]

       # ここで変換
       new_text = text.replace(search, replace)

       # テンプレートに渡す
       ctxt = self.get_context_data(new_text=new_text, form=form)
       return self.render_to_response(ctxt)