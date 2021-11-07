from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Thread, Category, Tag, Post
from django.utils import timezone
from ipware import get_client_ip
from .functions import get
from .forms import ThreadForm, PostForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


class Index(ListView):
    model = Thread
    paginated_by = 10


class CategoryView(DetailView):
    model = Category

    def get_query_set():
        return Category.objects.all().filter(pk = thread__category)


class ThreadView(UpdateView):
    template_name = 'keijiban/thread.html'
    model = Thread
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        form = self.form_class(self.request.GET or None)
        context.update({'form':form})
        return context

    def form_valid(self, form):
        t = form.save()
        # IPアドレスの取得　参考：https://qiita.com/3244/items/0b47d3ad91968fe15eb9
        client_addr, is_routable = get_client_ip(self.request, request_header_order=['X_FORWARDED_FOR', 'REMOTE_ADDR'])
        Post.objects.create(
            IPaddress = client_addr,
            ipID = get.hashing(client_addr),
            created = timezone.now(),
            name = form.data.get('name'),
            body = form.data.get('body'),
            thread=t,
            )
        return redirect('/threads/' + str(self.object.pk))

    def get_absolute_url(self):
        return reverse_lazy("thread", args=[self.object.pk])


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
            ipID = get.hashing(client_addr),
            created = timezone.now(),
            name = form.data.get('name'),
            body = form.data.get('body'),
            thread=t,
            )
        return CreateView.form_valid(self, form)

    def get_absolute_url(self):
        return reverse_lazy("thread", args=[self.object.pk])