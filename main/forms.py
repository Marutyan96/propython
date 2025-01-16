from django import forms
from .models import Article
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # Установка зашифрованного пароля
        if commit:
            user.save()
        return user


from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField


class ArticleForm(forms.ModelForm):
    content = RichTextField(config_name='default')  # Используем RichTextField вместо обычного TextField

    class Meta:
        model = Article  # Замените на вашу модель
        fields = ['title', 'content']
        widgets = {
            'content': CKEditorWidget(),
        }

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']





class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','name']

