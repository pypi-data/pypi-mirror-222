""" this module contains functions to scan all files in a directory """

import os
import pandas as pd
import hashlib
from collections import Counter
from pathlib import Path


def _replace_backslash(dir_path: str) -> str:
    """
    It takes a string as input and returns a string with all the backslashes replaced with forward
    slashes

    Args:
      dir_path (str): The path to the directory you want to convert.

    Returns:
      the string (path) with the backslash replaced with a forward slash.
    """
    return str(dir_path).replace(os.path.sep, "/")


def _create_hash(text: str) -> str:
    """
    It takes a string and returns the has value of that string using the MD5 hashing algorithm

    Args:
      text (str): The text to be hashed.

    Returns:
      A hash of the text.
    """
    return str(hashlib.md5(text.encode("utf-8")).hexdigest())


def _get_extension(filepath: str) -> str:
    """
    It takes a filepath as a string, splits it into the filename and extension, and converts
    the extension to lowercase

    Args:
      filepath (str): The path to the file you want to get the extension of.

    Returns:
      The file extension of the filepath.
    """
    filename = _replace_backslash(filepath).split("/")[-1]
    if filename.find(".") > -1:
        return filename.split(".")[-1].lower()
    else:
        return ""


def _get_extension_list(list_files: list[str]) -> list[str]:
    """
    It takes a list of files, and returns a list with only the file extensions

    Args:
      list_files (list[str]): a list of filenames (which can include the filepath)

    Returns:
      A list of strings (file extensions)
    """
    assert isinstance(list_files, list), "Input should be a list of strings"
    assert all(
        isinstance(elem, str) for elem in list_files
    ), "Input should be a list of strings"
    assert len(list_files) > 0, "Input is an empty list"

    all_extensions = list(map(_get_extension, list_files))
    return all_extensions


def _get_filesize(filepath: str) -> int:
    """
    > This function returns the size of a file in bytes

    Args:
      filepath (str): The path to the file you want to get the size of.

    Returns:
      The size of the file in bytes.
    """
    try:
        size = os.path.getsize(filepath)
    except FileNotFoundError:
        size = None
    return size


def _get_filesize_list(list_files: list[str]) -> list[int]:
    """
    This function takes a list of file names and returns a list of file sizes in bytes

    Args:
      list_files (list[str]): list[str]

    Returns:
      A list of integers
    """
    assert isinstance(list_files, list), "Input should be a list of strings"
    assert all(
        isinstance(elem, str) for elem in list_files
    ), "Input should be a list of strings"
    assert len(list_files) > 0, "Input is an empty list"

    all_sizes = list(map(_get_filesize, list_files))
    return all_sizes


def list_all_files(dir_path: str) -> dict:
    """
    It takes a directory path as input and returns a dict of file paths.

    Args:
      dir_path (str): The path to the directory containing the files.

    Returns:
      A dict of strings.
    """
    dir_path = _replace_backslash(dir_path)

    if not os.path.exists(dir_path):
        raise ValueError(f"The directory doesn't exist.")

    if not os.path.isdir(dir_path):
        raise ValueError(f"The path doesn't point to a directory.")

    file_paths = []
    for dirname, _, files in os.walk(dir_path):
        file_paths += [os.path.join(dirname, entry) for entry in files]

    if len(file_paths) == 0:
        raise ValueError(f"Could not find any files in the directory.")

    file_paths = list(map(_replace_backslash, file_paths))

    return _create_file_dict(file_paths)


def extension_stats(dict_files: list[str]) -> pd.DataFrame:
    """
    It takes a list of files and returns a dataframe with the number of files per extension

    Args:
      list_files (list[str]): list[str]

    Returns:
      A dataframe with the extension and the count of files with that extension.
    """
    all_extensions = [d["extension"] for d in dict_files.values()]

    # count nr of files per extensions
    count_extensions = Counter([ext for ext in all_extensions])
    df_ext_stats = pd.DataFrame.from_dict(
        count_extensions, orient="index"
    ).reset_index()
    df_ext_stats.columns = ["extension", "count"]
    df_ext_stats = df_ext_stats.sort_values(by="count", ascending=False)
    return df_ext_stats


def _create_file_dict(list_files: list[str]) -> dict:
    """
    It takes a list of file paths and returns a dictionary of file paths with their corresponding hash, extension and size

    Args:
      list_files (list[str]): list[str]

    Returns:
      A dictionary of dictionaries with information about the files.
    """
    all_extensions = _get_extension_list(list_files=list_files)
    all_sizes = _get_filesize_list(list_files=list_files)
    file_dict = {
        _create_hash(list_files[i]): {
            "filepath": list_files[i],
            "filename": Path(list_files[i]).name,
            "extension": all_extensions[i],
            "filesize": all_sizes[i],
        }
        for i in range(len(list_files))
    }
    return file_dict


def select_files(
    dict_files: dict,
    include: list[str] = None,
    exclude: list[str] = None,
    size_cap_mb: float = None,
) -> dict:
    """
    It takes a dict of files, and returns a list of files that have extensions that are in the include
    list, but not in the exclude list.
    Optionally only select files of less MB than stated in the size_cap_mb.

    Args:
      dict_files (dict): dict
      include (list[str]): list[str] = None
      exclude (list[str]): list[str] = None
      size_cap_mb (float): float = None

    Returns:
      capped_file_list
    """

    if size_cap_mb is not None:
        dict_files = {
            k: v
            for k, v in dict_files.items()
            if (v["filesize"] == None) or (v["filesize"] / 1024 / 1000 <= size_cap_mb)
        }

    if include is not None:
        assert isinstance(
            include, list
        ), "Include parameter should be a list of strings"
        assert all(
            isinstance(elem, str) for elem in include
        ), "Include parameter should be a list of strings"
        assert len(include) > 0, "Include parameter is an empty list"
        include = [elem.lower() for elem in include]

    if exclude is not None:
        assert isinstance(
            exclude, list
        ), "Exclude parameter should be a list of strings"
        assert all(
            isinstance(elem, str) for elem in exclude
        ), "Exclude parameter should be a list of strings"
        assert len(exclude) > 0, "Exclude parameter is an empty list"
        exclude = [elem.lower() for elem in exclude]

    if (include is not None) and (exclude is not None):
        dict_files = {
            k: v
            for k, v in dict_files.items()
            if (v["extension"] in include) and (v["extension"] not in exclude)
        }
    elif (include is None) and (exclude is not None):
        dict_files = {k: v for k, v in dict_files.items() if (v["extension"] not in exclude)}
    elif (include is not None) and (exclude is None):
        dict_files = {k: v for k, v in dict_files.items() if (v["extension"] in include)}
    else:
        dict_files

    return dict_files
