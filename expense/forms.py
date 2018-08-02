from django import forms

from .models import ExpenseModel
class AddNewExpenseForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea())
	expense_time = forms.DateField(widget=forms.DateInput())
	class Meta:
		model = ExpenseModel
		fields = ['payment_method', 'description', 'amount','share', 'expense_time', 'category' ]
	