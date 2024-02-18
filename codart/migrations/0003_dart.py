# Generated by Django 4.1.13 on 2024-02-15 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codart', '0002_profile_date_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=128)),
                ('code_block', models.TextField(max_length=1024)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='darts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
