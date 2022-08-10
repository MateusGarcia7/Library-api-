from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_account_user_type_alter_account_enrollment_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='enrollment_no',
            field=models.IntegerField(default=52754, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'member'), (2, 'IT staff'), (3, 'Librerian')], default=True),
        ),
    ]