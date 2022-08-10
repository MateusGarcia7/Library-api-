from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_rename_user_type[1]_account_user_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='enrollment_no',
            field=models.IntegerField(default=12138, unique=True),
        ),
    ]