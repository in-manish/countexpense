from django.db import models

# Create your models here.

class ExpenseModel(models.Model):
	PAYMENT_METHOD = (
			('CASH', 'CASH_OPTION'),
			('CARD', 'ATM_CARD_OPTION'),
			('WALLET', 'DIGITAL_PAYMENT'),
		)

	payment_method = models.CharField(max_length = 50, choices = PAYMENT_METHOD, default = 'CASH')
	description = models.CharField( max_length = 400)
	amount = models.IntegerField()
	expense_time = models.DateTimeField(blank=True)
	CATEGORY_SPENT_FOR = (
			('FOOD', 'FOOD & DRINK'),
			('FUEL', 'PETROL OR DIESEL'),
			('ENTERTAINMENT', 'ENTERTAINMENT'),
		)
	category = models.CharField(max_length= 50, choices = CATEGORY_SPENT_FOR, default = 'FOOD')