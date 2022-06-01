# Generated by Django 4.0.1 on 2022-03-09 23:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0007_brew_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipie',
            name='is_best',
        ),
        migrations.AddField(
            model_name='brew',
            name='bestRecipieID',
            field=models.ForeignKey(blank=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='brew', to='brew.recipie'),
            preserve_default=False,
        ),
    ]