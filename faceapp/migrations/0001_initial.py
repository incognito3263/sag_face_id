# Generated by Django 4.0.4 on 2022-06-07 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarWorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(verbose_name='Дата от')),
                ('date_to', models.DateField(blank=True, null=True, verbose_name='Дата до')),
                ('difference', models.IntegerField(default=0, verbose_name='Количество дней')),
            ],
            options={
                'verbose_name': 'Календарь выходных',
                'verbose_name_plural': 'Календарь выходных',
            },
        ),
        migrations.CreateModel(
            name='CsvImporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated_time', models.DateTimeField(verbose_name='Время последнего импорта')),
            ],
            options={
                'verbose_name': 'Время последнего импорта',
                'verbose_name_plural': 'Время последнего импорта',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.CharField(blank=True, max_length=1000, null=True, unique=True, verbose_name='ID сотрудника')),
                ('card_number', models.CharField(blank=True, max_length=1000, null=True, unique=True, verbose_name='Номер карты')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('birth_day', models.IntegerField(blank=True, null=True, verbose_name='Дата рождения')),
                ('full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=True, verbose_name='Статус сотрудника')),
                ('image', models.ImageField(upload_to='employee_image', verbose_name='Фото сотрудника')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Подробнее о сотруднике')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_department', to='faceapp.department', verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Сотрудники',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='От')),
                ('end_time', models.TimeField(verbose_name='До')),
            ],
            options={
                'verbose_name': 'Рабочее время',
                'verbose_name_plural': 'Рабочее время',
            },
        ),
        migrations.CreateModel(
            name='EmployeeVacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(verbose_name='Дата от')),
                ('date_to', models.DateField(blank=True, null=True, verbose_name='Дата до')),
                ('difference', models.IntegerField(default=0, verbose_name='Количество дней')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='faceapp.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Отпуск',
                'verbose_name_plural': 'Отпуск',
            },
        ),
        migrations.CreateModel(
            name='EmployeeBusinessTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(verbose_name='Дата от')),
                ('date_to', models.DateField(blank=True, null=True, verbose_name='Дата до')),
                ('difference', models.IntegerField(default=0, verbose_name='Количество дней')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='faceapp.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Командировки',
                'verbose_name_plural': 'Командировки',
                'permissions': (('can_add_business_trip', 'Can add Business trip'),),
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='working_hours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='faceapp.workinghours', verbose_name='Рабочее время'),
        ),
        migrations.CreateModel(
            name='DepartmentShiftTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_time', models.BooleanField(default=True, verbose_name='Работа по сменам')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='faceapp.department', verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Сменный рабочий',
                'verbose_name_plural': 'Сменный рабочий',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('check_status', models.CharField(choices=[('checkOut', 'Выход'), ('checkIn', 'Вход')], max_length=255, verbose_name='Состояние входа')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='Время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='faceapp.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Посещаемость',
                'verbose_name_plural': 'Посещаемость',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Username')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='faceapp.department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
