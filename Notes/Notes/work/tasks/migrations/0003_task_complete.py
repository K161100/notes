

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.IntegerField(default=0),
        ),
    ]
