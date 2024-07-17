import os

def run_script(script_name):
    exit_code = os.system(f'python3 {script_name}')
    if exit_code == 0:
        print(f"Successfully ran {script_name}")
    else:
        print(f"Error running {script_name} with exit code {exit_code}")

def main():
    scripts = ['generate_cfnetcdf_parent_file.py',
               'change_parent_coord_attr.py',
               'generate_cfnetcdf_child_files.py',
               'change_dim_cfnetcdf_child_files.py',
               'check_long_name_and_coverage_content_type.py']
   
    for script in scripts:
        run_script(script)

if __name__ == "__main__":
    main()