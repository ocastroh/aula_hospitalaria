# Generated by Django 5.1.2 on 2024-10-25 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academico', '0001_initial'),
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.alumno'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.docente'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.curso'),
        ),
        migrations.AddField(
            model_name='material',
            name='asignatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.asignatura'),
        ),
        migrations.AddField(
            model_name='clase',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academico.tipoclase'),
        ),
    ]