from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy


class ChoiceForm(forms.Form):
    answer = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': '질문을 입력해주세요.', 'class': 'form-control'}))

    # input(선택)을 반환
    def clean_choiceform(self):
        data = self.cleaned_data['answer']
        if data == '':
            raise ValidationError(ugettext_lazy('미선택'))
        return data