# Generated by Django 4.2.16 on 2025-01-27 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('post_code', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_outlet.address'),
        ),
    ]
