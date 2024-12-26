# Generated by Django 3.2 on 2024-12-25 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_purchaseorder_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcurementRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=50, unique=True)),
                ('item_details', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('urgency', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.vendor')),
            ],
        ),
    ]
