from django import forms
from .models import Thread, Post

widget_textarea = forms.Textarea(
    attrs={
        "class": "form-control",
        "rows" : 4,
        "placeholder" : "投稿したい内容を入力してね"
    }
)

widget_textinput = forms.TextInput(
    attrs={
        "class": "form-control",
        "value" : "名無しさん"
    }
)

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


class SearchForm(forms.Form):
    name = forms.CharField(label="ニックネーム", widget=widget_textinput)