# Generated by Django 4.0 on 2022-06-07 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0002_remove_leaveapp_user_leaveapp_authuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaveapp',
            name='authuser',
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
