# Generated by Django 4.2.7 on 2024-02-26 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_director', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('available_from', models.DateTimeField(default=None, null=True)),
                ('available_to', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('floor_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewRoom',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('from_time', models.DateTimeField()),
                ('to_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Occupied', 'Occupied'), ('Available', 'Available')], max_length=20)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interview_rooms', to='RoomManagement.boardmember')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interview_rooms', to='RoomManagement.room')),
            ],
        ),
    ]
