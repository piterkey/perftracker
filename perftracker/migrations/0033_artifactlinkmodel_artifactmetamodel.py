# Generated by Django 2.0.3 on 2018-09-30 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0032_merge_20180930_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtifactLinkModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artifact_uuid', models.UUIDField(db_index=True, editable=False, help_text='artifact uuid')),
                ('linked_uuid', models.UUIDField(db_index=True, editable=False, help_text='any object uuid')),
                ('deleted', models.BooleanField(db_index=True, help_text='Artifact link is deleted')),
            ],
        ),
        migrations.CreateModel(
            name='ArtifactMetaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, editable=False, help_text='Artifact file uuid')),
                ('filename', models.CharField(default='artifact', help_text='Artifact file name (for download)', max_length=128)),
                ('description', models.CharField(help_text='Artifact description', max_length=256)),
                ('mime', models.CharField(default='application/octet-stream', help_text='Artifact file mime type', max_length=32)),
                ('deleted', models.BooleanField(db_index=True, help_text='Artifact is deleted')),
                ('uploaded_dt', models.DateTimeField(default=django.utils.timezone.now, help_text='Datetime when artifact was uploaded')),
                ('ttl_days', models.IntegerField(default=180, help_text='Artifact time to live (days)')),
                ('deleted_dt', models.DateTimeField(blank=True, default=None, help_text='Datetime when artifact was deleted by garbage collector')),
                ('gc_dt', models.DateTimeField(db_index=True, help_text='Datetime when artifact can be deleted by GC')),
                ('size', models.IntegerField(help_text='Artifact file size in bytes')),
            ],
        ),
    ]
