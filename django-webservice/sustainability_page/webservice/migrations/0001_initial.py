# Generated by Django 4.1.4 on 2022-12-14 16:05

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024)),
                ('slug', models.SlugField()),
                ('details', models.TextField(null=True)),
                ('locale', models.CharField(choices=[('en', 'english'), ('jp', 'eapanese')], max_length=1024, verbose_name='experiance locale')),
            ],
            options={
                'verbose_name': 'Initiative',
                'verbose_name_plural': 'Initiatives',
            },
        ),
        migrations.CreateModel(
            name='InitiativeGroup',
            fields=[
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'verbose_name': 'Initiative Group',
                'verbose_name_plural': 'Initiative Groups',
            },
        ),
        migrations.CreateModel(
            name='InitiativeImage',
            fields=[
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image_source', models.ImageField(upload_to='initiative-images')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='initiative-images')),
                ('image_type', models.CharField(max_length=1024)),
                ('primary', models.BooleanField(default=False)),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservice.initiative')),
            ],
            options={
                'verbose_name': 'Initiative Image',
                'verbose_name_plural': 'Initiative Images',
            },
        ),
        migrations.AddField(
            model_name='initiative',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservice.initiativegroup'),
        ),
        migrations.CreateModel(
            name='SusPageUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Not Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.EmailField(max_length=1024, null=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=1024, null=True, verbose_name='last name')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
