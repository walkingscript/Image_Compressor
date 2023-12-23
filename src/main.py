import sys
from os import PathLike, mkdir, chdir
from os.path import abspath, exists as path_exists
from pathlib import Path
from typing import Iterable

from PIL import Image

DIR_NAME = 'compressed_files'


def save_as_jpg_files(path_list: Iterable[PathLike]) -> None:
    path_list = list(map(lambda x: Path(abspath(x)), path_list))
    if len(path_list) > 1:
        if not path_exists(DIR_NAME):
            mkdir(DIR_NAME)
        chdir(DIR_NAME)
    for path in path_list:
        with Image.open(path) as image:
            rgb_image = image.convert('RGB')
            rgb_image.save(f'{path.name}.jpg')


def main(args):
    if len(args) == 1:
        sys.exit()
    files = args[1:]
    save_as_jpg_files(files)


if __name__ == '__main__':
    main(sys.argv)
