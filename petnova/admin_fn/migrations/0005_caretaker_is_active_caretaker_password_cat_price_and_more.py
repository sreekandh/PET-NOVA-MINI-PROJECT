# Generated by Django 5.1 on 2024-10-14 04:24

import admin_fn.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_fn', '0004_caretaker'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='caretaker',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='caretaker',
            name='password',
            field=models.CharField(default='defaultpassword', max_length=128),
        ),
        migrations.AddField(
            model_name='cat',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dog',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='password',
            field=models.CharField(default='defaultpassword', max_length=128),
        ),
        migrations.AlterField(
            model_name='caretaker',
            name='specialization',
            field=models.CharField(choices=[('Pet Sitting', 'Pet Sitting'), ('Pet Grooming', 'Pet Grooming'), ('Dog Walker', 'Dog Walker'), ('Pet Feeder', 'Pet Feeder')], max_length=255),
        ),
        migrations.AlterField(
            model_name='cat',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='cat',
            name='breed',
            field=models.CharField(max_length=100, validators=[admin_fn.models.validate_text]),
        ),
        migrations.AlterField(
            model_name='cat',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='specialization',
            field=models.CharField(choices=[('Service dog training', 'Service dog training'), ('Agility training', 'Agility training'), ('K-9 training', 'K-9 training'), ('Therapy training', 'Therapy training'), ('Obedience training', 'Obedience training'), ('Normal pet training', 'Normal pet training')], max_length=255),
        ),
        migrations.CreateModel(
            name='CaretakerSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('Pet Sitting', 'Pet Sitting'), ('Pet Grooming', 'Pet Grooming'), ('Dog Walker', 'Dog Walker'), ('Pet Feeder', 'Pet Feeder')], max_length=100)),
                ('duration', models.IntegerField(choices=[(1, '1 Day'), (3, '3 Days'), (5, '5 Days'), (7, '7 Days')], default=1)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='caretaker_slots/')),
                ('caretaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caretaker_slots', to='admin_fn.caretaker')),
            ],
        ),
        migrations.CreateModel(
            name='CaretakerSlotBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('duration', models.PositiveIntegerField(help_text='Duration in days')),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('pet_name', models.CharField(max_length=100)),
                ('pet_breed', models.CharField(max_length=100)),
                ('pet_species', models.CharField(max_length=100)),
                ('pet_age', models.PositiveIntegerField()),
                ('pet_image', models.ImageField(blank=True, null=True, upload_to='pet_images/')),
                ('service_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='confirmed', max_length=10)),
                ('caretaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='admin_fn.caretaker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caretaker_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(choices=[(15, '15 Days'), (30, '30 Days'), (45, '45 Days'), (60, '60 Days')], default=15)),
                ('price', models.DecimalField(decimal_places=2, default=3000.0, max_digits=10)),
                ('methods', models.TextField(default='In-Person')),
                ('image', models.ImageField(blank=True, null=True, upload_to='training_slots/')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_slots', to='admin_fn.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='PetTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('owner_email', models.EmailField(max_length=254)),
                ('owner_phone', models.CharField(max_length=15)),
                ('pet_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='pet_images/')),
                ('description', models.TextField()),
                ('breed', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_fn.trainer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('training_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_fn.trainingslot')),
            ],
        ),
    ]