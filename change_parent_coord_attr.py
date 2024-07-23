import netCDF4 as nc

def fix_coordinates(file_path):
    # Open the netCDF file in append mode
    dataset = nc.Dataset(file_path, 'a')

    # List of variable names to update coordinates for
    vars_to_update = ['CALIBRATION', 'STATION', 'LATITUDE', 'LONGITUDE', 'TEMP', 'PSAL', 'CNDC', 'FDEP', 'SHIP', 'SHIPID', 'OWNER', 'CRUISE', 'TYPE']

    # for var_name in vars_to_update:
    #     if var_name in dataset.variables:
    #         var = dataset.variables[var_name]
    #         if 'coordinates' in var.ncattrs():
    #             # Set coordinates attribute to 'CAST'
    #             if var_name in ['TEMP', 'PSAL', 'CNDC']:
    #                 var.setncattr('coordinates', 'CAST PRES')
    #             elif var_name == 'SHIP':
    #                 var.setncattr('coordinates', 'CAST, SHIP_CHAR')
    #             elif var_name == 'OWNER':
    #                 var.setncattr('coordinates', 'CAST, OWNER_CHAR')
    #             elif var_name == 'CRUISE':
    #                 var.setncattr('coordinates', 'CAST, CRUISE_CHAR')
    #             elif var_name == 'TYPE':
    #                 var.setncattr('coordinates', 'CAST, TYPE_CHAR')
    #             else:
    #                 var.setncattr('coordinates', 'CAST')

    for var_name in vars_to_update:
        if var_name in dataset.variables:
            var = dataset.variables[var_name]
            if 'coordinates' in var.ncattrs():
                # Remove the 'coordinates' attribute
                del var.coordinates


    # Update the global attribute creator_url
    # new_creator_url = 'https://orcid.org/0000-0003-0210-4981; https://orcid.org/0000-0002-4646-9969; https://orcid.org/0000-0002-3331-5581; https://orcid.org/0000-0003-0900-5679; https://orcid.org/0000-0002-3068-1754; https://tinyurl.com/4y3w8fvj; https://www.scopus.com/authid/detail.uri?authorId=7201789296; https://orcid.org/0000-0001-5636-2092; https://orcid.org/0000-0002-6386-2471; https://orcid.org/0000-0002-6566-4292'
    # dataset.setncattr('creator_url', new_creator_url)

    # Close the dataset
    dataset.close()


# Path to your netCDF file
file_path = '/home/alessioc/UNIS_hydrographic_data_to_cfnetcdf/data/transformed_data/CTD_all_1876-2019.nc'

# Run the function to fix coordinates
fix_coordinates(file_path)

