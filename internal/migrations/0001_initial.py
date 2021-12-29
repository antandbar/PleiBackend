# Generated by Django 3.2 on 2021-12-29 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('discord_gamer', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.person')),
            ],
            options={
                'verbose_name': 'Gamer',
                'verbose_name_plural': 'Gamers',
                'db_table': 'gamer',
            },
        ),
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('id_scholar', models.AutoField(primary_key=True, serialize=False)),
                ('wallet_gamer', models.CharField(blank=True, max_length=64, null=True)),
                ('t_wallet_gamer', models.CharField(blank=True, max_length=15, null=True)),
                ('discord_manager', models.CharField(blank=True, max_length=25, null=True)),
                ('first_name_manager', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name_manager', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date_gamer', models.DateField(blank=True, null=True)),
                ('finish_date_gamer', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('discord_gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internal.gamer')),
            ],
            options={
                'verbose_name': 'Scholar',
                'verbose_name_plural': 'Scholars',
                'db_table': 'scholar',
            },
        ),
    ]