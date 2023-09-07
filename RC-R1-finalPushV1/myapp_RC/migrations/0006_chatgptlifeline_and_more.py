# Generated by Django 4.1.1 on 2023-05-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_RC', '0005_alter_profile_logouttime'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatGPTLifeLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=1000)),
                ('numUsed', models.IntegerField(default=0)),
                ('lastUsed', models.FloatField(default=1700000000.213593)),
                ('isDepleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='lifeline1_postcount',
            new_name='focuscount',
        ),
        migrations.AddField(
            model_name='profile',
            name='lifeline1_using',
            field=models.BooleanField(null=True),
        ),
    ]