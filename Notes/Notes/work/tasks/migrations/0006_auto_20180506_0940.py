

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20180506_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Username'),
        ),
    ]
