# Generated by Django 3.2.25 on 2024-09-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(
                blank=True,
                help_text=(
                    'The groups this user belongs to. A user will get'
                    'all permissions granted to each of their groups.'),
                related_name='user_set',
                related_query_name='user',
                to='auth.Group',
                verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(
                default=False,
                help_text=(
                    'Designates that this user has all permissions without'
                    'explicitly assigning them.'),
                verbose_name='superuser status'),
        ),
    ]