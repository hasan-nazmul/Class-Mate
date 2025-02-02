# Generated by Django 5.1.4 on 2025-01-19 06:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ClassroomHandler', '0002_initial'),
        ('ExamHandler', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='answersheet',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_sheet', to='ExamHandler.answersheet'),
        ),
        migrations.AddField(
            model_name='examination',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='ClassroomHandler.classroom'),
        ),
        migrations.AddField(
            model_name='answersheet',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_sheet', to='ExamHandler.examination'),
        ),
        migrations.CreateModel(
            name='Written',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ExamHandler.question')),
                ('answer_sheet', models.FileField(upload_to='exam_answer_documents/')),
            ],
            bases=('ExamHandler.question',),
        ),
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ExamHandler.question')),
                ('options', models.JSONField(blank=True, null=True)),
                ('answer', models.CharField(max_length=10)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mcq_questions', to='ExamHandler.examination')),
            ],
            bases=('ExamHandler.question',),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_answer', to='ExamHandler.mcq'),
        ),
    ]
