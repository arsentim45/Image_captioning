# **How to use:**
1. you can install deps, which is in are *requirements.txt* file
2. running main.py with arguments:

        ('-n', '--number_of_images', default=10, type=int, help='number of images to download')

        ('-s', '--section', default='', type=str, help='type of pictures to search for')

        ('-f', '--folder', default='', type=str, help='folder where to download')

        ('-g', '--get_data', default=False, type=bool, help='return data from database or no(False/True)')

        ('-d', '--download_data', default=True, type=bool,
                        help='put data into database or no(False/True)')
3. You can download only pictures using --download_data=True which is set by default
or use --get_data=True to get all data and main will return all pictures in database you can modify main.py for further
usage of the data you can get