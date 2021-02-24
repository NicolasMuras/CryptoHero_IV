# Generated by Django 3.1.7 on 2021-02-22 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=255, unique=True)),
                ('receiver', models.CharField(max_length=255, unique=True)),
                ('amount', models.FloatField()),
                ('timestamp', models.BigIntegerField()),
                ('txhash', models.CharField(max_length=255, unique=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.block')),
            ],
        ),
    ]
