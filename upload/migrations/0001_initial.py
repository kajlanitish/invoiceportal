# Generated by Django 3.0.3 on 2020-11-01 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.PositiveIntegerField(unique=True)),
                ('doc_number', models.PositiveIntegerField()),
                ('type', models.CharField(max_length=255)),
                ('net_due_date', models.DateField()),
                ('doc_date', models.DateField()),
                ('pstng_date', models.DateField()),
                ('amt_in_loc_cur', models.IntegerField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='upload.Vendor')),
            ],
        ),
    ]
