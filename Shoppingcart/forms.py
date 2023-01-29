from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['readonly'] = True

    class Meta:
        model = Payment
        fields = ['credit_card_number', 'expiry_date', 'amount']
        widgets = {
            'myuser': forms.HiddenInput(),
        }