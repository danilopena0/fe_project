from django.db import models


######################
# Enumerations
######################


class FolderName(models.TextChoices):
    """
    The name of the folder release that the data came from.
    """
    BUILDING_ENERGY_MODELS = 'building_energy_models'
    GEOGRAPHIC_INFORMATION = 'geographic_information'
    METADATA = 'metadata'
    TIMESERIES_AGGREGATES = 'timeseries_aggregates'
    TIMESERIES_AGGREGATES_METADATA = 'timeseries_aggregates_metadata'
    TIMESERIES_INDIVIDUAL_BUILDINGS = 'timeseries_individual_buildings'
    WEATHER = 'weather'
    CITATION = 'citation'
    DATA_DICTIONARY = 'data_dictionary'
    ENUMERATION_DICTIONARY = 'enumeration_dictionary'
    UPGRADE_DICTIONARY = 'upgrade_dictionary'
    UPGRADES_LOOKUP = 'upgrades_lookup'
    UNKNOWN = 'unknown'


class LocationClassification(models.TextChoices):
    """
    The geographic classification of the location (e.g. county, state, etc.)
    """
    COUNTY = 'county'
    STATE = 'state'
    MIDWEST = 'midwest'
    NORTHEAST = 'northeast'
    SOUTH = 'south'
    WEST = 'west'
    UNKNOWN = 'unknown'


class UpgradeType(models.TextChoices):
    """
    The type of building upgrade (baseline or upgrade).
    """
    BASELINE = 'baseline'
    UPGRADE = 'upgrade'
    UNKNOWN = 'unknown'


######################
# Abstract Models / Mixins
######################


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


######################
# Main Models
######################


class OEDIBuildingEnergyUsage(TimeStampedModel):
    """
    A model that represents the building energy usage data from the Open Energy Data Initiative (OEDI) dataset.
    This takes in timeseries data for a given building and stores it in a database.
    """
    folder_release_name = models.CharField(choices=FolderName.choices,
                                           max_length=100,
                                           default=FolderName.UNKNOWN,
                                           help_text="The name of the folder release that the data came from.")

    location_classification = models.CharField(choices=LocationClassification.choices,
                                               max_length=100,
                                               default=LocationClassification.UNKNOWN,
                                               help_text="The geographic classification of the location "
                                                         "(e.g. county, state, etc.)")
    location_name = models.CharField(max_length=100,
                                     help_text="The name of the specific location.")

    building_id = models.CharField(max_length=100, blank=False, null=False,
                                   help_text="The unique identifier for the building.")

    upgrade_type = models.CharField(choices=UpgradeType.choices,
                                    max_length=100,
                                    default=UpgradeType.UNKNOWN,
                                    help_text="The type of building upgrade (baseline or upgrade).")

    timestamp = models.DateTimeField(blank=False, null=False,
                                     help_text="The date and time of the energy data for the given building.")

    district_cooling_energy_consumption = models.FloatField(null=True, blank=True)
    district_heating_energy_consumption = models.FloatField(null=True, blank=True)
    district_heating_water_systems_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_cooling_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_exterior_lighting_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_fans_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_heat_recovery_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_heat_rejection_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_heating_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_interior_equipment_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_interior_lighting_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_pumps_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_refrigeration_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_water_systems_energy_consumption = models.FloatField(null=True, blank=True)
    natural_gas_heating_energy_consumption = models.FloatField(null=True, blank=True)
    natural_gas_interior_equipment_energy_consumption = models.FloatField(null=True, blank=True)
    natural_gas_water_systems_energy_consumption = models.FloatField(null=True, blank=True)
    district_cooling_total_energy_consumption = models.FloatField(null=True, blank=True)
    district_heating_total_energy_consumption = models.FloatField(null=True, blank=True)
    electricity_total_energy_consumption = models.FloatField(null=True, blank=True)
    natural_gas_total_energy_consumption = models.FloatField(null=True, blank=True)
    other_fuel_heating_energy_consumption = models.FloatField(null=True, blank=True)
    other_fuel_water_systems_energy_consumption = models.FloatField(null=True, blank=True)
    other_fuel_total_energy_consumption = models.FloatField(null=True, blank=True)
    site_energy_total_energy_consumption = models.FloatField(null=True, blank=True)
    district_cooling_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    district_heating_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    district_heating_water_systems_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_cooling_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_exterior_lighting_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_fans_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_heat_recovery_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_heat_rejection_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_heating_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_interior_equipment_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_interior_lighting_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_pumps_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_refrigeration_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_water_systems_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    natural_gas_heating_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    natural_gas_interior_equipment_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    natural_gas_water_systems_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    district_cooling_total_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    district_heating_total_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    electricity_total_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    natural_gas_total_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    other_fuel_heating_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    other_fuel_water_systems_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    other_fuel_total_energy_consumption_intensity = models.FloatField(null=True, blank=True)
    site_energy_total_energy_consumption_intensity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Building {self.building_id} on {self.timestamp}"
