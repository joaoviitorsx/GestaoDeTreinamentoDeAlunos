# Generated by Django 5.1.6 on 2025-02-18 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treino', '0002_alter_alunos_faixa_aulasconcluidas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='faixa',
            field=models.CharField(choices=[('M', 'Marrom'), ('P', 'Preta'), ('B', 'Branca'), ('A', 'Azul'), ('R', 'Roxa')], default='B', max_length=1),
        ),
        migrations.AlterField(
            model_name='aulasconcluidas',
            name='faixa_atual',
            field=models.CharField(choices=[('M', 'Marrom'), ('P', 'Preta'), ('B', 'Branca'), ('A', 'Azul'), ('R', 'Roxa')], default='B', max_length=1),
        ),
    ]
