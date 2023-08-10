# Generated by Django 4.2.4 on 2023-08-10 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.ManyToManyField(related_name='users', to='demo.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('batch_num', models.CharField(max_length=20)),
                ('batch_date', models.DateField()),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=10)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_inventory', to='demo.userprofile')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.userprofile')),
            ],
        ),
    ]
