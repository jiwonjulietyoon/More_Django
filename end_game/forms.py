from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.EmailField()  # validator: 이메일 형태로 입력이 들어왔는지 save하기 전에 검사하게 됨.

    class Meta:
        model = Post
        fields = ['title', 'content']
        # fields = '__all__'  => ['title', 'content', 'user_id', ...] 를 의미