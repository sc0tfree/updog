import os

from math import log2
from time import ctime


def is_valid_subpath(relative_directory, base_directory):
    in_question = os.path.abspath(os.path.join(base_directory, relative_directory))
    return os.path.commonprefix([base_directory, in_question]) == base_directory


def is_valid_upload_path(path, base_directory):
    if path == '':
        return False
    in_question = os.path.abspath(path)
    return os.path.commonprefix([base_directory, in_question]) == base_directory


def get_relative_path(file_path, base_directory):
    return file_path.split(os.path.commonprefix([base_directory, file_path]))[1][1:]


def human_readable_file_size(size):
    # Taken from Dipen Panchasara
    # https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
    _suffixes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    order = int(log2(size) / 10) if size else 0
    return '{:.4g} {}'.format(size / (1 << (order * 10)), _suffixes[order])


def process_files(directory_files, base_directory):
    files = []
    for file_entry in directory_files:

        real_path = os.path.realpath(os.path.join(base_directory, file_entry.name))

        # Default size
        size = '--'
        size_sort = -1

        if os.path.isfile(real_path):
            # Item is a file or a symlink points to a real file
            size_sort = file_entry.stat().st_size
            size = human_readable_file_size(size_sort)

        last_modified = '???'
        last_modified_sort = -1
        if os.path.exists(real_path):
            last_modified_sort = file_entry.stat().st_mtime
            last_modified = ctime(last_modified_sort)

        files.append({
            'name': file_entry.name,
            'is_dir': file_entry.is_dir(),
            'rel_path': get_relative_path(file_entry.path, base_directory),
            'size': size,
            'size_sort': size_sort,
            'last_modified': last_modified,
            'last_modified_sort': last_modified_sort,
            'is_symlink': file_entry.is_symlink(),
            'exists': os.path.exists(real_path)
        })
    return files


def get_parent_directory(path, base_directory):
    difference = get_relative_path(path, base_directory)
    difference_fields = difference.split('/')
    if len(difference_fields) == 1:
        return ''
    else:
        return '/'.join(difference_fields[:-1])
