# Generated by Django 2.1 on 2018-08-20 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_planners', '0004_auto_20180809_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='description',
        ),
        migrations.AddField(
            model_name='description',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_planners.Recipe'),
        ),
    ]