from django import forms
from datetimepicker.widgets import DateTimePicker

from .models import ExpenseModel
class AddNewExpenseForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea())
	expense_time = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
	class Meta:
		model = ExpenseModel
		fields = ['payment_method', 'description', 'amount','share', 'expense_time', 'category' ]
	