# Generated by Django 3.1.7 on 2021-02-20 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jjrh_bed', '0004_bed_unitname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='unitname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beds', to='jjrh_bed.unitname'),
        ),
    ]
