from django.forms import ModelForm, FileInput, ImageField

from application.models import Images


class UploadImageForm(ModelForm):
    class Meta:
        model = Images
        fields = '__all__'
