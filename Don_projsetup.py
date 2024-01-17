# Don_analytics_utils.py
byline = "Don_analytics_utils Module"


# project_folder_creator.py
'''
This module provides functions for creating a series of project folders.
'''

import pathlib
import time
import Don_analytics_utils

def create_folders_for_range(start_year, end_year):
    '''
    Create folders for a given range of years.

    Args:
        start_year (int): The starting year.
        end_year (int): The ending year.

    Returns:
        None
    '''
    for year in range(start_year, end_year + 1):
        folder_path = pathlib.Path.cwd().joinpath(str(year))
        print(f"Creating folder: {folder_path}")
        folder_path.mkdir(exist_ok=True)

def create_folders_from_list(folder_list, to_lowercase=False, remove_spaces=False):
    '''
    Create folders from a list of names.

    Args:
        folder_list (list): List of folder names.
        to_lowercase (bool): Convert folder names to lowercase.
        remove_spaces (bool): Remove spaces from folder names.

    Returns:
        None
    '''
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(' ', '')
        folder_path = pathlib.Path.cwd().joinpath(folder_name)
        print(f"Creating folder: {folder_path}")
        folder_path.mkdir(exist_ok=True)

def create_prefixed_folders(folder_list, prefix):
    '''
    Create prefixed folders using list comprehension.

    Args:
        folder_list (list): List of folder names.
        prefix (str): Prefix to be added to each folder name.

    Returns:
        None
    '''
    folder_paths = [pathlib.Path.cwd().joinpath(prefix + name) for name in folder_list]
    for folder_path in folder_paths:
        print(f"Creating folder: {folder_path}")
        folder_path.mkdir(exist_ok=True)

def create_folders_periodically(duration_secs):
    '''
    Create folders periodically using a while loop.

    Args:
        duration_secs (int): Duration in seconds.

    Returns:
        None
    '''
    start_time = time.time()
    while time.time() - start_time < duration_secs:
        timestamp = time.strftime('%Y%m%d%H%M%S')
        folder_path = pathlib.Path.cwd().joinpath(f"periodic_folder_{timestamp}")
        print(f"Creating folder: {folder_path}")
        folder_path.mkdir(exist_ok=True)
        time.sleep(1)  # Sleep for 1 second between folder creations

def main():
    '''
    Main function to demonstrate module capabilities.
    '''
    # Print byline from imported module
    print(f"Byline: {Don_analytics_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces
    # to one or more of your functions (e.g. function 2)
    # Call your function and test these options
    regions = [
      "North America",
      "South America",
      "Europe",
      "Asia",
      "Africa",
      "Oceania",
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

# Conditional Script Execution
if __name__ == '__main__':
    main()
