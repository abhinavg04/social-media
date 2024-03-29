from django import forms
from .models import Profile


class UserInfo(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profileimg','phone','state')
        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
        }
