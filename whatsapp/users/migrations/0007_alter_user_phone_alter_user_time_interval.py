# Generated by Django 4.0.8 on 2022-12-10 19:40

from django.db import migrations, models
import django_enum_choices.choice_builders
import django_enum_choices.fields
import whatsapp.users.constants


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='time_interval',
            field=django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('10 min', '10 min'), ('6 hr', '6 hr'), ('12 hr', '12 hr')], default=whatsapp.users.constants.TimeInterval['three_min'], enum_class=whatsapp.users.constants.TimeInterval, max_length=6),
        ),
    ]
