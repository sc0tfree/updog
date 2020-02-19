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
    for file in directory_files:
        if file.is_dir():
            size = '--'
            size_sort = -1
        else:
            size = human_readable_file_size(file.stat().st_size)
            size_sort = file.stat().st_size
        files.append({
            'name': file.name,
            'is_dir': file.is_dir(),
            'rel_path': get_relative_path(file.path, base_directory),
            'size': size,
            'size_sort': size_sort,
            'last_modified': ctime(file.stat().st_mtime),
            'last_modified_sort': file.stat().st_mtime
        })
    return files


def get_parent_directory(path, base_directory):
    difference = get_relative_path(path, base_directory)
    difference_fields = difference.split('/')
    if len(difference_fields) == 1:
        return ''
    else:
        return '/'.join(difference_fields[:-1])
