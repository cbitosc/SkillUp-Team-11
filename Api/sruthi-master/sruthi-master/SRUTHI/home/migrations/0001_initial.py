# Generated by Django 3.0.7 on 2020-06-22 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_event_registrations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('Rollno', models.IntegerField()),
                ('Branch', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('mobile_no', models.IntegerField()),
                ('email_id', models.CharField(max_length=40)),
                ('event_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_head_name', models.CharField(max_length=10)),
                ('event_head_year', models.IntegerField()),
                ('event_desc', models.CharField(max_length=400)),
                ('email_id', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='events_interested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]