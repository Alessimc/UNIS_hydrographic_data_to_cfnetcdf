from pathlib import Path
import xarray as xr
import numpy as np
import netCDF4 as nc
from datetime import datetime, timezone

# Get the current UTC date and time
current_utc_time = datetime.now(timezone.utc)

# Format the datetime object as ISO 8601 string
iso_format_time = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')



# Define the reference time
reference_time = np.datetime64('1876-01-01')



# In and out file paths 
original_data_dir = Path('data/original_data')

in_file = original_data_dir / 'CTD_all_1876-2019.nc'

transformed_data_dir = Path('data/transformed_data')

out_file = transformed_data_dir / 'CTD_all_1876-2019.nc'


# Load in dataset
xrds = xr.open_dataset(in_file)

print(xrds)


# Generate a unique integer CAST value for each time point
cast_values = np.arange(1, len(xrds['TIME']) + 1)

# Create a new CAST dimension
xrds = xrds.rename({'TIME': 'CAST'})

# Move the original TIME to a data variable that is CAST dependent
xrds['TIME'] = (('CAST',), xrds['CAST'].values)
# change to days since ref time
time_values = ((xrds['TIME'].values - reference_time) / np.timedelta64(1, 'D')).astype(np.int32)
xrds['TIME'].values = time_values

# Assign integer CAST values
xrds['CAST'] = (('CAST',), cast_values.astype(np.int32))

# Modify the dimensions of data variables to be dependent on 'CAST' instead of 'TIME'
data_vars_to_reshape = [var for var in xrds.data_vars if 'CAST' in xrds[var].dims]

for var in data_vars_to_reshape:
    xrds[var] = xrds[var].rename({'CAST': 'CAST'})


# Add standard and/or long name to TIME and CAST
xrds['CAST'].attrs = {'long_name': 'CTD cast nr.'}

xrds['TIME'].attrs = {'long_name': 'time',
                      'standard_name': 'time',
                      'units': f'days since {reference_time}',
                      'axis': 'T'}


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
xrds.attrs['history'] = f'At {iso_format_time} the TIME dimension was replaced by a CAST dimension to achieve a monotonic series. TIME(CAST) was created as a data variable. MET ACDD attributes were added. Changes made by Alessio Canclini.'
xrds.attrs['project'] = 'A collection of projects have contributed to this hydrographic database. See references.'

# remove comment attrs if empty
xrds.attrs.pop('comment', None)


# Save the modified dataset to a new NetCDF file
print(xrds)
xrds.to_netcdf(out_file)

with nc.Dataset(out_file, 'r+') as ds:
    # Rename the dimension 'CALIBRATION' to 'CALIBRATION_COEFFICIENT'
    if 'CALIBRATION' in ds.dimensions:
        ds.renameDimension('CALIBRATION', 'CALIBRATION_COEFFICIENT')
    else:
        print("Dimension 'CALIBRATION' not found.")
print(f'{out_file.name} succesfully saved to {out_file.parent}.')

print(ds)
