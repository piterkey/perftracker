# Generated by Django 2.0.3 on 2018-06-24 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0017_auto_20180624_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hwfarmnodemodel',
            old_name='cpu_score',
            new_name='cpu_score_up',
        ),
        migrations.RenameField(
            model_name='hwfarmnodemodel',
            old_name='disk_score',
            new_name='disk_score_up',
        ),
        migrations.RenameField(
            model_name='hwfarmnodemodel',
            old_name='network_score',
            new_name='network_score_up',
        ),
        migrations.RenameField(
            model_name='hwfarmnodemodel',
            old_name='ram_score',
            new_name='ram_score_up',
        ),
        migrations.RenameField(
            model_name='hwfarmnodemodel',
            old_name='storage_flush_per_sec',
            new_name='storage_flush_per_sec_up',
        ),
    ]
