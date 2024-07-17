# check if all variables have a coeverage_content_type and a long_name attribute, if not, assign one

from pathlib import Path
import xarray as xr


transformed_data_dir = Path('data/transformed_data')

parent_file = transformed_data_dir / 'CTD_all_1876-2019.nc'

xrds = xr.open_dataset(parent_file)

# xrds.load()

# xrds.close()

# looking at variable attributes before long_name changes
for data_var in xrds.coords:
    try:
        print(data_var, xrds.coords[data_var].attrs['long_name'])
    except:
        print(data_var, '\033[31m MISSING \033[0m')
for data_var in xrds.data_vars:
    try:
        print(data_var, xrds.data_vars[data_var].attrs['long_name'])
    except:
        print(data_var, '\033[31m MISSING \033[0m')

print('')

# Define default descriptive strings for coordinates and variables
default_long_names = {
    'PRES': 'Sea water pressure',
    'TIME': 'time',
    'CAST': 'CTD cast nr.',
    'CALIBRATION': 'Slope and offset for linear regression between CTD and bottle conductivities',
    'STATION': 'Station',
    'LATITUDE': 'latitude',
    'LONGITUDE': 'longitude',
    'TEMP': 'Sea water temperature',
    'PSAL': 'Practical salinity of sea water',
    'CNDC': 'Electrical conductivity of sea water',
    'FDEP': 'Bathymetric depth at profile measurement site from echosounder.',
    'SHIP': 'Ship',
    'SHIPID': 'shipID',
    'OWNER': 'Owner',
    'CRUISE': 'Cruise',
    'TYPE': 'Data type using World Ocean Data (WMO) acronyms: C=CTD, B=Bottle, XCTD=Expendable CTD, XBT=Expendable bathythermograph, MBT=Mechanical bathythermograph, Unknown=Unknown'
}

# Define default coverage_content_type
coverage_content_types = {
    'PRES': 'physicalMeasurement',
    'TIME': 'coordinate',
    'CAST': 'referenceInformation',
    'CALIBRATION': 'referenceInformation',
    'STATION': 'referenceInformation',
    'LATITUDE': 'coordinate',
    'LONGITUDE': 'coordinate',
    'TEMP': 'physicalMeasurement',
    'PSAL': 'physicalMeasurement',
    'CNDC': 'physicalMeasurement',
    'FDEP': 'physicalMeasurement',
    'SHIP': 'referenceInformation',
    'SHIPID': 'referenceInformation',
    'OWNER': 'referenceInformation',
    'CRUISE': 'referenceInformation',
    'TYPE': 'referenceInformation'
}

# Function to add long_name attribute if it doesn't exist
def add_long_name(var, default_long_name):
    if 'long_name' not in xrds[var].attrs:
        xrds[var].attrs['long_name'] = default_long_name
        print(f"Added long_name to {var}: {default_long_name}")

# Function to add coverage_content_type attribute if it doesn't exist
def add_coverage_content_type(var, coverage_content_type):
    if 'coverage_content_type' not in xrds[var].attrs:
        xrds[var].attrs['coverage_content_type'] = coverage_content_type
        print(f"Added coverage_content_type to {var}: {coverage_content_type}")

    # PARENT FILE
# Check coordinates
for coord in xrds.coords:
    if coord in default_long_names:
        add_long_name(coord, default_long_names[coord])
        add_coverage_content_type(coord, coverage_content_types[coord])

# Check data variables
for var in xrds.data_vars:
    if var in default_long_names:
        add_long_name(var, default_long_names[var])
        add_coverage_content_type(var, coverage_content_types[var])




# looking at variable attributes after long_name changes
print('')
for data_var in xrds.coords:
    print(data_var, xrds.coords[data_var].attrs['coverage_content_type'])
    try:
        print(data_var, xrds.coords[data_var].attrs['long_name'])
    except:
        print(data_var, '\033[31m MISSING \033[0m')
for data_var in xrds.data_vars:
    print(data_var, xrds.data_vars[data_var].attrs['coverage_content_type'])
    try:
        print(data_var, xrds.data_vars[data_var].attrs['long_name'])
    except:
        print(data_var, '\033[31m MISSING \033[0m')

# Overwrite parent file
# xrds.to_netcdf(parent_file, mode='w')


# then do for all child files
print('Traversing child files')
# List subdirectories containing child files
subdirs = [d for d in transformed_data_dir.iterdir() if d.is_dir()]

# Loop through each subdirectory
for subdir in subdirs:
    print(f"Subdirectory: {subdir.name}")

    # List .nc files in the current subdirectory
    nc_files = list(subdir.glob('*.nc'))

    # Loop through each .nc file
    for nc_file in nc_files:
        xrds = xr.open_dataset(nc_file)

        xrds.load()

        xrds.close()

        # Check coordinates
        for coord in xrds.coords:
            if coord in default_long_names:
                add_long_name(coord, default_long_names[coord])
                add_coverage_content_type(coord, coverage_content_types[coord])

        # Check data variables
        for var in xrds.data_vars:
            if var in default_long_names:
                add_long_name(var, default_long_names[var])
                add_coverage_content_type(var, coverage_content_types[var])

        xrds.to_netcdf(nc_file, mode='w')
        
        # import subprocess

        # # Function to run ncdump and capture the output
        # def run_ncdump(file_path, options=""):
        #     try:
        #         # Construct the ncdump command
        #         command = f"ncdump {options} {file_path}"
        #         # Run the command as a subprocess and capture the output
        #         result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        #         # Return the output of ncdump
        #         return result.stdout
        #     except subprocess.CalledProcessError as e:
        #         print(f"An error occurred while running ncdump: {e}")
        #         return None

        # # Example usage
        # options = "-h"  # Options for ncdump, e.g., '-h' for header only

        # output = run_ncdump(nc_file, options)
        # if output:
        #     print(output)
