# Generated by Django 2.0 on 2018-09-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0021_drop_course_similarity_graph_saving'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskerror',
            name='namespace',
            field=models.CharField(default='-empty-', max_length=200),
        ),
    ]
