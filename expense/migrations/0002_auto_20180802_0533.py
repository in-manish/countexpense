# Generated by Django 2.0.7 on 2018-08-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensemodel',
            name='share',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expensemodel',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]