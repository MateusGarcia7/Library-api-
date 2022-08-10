from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_remove_account_user_type_account_user_type[1]_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user_type[1]',
            new_name='user_type',
        ),
        migrations.AlterField(
            model_name='account',
            name='enrollment_no',
            field=models.IntegerField(default=50331, unique=True),
        ),
    ]