# Generated by Django 2.0.5 on 2018-08-19 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20180819_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='under_comments', to='firstapp.Article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, choices=[('life', 'Life'), ('tech', 'Tech')], max_length=5, null=True),
        ),
    ]
