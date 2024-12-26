# Generated by Django 5.1.4 on 2024-12-26 09:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ClassroomHandler', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teaching', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enrollments',
            name='enrolled_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled', to='ClassroomHandler.classroom'),
        ),
        migrations.AddField(
            model_name='enrollments',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enrolled',
            name='enrolled_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled', to='ClassroomHandler.enrollments'),
        ),
        migrations.AddField(
            model_name='teaching',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teaching',
            name='teaching_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teaching', to='ClassroomHandler.classroom'),
        ),
        migrations.AlterUniqueTogether(
            name='enrollments',
            unique_together={('enrolled_class', 'student')},
        ),
        migrations.AlterUniqueTogether(
            name='teaching',
            unique_together={('teaching_class', 'teacher')},
        ),
    ]
