# Generated by Django 5.1.4 on 2025-01-19 06:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('exam_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('exam_title', models.CharField(max_length=300)),
                ('instructions', models.TextField(max_length=600)),
                ('starting_time', models.DateTimeField()),
                ('ending_time', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('status', models.CharField(default='Upcoming', max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['ending_time', 'starting_time', 'duration'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order', models.IntegerField(null=True)),
                ('question_fullmarks', models.FloatField()),
                ('question', models.TextField(max_length=500)),
                ('question_image', models.ImageField(upload_to='exam_question_images/')),
            ],
        ),
    ]
