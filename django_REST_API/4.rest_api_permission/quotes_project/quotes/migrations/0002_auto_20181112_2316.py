# Generated by Django 2.1.3 on 2018-11-12 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.QuoteCategory'),
        ),
    ]