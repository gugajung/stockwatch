# Generated by Django 2.2 on 2019-06-26 19:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_tickerprices'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickerprices',
            name='date',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tickerprices',
            name='close_price',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tickerprices',
            name='high_price',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tickerprices',
            name='low_price',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tickerprices',
            name='open_price',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]