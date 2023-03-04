# Generated by Django 4.1.5 on 2023-01-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.IntegerField()),
                ('glucose', models.IntegerField()),
                ('blood_pressure', models.IntegerField()),
                ('skin_thickess', models.IntegerField()),
                ('insulin', models.IntegerField()),
                ('bmi', models.FloatField()),
                ('diabetes_pedigree_function', models.FloatField()),
                ('age', models.PositiveIntegerField()),
                ('result', models.TextField(max_length=100)),
            ],
        ),
    ]