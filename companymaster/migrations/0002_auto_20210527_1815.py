# Generated by Django 2.1.7 on 2021-05-27 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companymaster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_no', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companymaster.Company')),
            ],
            options={
                'verbose_name': 'CompanyPDF',
                'verbose_name_plural': 'CompanyPDF',
            },
        ),
        migrations.CreateModel(
            name='PDFModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'PDFModel',
                'verbose_name_plural': 'PDFModel',
            },
        ),
        migrations.AddField(
            model_name='companypdf',
            name='pdf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companymaster.PDFModel'),
        ),
    ]
