from django import forms
from formApp.models import User
from django.core import validators


# def check_begin_a(value):
#     if value[0].lower()!='a':
#         raise forms.ValidationError("Must begin with the letter a/A")

class FormModel(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class FormName(forms.Form):
    # name = forms.CharField(validators=[check_begin_a])
    name = forms.CharField()
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label="Enter email again")
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verifyEmail']
        if email != verify_email:
            raise forms.ValidationError("Emails Do Not Match")

    # def clean_bot_catcher(self):
    #     bot_catcher=self.cleaned_data['bot_catcher']
    #     if len(bot_catcher)>0:
    #         raise forms.ValidationError("BYE BYE BOT!")
    #     return bot_catcher
