import datetime

from django import forms
from django.contrib import auth

class ArticleAddForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5)
    text = forms.CharField(label='Text')
    tags = forms.CharField(label='Tags', required=False)

    def __init__(self, user=None, *args, **kwargs):
        self._user = user
        forms.Form.__init__(self, *args, **kwargs)

    def save(self):
        article = Question()
        article.title = self.cleaned_data['title']
        article.text = self.cleaned_data['text']
        article.created_at = datetime.datetime.now()
        article.rating = 0
        article.author = Profile.objects.all()[1]
        article.save()

        return article


class AnswerAddForm(forms.Form):
    text = forms.CharField(max_length=255, min_length=3)

    def __init__(self, user=None, *args, **kwargs):
        self._user = user
        forms.Form.__init__(self, *args, **kwargs)

    def save(self):
        answer = Answer()
        answer.text = self.cleaned_data['text']
        answer.created_at = datetime.datetime.now()
        answer.rating = 0
        answer.author = Profile.objects.all()[1]

        answer.question = Question.objects.all()[1]
        answer.save()

        return answer


class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=20, min_length=3)
    email = forms.CharField(max_length=255, min_length=3)
    password = forms.CharField(max_length=20, min_length=4)
    password_repeat = forms.CharField(max_length=20, min_length=4, label='Repeat')

    def clean_password_repeat(self):
        if self.cleaned_data['password'] != self.cleaned_data['password_repeat']:
            raise forms.ValidationError('Passwords are not equal.')

    def save(self):
        user = User.objects.create_user(self.cleaned_data['login'], self.cleaned_data['email'],
                                        self.cleaned_data['password'])

        Profile.objects.create(user=user)


class SignInForm(forms.Form):
    user_name = forms.CharField(label='Email')
    password = forms.CharField(label='Password')

    _user = None

    def clean(self):
        try:
            self._user = auth.authenticate(username=self.cleaned_data['user_name'],
                                           password=self.cleaned_data['password'])
        except:
            raise forms.ValidationError('Invalid login or password')

    def auth(self):
        if not self._user:
            self.clean()
        return self._user
