# Generated by Django 5.1.2 on 2024-11-20 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0005_remove_antecedentesfamiliares_alumno'),
        ('personas', '0007_alumno_ubicacion_apoderado_ubicacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='antecedentes_familiares',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrativo.antecedentesfamiliares'),
        ),
    ]
