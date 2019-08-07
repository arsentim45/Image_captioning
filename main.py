import argparse


from Parser.Shutterstock_parser import get_images
from Database.database_creator import creator
from Database.database_operations import add_photo, get_photos


def main(params):
    download_data = params['download_data']
    number_of_images = params['number_of_images']
    section = params['section']
    folder = params['section']
    get_data = params['get_data']

    if download_data:
        creator()
        pictures = get_images(number_of_images, section, folder)
        for pic in pictures:
            add_photo(pic[0], pic[1])
    if get_data:
        pictures = get_photos()
        return pictures


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number_of_images', default=10, type=int, help='number of images to download')
    parser.add_argument('-s', '--section', default='', type=str, help='type of pictures to search for')
    parser.add_argument('-f', '--folder', default='', type=str, help='folder where to download')
    parser.add_argument('-g', '--get_data', default=False, type=bool,
                        help='return data from database or no(False/True)')
    parser.add_argument('-d', '--download_data', default=True, type=bool,
                        help='put data into database or no(False/True)')
    args = parser.parse_args()
    params = vars(args)
    main(params)
