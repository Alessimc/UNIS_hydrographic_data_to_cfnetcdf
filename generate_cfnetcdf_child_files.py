from pathlib import Path
import xarray as xr
import time
from datetime import datetime, timezone

# Get the current UTC date and time
current_utc_time = datetime.now(timezone.utc)

# Format the datetime object as ISO 8601 string
iso_format_time = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')


# In and out file paths 
original_data_dir = Path('data/original_data')


transformed_data_dir = Path('data/transformed_data')

out_file = transformed_data_dir / 'CTD_all_1876-2019.nc'


# List subdirectories containing child files
subdirs = [d for d in original_data_dir.iterdir() if d.is_dir()]

# Loop through each subdirectory
for subdir in subdirs:
    print(f"Subdirectory: {subdir.name}")

    # List .nc files in the current subdirectory
    nc_files = list(subdir.glob('*.nc'))

    # Loop through each .nc file
    for nc_file in nc_files:
        # Read in file
        xrds = xr.open_dataset(nc_file)

        # Add missing MET ACDD metadata
        xrds.attrs['date_created'] = '2019-08-16T00:00:00Z'
        xrds.attrs['creator_type'] = 'person'
        xrds.attrs['creator_institution'] = 'University Centre in Svalbard; Norwegian Polar Institute'
        xrds.attrs['creator_name'] = 'Ragnheid Skogseth; Mathias Bockwoldt'
        xrds.attrs['creator_email'] = 'Ragnheid.Skogseth@unis.no; mathias.bockwoldt@npolar.no'
        xrds.attrs['creator_url'] = 'https://orcid.org/0000-0003-0210-4981; https://orcid.org/0000-0002-4646-9969'
        # xrds.attrs['publisher_name'] = # not required since hosted by MET?
        # xrds.attrs['publisher_email'] = # not required since hosted by MET?
        # xrds.attrs['publisher_url'] = # not required since hosted by MET?
        xrds.attrs['history'] = f'MET ACDD attributes were added at {iso_format_time} by Alessio Canclini.'
        xrds.attrs['project'] = 'A collection of projects have contributed to this hydrographic database. See references.'
        xrds.attrs['featureType'] = 'profile'

        # remove comment attrs if empty
        xrds.attrs.pop('comment', None)

        # Save the modified dataset to a new NetCDF file
        full_out_path = transformed_data_dir / subdir.name / nc_file.name

        full_out_path.parent.mkdir(parents=True, exist_ok=True)

        # Now write the NetCDF file
        xrds.to_netcdf(full_out_path)
        print(f'{full_out_path.name} succesfully saved to {full_out_path.parent}.')






    