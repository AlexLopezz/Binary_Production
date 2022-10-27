# Generated by Django 4.1.1 on 2022-10-27 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checking_in', '0002_alter_order_options_invoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Method_Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='method_pay',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='checking_in.method_pay'),
            preserve_default=False,
        ),
    ]
