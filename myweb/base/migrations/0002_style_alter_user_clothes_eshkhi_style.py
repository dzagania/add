# Generated by Django 5.0.6 on 2024-07-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='clothes',
            field=models.ManyToManyField(blank=True, related_name='users', to='base.eshkhi'),
        ),
        migrations.AddField(
            model_name='eshkhi',
            name='style',
            field=models.ManyToManyField(blank=True, related_name='eshkhi', to='base.style'),
        ),
    ]
