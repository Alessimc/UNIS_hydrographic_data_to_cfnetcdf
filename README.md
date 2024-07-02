# UNIS_hydrographic_data_to_cfnetcdf

Download and transform hydrographic data from UNIS to CF-NetCDF

The dataset hosted at https://data.npolar.no/dataset/39d9f0f9-af12-420c-a879-10990df2e22d and described in https://sios-svalbard.org/metsis/search?search_api_fulltext_op=and&fulltext=39d9f0f9-af12-420c-a879-10990df2e22d&start_date=&end_date=&items_per_page=15&f\[0\]=dataset_level%3ALevel-1 is downloaded and converted into CF-NetCDF for inclusion into the BlueCloud relevant data for SIOS. We keep as much as possible of the metadata and the DOI at NPI as well as the landing page.

The resulting data will be made available through ADC at MET as a cached dataset to serve the needs of BlueCloud.

Scripts used for data transformation are:
- generate_cfnetcdf_child_files.py then change_dim_cfnetcdf_child_files.py
- generate_cfnetcdf_parent_file.py

MET ACDD Requirements are checked using
- check_for_met_ACDD.py

Notebooks are messy and only used for testing and exploratory analysis.

unzip.py is a helper file that unzips data and allocates it to a specified directory.
