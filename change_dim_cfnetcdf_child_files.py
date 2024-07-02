from pathlib import Path
import xarray as xr
import netCDF4 as nc


transformed_data_dir = Path('data/transformed_data')

# List subdirectories containing child files
subdirs = [d for d in transformed_data_dir.iterdir() if d.is_dir()]

# Loop through each subdirectory
for subdir in subdirs:
    print(f"Subdirectory: {subdir.name}")

    # List .nc files in the current subdirectory
    nc_files = list(subdir.glob('*.nc'))

    # Loop through each .nc file
    for nc_file in nc_files:
        # Read in file
        with nc.Dataset(nc_file, 'r+') as ds:
            # Rename the dimension 'CALIBRATION' to 'CALIBRATION_COEFFICIENT'
            if 'CALIBRATION' in ds.dimensions:
                ds.renameDimension('CALIBRATION', 'CALIBRATION_COEFFICIENT')
            else:
                print("Dimension 'CALIBRATION' not found.")

        print(f'Dim name changed in  {nc_file.name}.')






    