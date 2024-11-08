

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Event Id')),
                ('event_name', models.CharField(max_length=50, verbose_name='Event Name')),
                ('event_detail', models.TextField(verbose_name='Event Details')),
                ('rules', models.TextField(verbose_name='Rules')),
                ('event_logo', models.ImageField(null=True, upload_to='event_logo/', verbose_name='Event Logo')),
                ('fees', models.IntegerField(verbose_name='Fees')),
                ('event_status', models.CharField(choices=[('Available', 'Available'), ('Scrapped', 'Scrapped'), ('Delete', 'Delete'), ('Full', 'Full')], max_length=30, verbose_name='Event Status')),
                ('venue', models.CharField(max_length=50, null=True, verbose_name='Venue')),
                ('date_time', models.DateTimeField(blank=True, null=True, verbose_name='Event Date & Time')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_content', models.CharField(max_length=1000, verbose_name='News Content')),
                ('hyperlink', models.CharField(max_length=50, verbose_name='hyperlink')),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('reg_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='UserManager.user')),
                ('remark', models.TextField(default=None, null=True)),
                ('total_payment', models.IntegerField()),
                ('remaining_payment', models.IntegerField()),
                ('paid_payment', models.IntegerField(default=0)),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_status', models.CharField(choices=[('Not Paid', 'Not Paid'), ('Paid', 'Paid'), ('Confirm', 'Confirm'), ('Attended', 'Attended'), ('Attended Winner', 'Attended Winner'), ('Certificate Issued', 'Certificate Issued'), ('Winner Certificate Issued', 'Winner Certificate Issued'), ('Scrapped', 'Scrapped'), ('Delete', 'Delete')], max_length=50)),
                ('certi_otp', models.IntegerField()),
                ('attendance_otp', models.IntegerField()),
                ('event', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='EventWebSite.event')),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventWebSite.participants')),
            ],
        ),
    ]
