from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_account_enrollment_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user_type',
        ),
        migrations.AddField(
            model_name='account',
            name='user_type[1]',
            field=models.PositiveSmallIntegerField(choices=[(1, 'member'), (2, 'IT staff'), (3, 'Librerian')], default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='enrollment_no',
            field=models.IntegerField(default=57562, unique=True),
        ),
    ]