# Generated by Django 4.2.1 on 2023-06-02 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network_links', '0003_alter_factory_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('number_house', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.PositiveIntegerField(choices=[(0, 'Factory'), (1, 'Retail'), (2, 'Individual')])),
                ('debt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_house', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('contacts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='network_links.contacts')),
                ('product', models.ManyToManyField(to='network_links.product')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='network_links.network')),
            ],
            options={
                'verbose_name': 'Звено',
                'verbose_name_plural': 'Звенья',
            },
        ),
        migrations.RemoveField(
            model_name='individual',
            name='product',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='retail',
            name='product',
        ),
        migrations.RemoveField(
            model_name='retail',
            name='provider',
        ),
        migrations.DeleteModel(
            name='Factory',
        ),
        migrations.DeleteModel(
            name='Individual',
        ),
        migrations.DeleteModel(
            name='Retail',
        ),
    ]
