# Generated by Django 2.1.5 on 2019-01-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library_registration',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Contact_no', models.IntegerField()),
                ('Email', models.EmailField(max_length=30)),
                ('Website', models.CharField(max_length=255)),
                ('Symbol', models.ImageField(upload_to='img/')),
                ('Date_of_establishment', models.DateTimeField()),
                ('Policy', models.CharField(max_length=255)),
                ('Membership_Details', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User_registration',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Contact_no', models.IntegerField()),
                ('Email', models.EmailField(max_length=30)),
                ('Website', models.CharField(max_length=255)),
            ],
        ),
    ]
