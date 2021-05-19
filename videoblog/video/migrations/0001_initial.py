# Generated by Django 3.1.2 on 2020-12-07 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('videos', models.FileField(upload_to='video/%y')),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]