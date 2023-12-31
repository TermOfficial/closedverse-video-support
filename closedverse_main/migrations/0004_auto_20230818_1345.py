# Generated by Django 3.2.19 on 2023-08-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0003_auto_20230818_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='roles/')),
                ('organization', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='community',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='unique_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='protect_data',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='welcomemsg',
            name='order',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='role',
            name='is_static',
            field=models.BooleanField(default=False),
        ),
        #migrations.AlterField(
        #    model_name='user',
        #    name='role',
        #    field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='closedverse_main.role'),
        #),
    ]
