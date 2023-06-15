# Generated by Django 4.1 on 2023-06-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_remove_package_tax_addcustomer_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('invoice_number', models.IntegerField()),
                ('balance_due', models.IntegerField()),
                ('invoice_date', models.DateField()),
                ('due_date', models.DateField()),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Package',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.RenameField(
            model_name='addcustomer',
            old_name='address',
            new_name='Customer_display_name',
        ),
        migrations.AddField(
            model_name='addcustomer',
            name='Portal_Language',
            field=models.CharField(choices=[('ENGLISH', 'ENGLISH'), ('NEPALI', 'NEPALI')], default='h', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addcustomer',
            name='currency',
            field=models.CharField(choices=[('NPR-Nepales', 'NPR-Nepales'), ('AUD', 'AUD'), ('CAD', 'CAD'), ('CNI', 'CNI')], default='AUD', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addcustomer',
            name='facebook',
            field=models.CharField(default='hgh', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addcustomer',
            name='first_name',
            field=models.CharField(default='jk', max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addcustomer',
            name='last_name',
            field=models.CharField(default='ghj', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addcustomer',
            name='primary_contact',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.')], default='rty', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addcustomer',
            name='twitter',
            field=models.CharField(default='fgh', max_length=50),
            preserve_default=False,
        ),
    ]