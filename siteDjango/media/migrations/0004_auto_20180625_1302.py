# Generated by Django 2.0.5 on 2018-06-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20180623_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='type',
            field=models.CharField(choices=[('M', 'Film'), ('S', 'Serie'), ('E', 'Episode')], max_length=1, verbose_name='Type de Media'),
        ),
    ]
