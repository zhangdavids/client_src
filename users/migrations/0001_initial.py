# Generated by Django 2.0.6 on 2019-03-27 13:58

from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_created=True, verbose_name='created time')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='名字')),
                ('token', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='token')),
                ('department', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='部门')),
                ('mobile', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='手机')),
                ('memo', models.TextField(blank=True, default=None, null=True, verbose_name='备注')),
                ('dep', models.CharField(blank=True, max_length=128, verbose_name='Department')),
                ('org', models.CharField(blank=True, max_length=128, verbose_name='Organization')),
                ('telephone', models.CharField(blank=True, max_length=50, verbose_name='Telephone')),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=5)),
                ('address', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User Profile',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
