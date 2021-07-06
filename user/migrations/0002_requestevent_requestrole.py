# Generated by Django 3.2.5 on 2021-07-06 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestRole',
            fields=[
                ('requestID', models.AutoField(primary_key=True, serialize=False)),
                ('setAsOrganizer', models.BooleanField(default=False)),
                ('setAsAdministrator', models.BooleanField(default=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='RequestEvent',
            fields=[
                ('requestEventID', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.event')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
