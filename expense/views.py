from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime


from .forms import AddNewExpenseForm
from .models import ExpenseModel
# Create your views here.

def home(request):
	detail = ExpenseModel.objects.all()
	total=0
	for cost in detail:
		total += cost.amount
	if request.method == 'POST':
		start_date = datetime.date(int(request.POST['from-date'].split('-')[0]), 
			int(request.POST['from-date'].split('-')[1]), int(request.POST['from-date'].split('-')[2]))
		end_date = datetime.date(int(request.POST['to-date'].split('-')[0]), 
			int(request.POST['to-date'].split('-')[1]), int(request.POST['to-date'].split('-')[2]))
		detail = ExpenseModel.objects.filter(expense_time__range=(start_date, end_date))
		start_date = request.POST['from-date']
		end_date = request.POST['to-date']
		selected_spent = 0
		for x in detail:
			selected_spent += x.amount
		context = {
			'detail': detail,
			'total': total, 
			'selected_spent':selected_spent,
			'start_date': start_date,
			'to_date':end_date,
		 }
		return render(request, 'expense/home.html', context)
	return render(request, 'expense/home.html', {'detail': detail, 'total': total })


def new_expense(request):
	form = AddNewExpenseForm()
	if request.method == 'POST':
		form = AddNewExpenseForm(request.POST)
		form.save()
		return redirect('home')
	return render(request, 'expense/new.html', { 'form': form })