import xarray as xr
from pathlib import Path

# MET required attributes
required_attributes = {
    "id": "Required if not hosted by MET",
    "naming_authority": "Required if not hosted by MET",
    "title": "Required",
    "summary": "Required",
    "keywords": "Required, GCMD Science Keywords",
    "keywords_vocabulary": "Required, GCMD Science Keywords",
    "geospatial_lat_min": "Required",
    "geospatial_lat_max": "Required",
    "geospatial_lon_min": "Required",
    "geospatial_lon_max": "Required",
    "time_coverage_start": "Required",
    "time_coverage_end": "Required",
    "Conventions": "Required",
    "history": "Required",
    "date_created": "Required",
    "creator_type": "Required",
    "creator_institution": "Required",
    "creator_name": "Required",
    "creator_email": "Required",
    "creator_url": "Required",
    "publisher_name": "Required if not hosted by MET",
    "publisher_email": "Required if not hosted by MET",
    "publisher_url": "Required if not hosted by MET",
    "project": "Required",
    "license": "Required"
}


def missing_MET_ACDD_attributes(file_path):
    file_path = Path(file_path)
    # Open the NetCDF file using xarray
    with xr.open_dataset(file_path) as ds:
        # Get the global attributes
        global_attrs = ds.attrs
        
        # Initialize lists to store missing and empty attributes
        missing_attributes = []
        empty_attributes = []
        
        # Check each required attribute
        for attr, description in required_attributes.items():
            if attr not in global_attrs:
                missing_attributes.append(attr)
            elif global_attrs[attr] is None or global_attrs[attr] == '':
                empty_attributes.append(attr)
        
        # Print the results
        if missing_attributes or empty_attributes:
            print(f"{file_path} is missing or has empty the following required attributes:")
            for attr in missing_attributes:
                print(f"  - {attr}: {required_attributes[attr]} (MISSING)")
            for attr in empty_attributes:
                print(f"  - {attr}: {required_attributes[attr]} (EMPTY)")
        else:
            print(f"{file_path} has all required attributes and they are non-empty.")
