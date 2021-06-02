# Generated by Django 2.1.7 on 2021-06-02 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companymaster', '0002_auto_20210527_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_no', models.IntegerField(blank=True, null=True)),
                ('pdf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companymaster.PDFModel')),
            ],
            options={
                'verbose_name': 'PDFPage',
                'verbose_name_plural': 'PDFPage',
            },
        ),
        migrations.RemoveField(
            model_name='companypdf',
            name='company',
        ),
        migrations.RemoveField(
            model_name='companypdf',
            name='pdf',
        ),
        migrations.DeleteModel(
            name='CompanyPDF',
        ),
        migrations.AddField(
            model_name='company',
            name='address_pdf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='address_pdf', to='companymaster.PDFPage'),
        ),
        migrations.AddField(
            model_name='company',
            name='business_description_pdf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='business_description_pdf', to='companymaster.PDFPage'),
        ),
        migrations.AddField(
            model_name='company',
            name='company_name_pdf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='company_name_pdf', to='companymaster.PDFPage'),
        ),
        migrations.AddField(
            model_name='company',
            name='country_pdf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='country_pdf', to='companymaster.PDFPage'),
        ),
        migrations.AddField(
            model_name='company',
            name='exchange_pdf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='exchange_pdf', to='companymaster.PDFPage'),
        ),
        migrations.AddField(
            model_name='company',
            name='symbol_pdf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='symbol_pdf', to='companymaster.PDFPage'),
        ),
    ]