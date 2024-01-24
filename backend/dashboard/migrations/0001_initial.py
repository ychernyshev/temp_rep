# Generated by Django 3.2.23 on 2024-01-24 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LetterItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_number', models.CharField(max_length=13)),
                ('is_court', models.BooleanField(default=False)),
                ('is_court_subpoena', models.BooleanField(default=False)),
                ('is_police_subpoena', models.BooleanField(default=False)),
                ('date_of_receipt', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'letter',
                'verbose_name_plural': 'Letters',
            },
        ),
        migrations.CreateModel(
            name='RecipientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'recipient',
                'verbose_name_plural': 'Recipients',
            },
        ),
        migrations.CreateModel(
            name='SenderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'sender',
                'verbose_name_plural': 'Senders',
            },
        ),
        migrations.CreateModel(
            name='LetterCardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.letteritemmodel')),
                ('recipient', models.ManyToManyField(db_index=True, to='dashboard.RecipientModel')),
                ('sender', models.ManyToManyField(db_index=True, to='dashboard.SenderModel')),
            ],
        ),
    ]