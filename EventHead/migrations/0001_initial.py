
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EventWebSite', '0001_initial'),
        ('UserManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventWebSite.event')),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManager.event_committee')),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third')])),
                ('winning_certificate_issue', models.BooleanField(default=False)),
                ('winning_certi_otp', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventWebSite.event')),
                ('event_head', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EventHead.event_head')),
                ('winner', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='EventWebSite.participation')),
            ],
        ),
    ]
