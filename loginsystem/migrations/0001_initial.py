# Generated by Django 5.1.3 on 2025-05-08 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(default='Admin Name', max_length=100)),
                ('admin_id', models.CharField(default='unknown', max_length=50, unique=True)),
                ('admin_email', models.EmailField(default='admin@example.com', max_length=254, unique=True)),
                ('admin_phone', models.CharField(blank=True, default='0000000000', max_length=16, null=True)),
                ('department', models.CharField(default='Unknown Department', max_length=100)),
                ('role', models.CharField(choices=[('Placement Head', 'Placement Head'), ('Placement Officer', 'Placement Officer'), ('Coordinator', 'Coordinator')], default='Coordinator', max_length=20)),
                ('experience', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('password', models.CharField(default='password', max_length=128)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='Unknown Company', max_length=100)),
                ('website', models.URLField(blank=True, default='https://example.com', null=True)),
                ('industry', models.CharField(blank=True, default='Unknown Industry', max_length=100, null=True)),
                ('address', models.TextField(blank=True, default='No address provided', null=True)),
                ('contact_name', models.CharField(default='Unknown Contact', max_length=100)),
                ('email', models.EmailField(default='company@example.com', max_length=254)),
                ('phone', models.CharField(blank=True, default='0000000000', max_length=16, null=True)),
                ('job_profiles', models.TextField(blank=True, default='No job profiles listed', null=True)),
                ('location', models.CharField(blank=True, default='Unknown Location', max_length=100, null=True)),
                ('eligibility', models.TextField(blank=True, default='No eligibility criteria', null=True)),
                ('selection_process', models.TextField(blank=True, default='No selection process', null=True)),
                ('ctc', models.CharField(blank=True, default='Not specified', max_length=50, null=True)),
                ('internship', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('other_info', models.TextField(blank=True, default='No additional info', null=True)),
                ('password', models.CharField(blank=True, default='password', max_length=128, null=True)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown Student', max_length=100)),
                ('student_id', models.CharField(default='000000', max_length=50, unique=True)),
                ('email', models.EmailField(blank=True, default='student@example.com', max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, default='0000000000', max_length=16, null=True)),
                ('branch', models.CharField(blank=True, default='Unknown Branch', max_length=100, null=True)),
                ('year_of_study', models.CharField(blank=True, default='First Year', max_length=20, null=True)),
                ('cgpa', models.FloatField(blank=True, default=0.0, null=True)),
                ('skills', models.TextField(blank=True, default='No skills listed', null=True)),
                ('resume_link', models.URLField(blank=True, default='https://example.com', null=True)),
                ('password', models.CharField(blank=True, default='password', max_length=128, null=True)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
