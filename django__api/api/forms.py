from django.forms import ModelForm
from app.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('age', 'gender', 'bio')

