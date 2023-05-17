# Generated by Django 4.1.3 on 2022-12-02 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('cnumber', models.CharField(db_column='Cnumber', max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=30)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=50, null=True)),
                ('phone', models.CharField(db_column='Phone', max_length=30, unique=True)),
                ('edate', models.DateField(blank=True, db_column='Edate', null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('year', models.TextField(db_column='Year', primary_key=True, serialize=False)),
                ('no', models.IntegerField(db_column='No', unique=True)),
                ('datetime', models.DateTimeField(blank=True, db_column='Datetime', null=True)),
                ('duration', models.TimeField(blank=True, db_column='Duration', null=True)),
            ],
            options={
                'db_table': 'episode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('gname', models.CharField(db_column='Gname', max_length=30, primary_key=True, serialize=False)),
                ('no_of_member', models.IntegerField(blank=True, db_column='No_of_member', null=True)),
            ],
            options={
                'db_table': 'group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invitedguest',
            fields=[
                ('guest_id', models.AutoField(db_column='Guest_ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'invitedguest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('ssn', models.CharField(db_column='SSN', max_length=12, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'mentor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('ssn', models.CharField(db_column='SSN', max_length=12, primary_key=True, serialize=False)),
                ('phone', models.CharField(db_column='Phone', max_length=30, unique=True)),
                ('fname', models.CharField(blank=True, db_column='Fname', max_length=20, null=True)),
                ('lname', models.CharField(db_column='Lname', max_length=20)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('year', models.TextField(db_column='Year', primary_key=True, serialize=False)),
                ('location', models.CharField(db_column='Location', max_length=100)),
            ],
            options={
                'db_table': 'season',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('number', models.AutoField(db_column='Number', primary_key=True, serialize=False)),
                ('released_year', models.TextField(blank=True, db_column='Released_year', null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=30, null=True)),
            ],
            options={
                'db_table': 'song',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groupsignaturesong',
            fields=[
                ('gname', models.OneToOneField(db_column='Gname', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.group')),
                ('song_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'groupsignaturesong',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mc',
            fields=[
                ('ssn', models.OneToOneField(db_column='SSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.person')),
            ],
            options={
                'db_table': 'mc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mentorvaluatetrainee',
            fields=[
                ('year', models.OneToOneField(db_column='Year', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.season')),
                ('score', models.IntegerField(blank=True, db_column='Score', null=True)),
            ],
            options={
                'db_table': 'mentorvaluatetrainee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('ssn', models.OneToOneField(db_column='SSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.mentor')),
            ],
            options={
                'db_table': 'producer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seasonmentor',
            fields=[
                ('year', models.OneToOneField(db_column='Year', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.season')),
            ],
            options={
                'db_table': 'seasonmentor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seasontrainee',
            fields=[
                ('year', models.OneToOneField(db_column='Year', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.season')),
            ],
            options={
                'db_table': 'seasontrainee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('ssn', models.OneToOneField(db_column='SSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.mentor')),
            ],
            options={
                'db_table': 'singer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Songcomposedby',
            fields=[
                ('song', models.OneToOneField(db_column='Song_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.song')),
            ],
            options={
                'db_table': 'songcomposedby',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Songwriter',
            fields=[
                ('ssn', models.OneToOneField(db_column='SSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.mentor')),
            ],
            options={
                'db_table': 'songwriter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('year', models.OneToOneField(db_column='Year', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.episode')),
                ('stage_no', models.IntegerField(db_column='Stage_No', unique=True)),
                ('is_group', models.IntegerField(blank=True, db_column='is_Group', null=True)),
                ('skill', models.IntegerField(blank=True, db_column='Skill', null=True)),
                ('total_vote', models.IntegerField(blank=True, db_column='Total_vote', null=True)),
            ],
            options={
                'db_table': 'stage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stageincludetrainee',
            fields=[
                ('ep_no', models.OneToOneField(db_column='Ep_No', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.episode')),
                ('ssn_trainee', models.CharField(db_column='SSN_Trainee', max_length=12)),
                ('role', models.IntegerField(blank=True, db_column='Role', null=True)),
                ('no_of_vote', models.IntegerField(blank=True, db_column='No_of_Vote', null=True)),
            ],
            options={
                'db_table': 'stageincludetrainee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Themesong',
            fields=[
                ('song', models.OneToOneField(db_column='Song_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.song')),
            ],
            options={
                'db_table': 'themesong',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('ssn', models.OneToOneField(db_column='SSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.person')),
                ('dob', models.DateField(blank=True, db_column='DoB', null=True)),
                ('photo', models.TextField(blank=True, db_column='Photo', null=True)),
            ],
            options={
                'db_table': 'trainee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Guestsupportstage',
            fields=[
                ('year', models.OneToOneField(db_column='Year', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.stage')),
            ],
            options={
                'db_table': 'guestsupportstage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producerprogram',
            fields=[
                ('program_name', models.CharField(db_column='Program_name', max_length=30)),
                ('ssn', models.OneToOneField(db_column='SSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.producer')),
            ],
            options={
                'db_table': 'producerprogram',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Singersignaturesong',
            fields=[
                ('song_name', models.CharField(db_column='Song_name', max_length=30)),
                ('ssn', models.OneToOneField(db_column='SSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='information.singer')),
            ],
            options={
                'db_table': 'singersignaturesong',
                'managed': False,
            },
        ),
    ]
