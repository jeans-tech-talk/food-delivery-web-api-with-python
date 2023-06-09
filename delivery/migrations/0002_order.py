# Generated by Django 4.1.7 on 2023-04-05 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_address', models.TextField()),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Checks', 'Checks'), ('Debit cards', 'Debit cards'), ('Mobile payments', 'Mobile payments'), ('Electronic bank transfers', 'Electronic bank transfer')], max_length=25)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
