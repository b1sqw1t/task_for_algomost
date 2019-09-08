from django import forms
from django.core.exceptions import ValidationError

from account.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'age', 'area_of_activity', 'name_of_facebook', 'name_of_instagram')


    def clean(self):
        cleaned_data = self.cleaned_data

        if Profile.objects.filter(first_name=cleaned_data['first_name'],
                                  last_name=cleaned_data['last_name'],
                                  age=cleaned_data['age'],
                                  area_of_activity=cleaned_data['area_of_activity'],
                                  name_of_facebook=cleaned_data['name_of_facebook'],
                                  name_of_instagram=cleaned_data['name_of_instagram'],
                                  email=cleaned_data['email']).exists():
            raise ValidationError('Ошибка. Такая анкета уже существует')
        return cleaned_data

    # def clean(self):
    #     cleaned_data = super().clean()
    #
    #     if Profile.objects.filter(first_name=cleaned_data['first_name'], last_name=cleaned_data['last_name'], email=cleaned_data['email']).exists():
    #         self.add_error(NON_FIELD_ERROR)
    #
    #     return cleaned_data