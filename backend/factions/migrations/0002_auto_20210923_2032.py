# Generated by Django 3.2.7 on 2021-09-23 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('factions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faction',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='member_of_faction', through='factions.FactionMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FactionInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invited_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factions.faction')),
                ('invited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_faction_invitation', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faction_invitation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='faction',
            name='invitations',
            field=models.ManyToManyField(blank=True, related_name='invited_to_faction', through='factions.FactionInvitation', to=settings.AUTH_USER_MODEL),
        ),
    ]
