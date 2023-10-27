import pandas as pd

from oedi.models import OEDIBuildingEnergyUsage, FolderName, LocationClassification, UpgradeType

# Read in data
oedi_data = pd.read_parquet('oedi/data/105029-0.parquet', engine='pyarrow')
oedi_data.reset_index(inplace=True)

# Grab a row
i = 0
row = oedi_data.iloc[i]
print(f'Processing row {i} of {len(oedi_data)}')

# Create or update OEDIBuildingEnergyUsage object
oedi_object, created = OEDIBuildingEnergyUsage.objects.update_or_create(
    folder_release_name=FolderName.TIMESERIES_INDIVIDUAL_BUILDINGS,
    location_classification=LocationClassification.COUNTY,
    location_name='G0100010',
    building_id=row['bldg_id'],
    upgrade_type=UpgradeType.BASELINE,
    timestamp=row['timestamp'],
    district_cooling_energy_consumption=row['out.district_cooling.cooling.energy_consumption'],
    district_heating_energy_consumption=row['out.district_heating.heating.energy_consumption'],
    district_heating_water_systems_energy_consumption=row['out.district_heating.water_systems.energy_consumption'],
    electricity_cooling_energy_consumption=row['out.electricity.cooling.energy_consumption'],
    electricity_exterior_lighting_energy_consumption=row['out.electricity.exterior_lighting.energy_consumption'],
    electricity_fans_energy_consumption=row['out.electricity.fans.energy_consumption'],
    electricity_heat_recovery_energy_consumption=row['out.electricity.heat_recovery.energy_consumption'],
    electricity_heat_rejection_energy_consumption=row['out.electricity.heat_rejection.energy_consumption'],
    electricity_heating_energy_consumption=row['out.electricity.heating.energy_consumption'],
    electricity_interior_equipment_energy_consumption=row['out.electricity.interior_equipment.energy_consumption'],
    electricity_interior_lighting_energy_consumption=row['out.electricity.interior_lighting.energy_consumption'],
    electricity_pumps_energy_consumption=row['out.electricity.pumps.energy_consumption'],
    electricity_refrigeration_energy_consumption=row['out.electricity.refrigeration.energy_consumption'],
    electricity_water_systems_energy_consumption=row['out.electricity.water_systems.energy_consumption'],
    natural_gas_heating_energy_consumption=row['out.natural_gas.heating.energy_consumption'],
    natural_gas_interior_equipment_energy_consumption=row['out.natural_gas.interior_equipment.energy_consumption'],
    natural_gas_water_systems_energy_consumption=row['out.natural_gas.water_systems.energy_consumption'],
    district_cooling_total_energy_consumption=row['out.district_cooling.total.energy_consumption'],
    district_heating_total_energy_consumption=row['out.district_heating.total.energy_consumption'],
    electricity_total_energy_consumption=row['out.electricity.total.energy_consumption'],
    natural_gas_total_energy_consumption=row['out.natural_gas.total.energy_consumption'],
    other_fuel_heating_energy_consumption=row['out.other_fuel.heating.energy_consumption'],
    other_fuel_water_systems_energy_consumption=row['out.other_fuel.water_systems.energy_consumption'],
    other_fuel_total_energy_consumption=row['out.other_fuel.total.energy_consumption'],
    site_energy_total_energy_consumption=row['out.site_energy.total.energy_consumption'],
    district_cooling_energy_consumption_intensity=row['out.district_cooling.cooling.energy_consumption_intensity'],
    district_heating_energy_consumption_intensity=row['out.district_heating.heating.energy_consumption_intensity'],
    district_heating_water_systems_energy_consumption_intensity=row[
        'out.district_heating.water_systems.energy_consumption_intensity'],
    electricity_cooling_energy_consumption_intensity=row['out.electricity.cooling.energy_consumption_intensity'],
    electricity_exterior_lighting_energy_consumption_intensity=row[
        'out.electricity.exterior_lighting.energy_consumption_intensity'],
    electricity_fans_energy_consumption_intensity=row['out.electricity.fans.energy_consumption_intensity'],
    electricity_heat_recovery_energy_consumption_intensity=row[
        'out.electricity.heat_recovery.energy_consumption_intensity'],
    electricity_heat_rejection_energy_consumption_intensity=row[
        'out.electricity.heat_rejection.energy_consumption_intensity'],
    electricity_heating_energy_consumption_intensity=row['out.electricity.heating.energy_consumption_intensity'],
    electricity_interior_equipment_energy_consumption_intensity=row[
        'out.electricity.interior_equipment.energy_consumption_intensity'],
    electricity_interior_lighting_energy_consumption_intensity=row[
        'out.electricity.interior_lighting.energy_consumption_intensity'],
    electricity_pumps_energy_consumption_intensity=row['out.electricity.pumps.energy_consumption_intensity'],
    electricity_refrigeration_energy_consumption_intensity=row[
        'out.electricity.refrigeration.energy_consumption_intensity'],
    electricity_water_systems_energy_consumption_intensity=row[
        'out.electricity.water_systems.energy_consumption_intensity'],
    natural_gas_heating_energy_consumption_intensity=row['out.natural_gas.heating.energy_consumption_intensity'],
    natural_gas_interior_equipment_energy_consumption_intensity=row[
        'out.natural_gas.interior_equipment.energy_consumption_intensity'],
    natural_gas_water_systems_energy_consumption_intensity=row[
        'out.natural_gas.water_systems.energy_consumption_intensity'],
    district_cooling_total_energy_consumption_intensity=row[
        'out.district_cooling.total.energy_consumption_intensity'],
    district_heating_total_energy_consumption_intensity=row[
        'out.district_heating.total.energy_consumption_intensity'],
    electricity_total_energy_consumption_intensity=row['out.electricity.total.energy_consumption_intensity'],
    natural_gas_total_energy_consumption_intensity=row['out.natural_gas.total.energy_consumption_intensity'],
    other_fuel_heating_energy_consumption_intensity=row['out.other_fuel.heating.energy_consumption_intensity'],
    other_fuel_water_systems_energy_consumption_intensity=row[
        'out.other_fuel.water_systems.energy_consumption_intensity'],
    other_fuel_total_energy_consumption_intensity=row['out.other_fuel.total.energy_consumption_intensity'],
    site_energy_total_energy_consumption_intensity=row['out.site_energy.total.energy_consumption_intensity'],
)

# Save or update
if created:
    print(f'Created: {oedi_object}')
    oedi_object.save()
else:
    print(f'Updated: {oedi_object}')
