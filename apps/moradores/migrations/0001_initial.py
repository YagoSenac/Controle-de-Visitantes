# Generated by Django 5.1.1 on 2024-11-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=200, verbose_name='Nome completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('numero_casa', models.PositiveSmallIntegerField(verbose_name='Número da casa do morador')),
                ('placa_veiculo', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa do Carro')),
            ],
            options={
                'verbose_name': 'Morador',
                'verbose_name_plural': 'Moradores',
                'db_table': 'Morador',
            },
        ),
    ]
