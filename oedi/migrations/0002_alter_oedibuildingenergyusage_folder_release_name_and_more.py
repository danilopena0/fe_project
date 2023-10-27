# Generated by Django 4.2.6 on 2023-10-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oedi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="oedibuildingenergyusage",
            name="folder_release_name",
            field=models.CharField(
                choices=[
                    ("building_energy_models", "Building Energy Models"),
                    ("geographic_information", "Geographic Information"),
                    ("metadata", "Metadata"),
                    ("timeseries_aggregates", "Timeseries Aggregates"),
                    (
                        "timeseries_aggregates_metadata",
                        "Timeseries Aggregates Metadata",
                    ),
                    (
                        "timeseries_individual_buildings",
                        "Timeseries Individual Buildings",
                    ),
                    ("weather", "Weather"),
                    ("citation", "Citation"),
                    ("data_dictionary", "Data Dictionary"),
                    ("enumeration_dictionary", "Enumeration Dictionary"),
                    ("upgrade_dictionary", "Upgrade Dictionary"),
                    ("upgrades_lookup", "Upgrades Lookup"),
                    ("unknown", "Unknown"),
                ],
                default="unknown",
                help_text="The name of the folder release that the data came from.",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="oedibuildingenergyusage",
            name="location_classification",
            field=models.CharField(
                choices=[
                    ("county", "County"),
                    ("state", "State"),
                    ("midwest", "Midwest"),
                    ("northeast", "Northeast"),
                    ("south", "South"),
                    ("west", "West"),
                    ("unknown", "Unknown"),
                ],
                default="unknown",
                help_text="The geographic classification of the location (e.g. county, state, etc.)",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="oedibuildingenergyusage",
            name="upgrade_type",
            field=models.CharField(
                choices=[
                    ("baseline", "Baseline"),
                    ("upgrade", "Upgrade"),
                    ("unknown", "Unknown"),
                ],
                default="unknown",
                help_text="The type of building upgrade (baseline or upgrade).",
                max_length=100,
            ),
        ),
    ]
