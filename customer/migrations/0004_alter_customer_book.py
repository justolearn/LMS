# Generated by Django 3.2.4 on 2021-07-01 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210629_1918'),
        ('customer', '0003_alter_customer_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='book',
            field=models.ManyToManyField(related_name='books', to='books.Books'),
        ),
    ]
