from django.shortcuts import render, redirect
from django.http import HttpResponse


from .forms import AddNewExpenseForm
from .models import ExpenseModel
# Create your views here.

def home(request):
	detail = ExpenseModel.objects.all()
	total=0
	for cost in detail:
		total += cost.amount
	return render(request, 'expense/home.html', {'detail': detail, 'total': total })


def new_expense(request):
	form = AddNewExpenseForm()
	if request.method == 'POST':
		form = AddNewExpenseForm(request.POST)
		form.save()
		return redirect('home')
	return render(request, 'expense/new.html', { 'form': form })