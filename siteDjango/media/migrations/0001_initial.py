# Generated by Django 2.0.5 on 2018-06-23 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name="Numéro de l'épisode")),
                ('season', models.IntegerField(verbose_name="Saison de l'épisode")),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[('M', 'Film'), ('S', 'Serie'), ('E', 'Episode')], verbose_name='Type de Media')),
                ('title', models.CharField(max_length=100, verbose_name='Titre du Media')),
                ('synopsis', models.TextField(verbose_name='Synopsis')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('nationality', models.IntegerField(choices=[('FR', 'France'), ('US', 'Etats-Unies')], verbose_name='Nationalité')),
                ('originale_title', models.CharField(max_length=100, verbose_name='Titre original')),
                ('release_date', models.DateField(verbose_name='Date de sortie')),
                ('pegi_certification', models.IntegerField(verbose_name='Certification')),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='media',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='media.Media', verbose_name='Media'),
        ),
        migrations.AddField(
            model_name='episode',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='media.Media', verbose_name='Série'),
        ),
    ]
