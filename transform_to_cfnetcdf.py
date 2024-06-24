from pathlib import Path
import xarray as xr
import time
from check_for_met_ACDD import missing_MET_ACDD_attributes


original_data_dir = Path('data/original_data')

# parent file
parent_file_path = original_data_dir / 'CTD_all_1876-2019.nc'

xrds = xr.open_dataset(parent_file_path)

# TODO: Add missing MET ACDD attributes
# xrds.attrs['date_created'] = '2019-08-16T00:00:00Z'
# xrds.attrs['creator_type'] = 'person'
# xrds.attrs['creator_institution'] = 'Norwegian Polar Institute' TODO: Add UNIS?
# xrds.attrs['creator_name'] = 'Mathias Bockwoldt' TODO: Add R. Skogseth?
# xrds.attrs['creator_email'] = 'mathias.bockwoldt@npolar.no'TODO: Add R. Skogseth?
# xrds.attrs['creator_url'] = # TODO
# xrds.attrs['publisher_name'] = # not required since hosted by MET?
# xrds.attrs['publisher_email'] = # not required since hosted by MET?
# xrds.attrs['publisher_url'] = # not required since hosted by MET?
# xrds.attrs['history'] = # TODO
# xrds.attrs['project'] = # TODO

# overwrite file  
# xrds.to_netcdf(parent_file_path)



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

        print(missing_MET_ACDD_attributes(nc_file))

        # TODO: Add missing MET ACDD attributes
        # xrds.attrs['date_created'] = '2019-08-16T00:00:00Z'
        # xrds.attrs['creator_type'] = 'person'
        # xrds.attrs['creator_institution'] = 'Norwegian Polar Institute' TODO: Add UNIS?
        # xrds.attrs['creator_name'] = 'Mathias Bockwoldt' TODO: Add R. Skogseth?
        # xrds.attrs['creator_email'] = 'mathias.bockwoldt@npolar.no'TODO: Add R. Skogseth?
        # xrds.attrs['creator_url'] = # TODO
        # xrds.attrs['publisher_name'] = # not required since hosted by MET?
        # xrds.attrs['publisher_email'] = # not required since hosted by MET?
        # xrds.attrs['publisher_url'] = # not required since hosted by MET?
        # xrds.attrs['history'] = # TODO
        # xrds.attrs['project'] = # TODO


        # overwrite file  
        # xrds.to_netcdf(nc_file)





    