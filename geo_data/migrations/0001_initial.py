import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Area',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(

            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(

            name='PostalCode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(

            name='Village',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),

            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_data.country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_data.division')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(

            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo_data.area')),
                ('postal_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo_data.postalcode')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='postalcode',
            name='union',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_data.union'),
        ),
        migrations.CreateModel(

            name='Upazila',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_data.district')),
            ],
            options={
                'abstract': False,
            },
        ),

        migrations.AddField(
            model_name='union',
            name='upazila',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_data.upazila'),
        ),
        migrations.CreateModel(
            name='PoliceStation',

            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
                ('upazila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_data.upazila')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(

            name='Pauroshova',

            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
                ('upazila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_data.upazila')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostOffice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_data.village')),
            ],
            options={
                'abstract': False,
            },
        ),

        migrations.AddField(
            model_name='area',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo_data.village'),
        ),

        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),

                ('pauroshova', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo_data.pauroshova')),
                ('union', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo_data.union')),

            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='village',
            name='ward',
            field=models.ManyToManyField(to='geo_data.ward'),
        ),

        migrations.AddField(
            model_name='area',
            name='Ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo_data.ward'),
        ),

    ]
