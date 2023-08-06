"""This module tests the methods of the file_index module in file_index.py."""

import os
import pytest
from pathlib import Path
import pandas as pd
from drivescanner import file_index


class TestReplaceBackslash:
    """
    all tests for _replace_backslash in file_index module
        bad argument:
            none
        special argument:
            none
        normal argument:
            a filepath
    """

    test = [
        ("this\\is\\a\\path\\test.csv", "this/is/a/path/test.csv"),
        ("this/is/also/a/path/test.csv", "this/is/also/a/path/test.csv"),
        (123, "123"),
        ("thisisnotapath", "thisisnotapath"),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_replace_backslash_normal_arguments(self, input, expected):
        assert file_index._replace_backslash(input) == expected


class TestCreateHash:
    """
    all tests for _create_hash in ingest module
        bad argument:
            none
        special argument:
            none
        normal argument:
            a string
    """

    test = [
        ("123", "202cb962ac59075b964b07152d234b70"),
        ("hello", "5d41402abc4b2a76b9719d911017c592"),
        ("this/is/a/pretend/path.file.txt", "7bfe3fa8f1db826321827dccf9e6fd62"),
        (
            "this/is/a/pretend/path&fileto(&%$#@!).txt",
            "68347fa29b0fe07da89e8c182b502708",
        ),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_create_hash_normal_arguments(self, input, expected):
        result = file_index._create_hash(input)
        assert (
            result == expected
        ), f"the expected hash for {input} was {expected}, but the hash is {result}"


class TestGetExtension:
    """
    all tests for _get_extension in file_index module
        bad argument:
            none
        special argument:
            none
        normal argument:
            a string (which should be a filepath)
    """

    test = [
        ("just\\some\\path/test1.Csv", "csv"),
        ("test2.myfile.xlsx", "xlsx"),
        ("test3.txt", "txt"),
        ("test4.pptx", "pptx"),
        ("test5.PDF", "pdf"),
        ("test6.json", "json"),
        ("test7", ""),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_get_extension_normal_input(self, input, expected):
        assert file_index._get_extension(input) == expected


class TestGetExtensionList:
    """
    all tests for _get_extension_list in file_index module
        bad argument:
            input is not a list
            input is a list, but not of strings
            list is empty
        special argument:
            none
        normal argument:
            a list of files as strings
    """

    def test_get_extension_list_no_list(self):
        with pytest.raises(AssertionError, match=f"Input should be a list of strings"):
            file_index._get_extension_list(list_files="test")

    def test_get_extension_list_not_list_of_strings(self):
        with pytest.raises(AssertionError, match=f"Input should be a list of strings"):
            file_index._get_extension_list(list_files=[1, 2, 3])

    def test_get_extension_list_empty_list(self):
        with pytest.raises(AssertionError, match=f"Input is an empty list"):
            file_index._get_extension_list(list_files=[])

    test = [
        (
            [
                "test1.Csv",
                "test2.xlsx",
                "test3.txt",
                "test4.pptx",
                "test5.PDF",
                "test6.json",
                "test7",
            ],
            ["csv", "xlsx", "txt", "pptx", "pdf", "json", ""],
        ),
        (
            [
                "test1.csv",
                "test2.xlsx",
                "test3.txt",
                "test4.pptx",
                "test5.pdf",
                "test6.json",
                "test7.txt",
                "test8.txt",
            ],
            ["csv", "xlsx", "txt", "pptx", "pdf", "json", "txt", "txt"],
        ),
        (
            [
                "test1.csv",
                "test2.xlsx",
                "test3.txt",
                "test4.pptx",
                "test5.pdf",
                "test6.json",
                "test7.txt",
                "test8.json",
            ],
            ["csv", "xlsx", "txt", "pptx", "pdf", "json", "txt", "json"],
        ),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_get_extension_list_normal_input(self, input, expected):
        assert file_index._get_extension_list(input) == expected


class TestGetFilesize:
    """
    Test the function _get_filesize from file_index
    bad argument:
        none
    special argument:
        file does not exist
    normal argument:
        a filepath
    """

    def test_get_filesize(self, my_tmp_dir):
        dir_path = Path(my_tmp_dir)
        input = [
            os.path.join(dir_path, "example_1.csv"),
            os.path.join(dir_path, "example_2.pdf"),
            os.path.join(dir_path, "example_3.txt"),
            os.path.join(dir_path, "example_4.pptx"),
            os.path.join(dir_path, "example_5.json"),
            os.path.join(dir_path, "example_6.xlsx"),
            os.path.join(dir_path, "example_10.csv"),
        ]
        expected = [10, 14, 14, 14, 14, 14, None]
        result = []
        for filepath in input:
            result.append(file_index._get_filesize(filepath))
        assert all(
            [x == y for x, y in zip(result, expected)]
        ), f"Expected: {expected}, Actual: {result}"


class TestGetFilesizeList:
    """
    Test the function get_filesize_list from file_index
    bad argument:
        none
    special argument:
        none
    normal argument:
        a list of filepaths (existing or non-existing files)
    """

    def test_get_filesize_list_1(self, my_tmp_dir):
        dir_path = Path(my_tmp_dir)
        input = [
            os.path.join(dir_path, "example_1.csv"),
            os.path.join(dir_path, "example_2.pdf"),
            os.path.join(dir_path, "example_3.txt"),
            os.path.join(dir_path, "example_4.pptx"),
            os.path.join(dir_path, "example_5.json"),
            os.path.join(dir_path, "example_6.xlsx"),
            os.path.join(dir_path, "example_10.csv"),
        ]
        expected = [10, 14, 14, 14, 14, 14, None]
        result = file_index._get_filesize_list(input)
        assert all(
            [x == y for x, y in zip(result, expected)]
        ), f"Expected: {expected}, Actual: {result}"

    def test_get_filesize_list_2(self, my_tmp_dir_one_subdir):
        dir_path = Path(my_tmp_dir_one_subdir)
        input = [
            os.path.join(dir_path, "example_10.csv"),
            os.path.join(dir_path, "example_12.pdf"),
            os.path.join(dir_path, "example_13.txt"),
            os.path.join(dir_path, "1_subdirectory", "example_14.pptx"),
            os.path.join(dir_path, "1_subdirectory", "example_15.json"),
            os.path.join(dir_path, "1_subdirectory", "example_16.xlsx"),
        ]
        expected = [10, 14, 14, 14, 14, 14]
        result = file_index._get_filesize_list(input)
        assert all(
            [x == y for x, y in zip(result, expected)]
        ), f"Expected: {expected}, Actual: {result}"

    def test_get_filesize_list_3(self, my_tmp_dir_multiple_subdir):
        dir_path = Path(my_tmp_dir_multiple_subdir)
        input = [
            os.path.join(dir_path, "example_20.csv"),
            os.path.join(dir_path, "example_22.pdf"),
            os.path.join(dir_path, "example_23.txt"),
            os.path.join(dir_path, "1_subdirectory", "example_24.pptx"),
            os.path.join(
                dir_path, "1_subdirectory", "2_subdirectory", "example_25.json"
            ),
            os.path.join(
                dir_path, "1_subdirectory", "2_subdirectory", "example_26.xlsx"
            ),
        ]
        expected = [10, 14, 14, 14, 14, 14]
        result = file_index._get_filesize_list(input)
        assert all(
            [x == y for x, y in zip(result, expected)]
        ), f"Expected: {expected}, Actual: {result}"


class TestListAllFiles:
    """
    all tests for list_all_files in file_index module
        bad argument:
            path doesn't exist
            no files in directory
            path doesn't point to a directory
        special argument:
            none
        normal argument:
            list all files in a directory
            list all files in a directory with one subdirectory (also with files in it)
            list all files in a directory with two subdirectories (also with files in them)
    """

    def test_list_all_files_loc_not_exists(self, my_tmp_dir):
        dir_path = os.path.join(Path(my_tmp_dir), "my_nonexisting_directory")
        with pytest.raises(ValueError, match=f"The directory doesn't exist."):
            file_index.list_all_files(dir_path=dir_path)

    def test_list_all_files_no_files(self, my_empty_tmp_dir):
        dir_path = Path(my_empty_tmp_dir)
        with pytest.raises(
            ValueError, match=f"Could not find any files in the directory."
        ):
            file_index.list_all_files(dir_path=dir_path)

    def test_list_all_files_loc_not_dir(self, my_tmp_dir):
        dir_path = os.path.join(Path(my_tmp_dir), "example_1.csv")
        with pytest.raises(ValueError, match=f"The path doesn't point to a directory."):
            file_index.list_all_files(dir_path=dir_path)

    def test_list_all_files(self):
        result = file_index.list_all_files(
            dir_path="tests/testfiles/mysubfolderforfileindex"
        )
        expected = {
            "39fb72233f11607b325791982114fb74": {
                "filepath": "tests/testfiles/mysubfolderforfileindex/circuits.csv",
                "filename": "circuits.csv",
                "extension": "csv",
                "filesize": 8667,
            },
            "e36faa69cb748215e2ec00fed27badca": {
                "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xls",
                "filename": "Excel test Excel.xls",
                "extension": "xls",
                "filesize": 26112,
            },
            "8ef834c3461a7665ab8f6da2f8158c1a": {
                "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xlsx",
                "filename": "Excel test Excel.xlsx",
                "extension": "xlsx",
                "filesize": 9217,
            },
            "e4896cf93bfd7f9f170a526e530f8c9e": {
                "filepath": "tests/testfiles/mysubfolderforfileindex/HTM test.htm",
                "filename": "HTM test.htm",
                "extension": "htm",
                "filesize": 233,
            },
            "0209a7022087172f346ec133f28a1926": {
                "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/Lipsum_2.txt",
                "filename": "Lipsum_2.txt",
                "extension": "txt",
                "filesize": 116,
            },
            "778eba7ddc5ee844fcfae877843839d2": {
                "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/mysecondsubfolder/Lipsum_3.txt",
                "filename": "Lipsum_3.txt",
                "extension": "txt",
                "filesize": 116,
            },
        }
        assert result == expected, f"Expected: {expected}, Actual: {result}"


class TestExtensionStats:
    # """
    # all tests for extension_stats in file_index module
    # bad argument:
    # none
    # special argument:
    # none
    # normal argument:
    # list doesn't contain files
    # a list with paths to files (as strings)
    # """

    test = [
        (
            {
                "a": {"extension": ""},
                "b": {"extension": ""},
                "c": {"extension": ""},
                "d": {"extension": ""},
                "e": {"extension": ""},
                "f": {"extension": ""},
                "g": {"extension": ""},
            },
            pd.DataFrame(
                data=[
                    ("", 7),
                ],
                columns=["extension", "count"],
            ),
        ),
        (
            {
                "a": {"extension": "csv"},
                "b": {"extension": "pdf"},
                "c": {"extension": "txt"},
                "d": {"extension": "pptx"},
                "e": {"extension": "json"},
                "f": {"extension": "xlsx"},
                "g": {"extension": ""},
            },
            pd.DataFrame(
                data=[
                    ("csv", 1),
                    ("pdf", 1),
                    ("txt", 1),
                    ("pptx", 1),
                    ("json", 1),
                    ("xlsx", 1),
                    ("", 1),
                ],
                columns=["extension", "count"],
            ),
        ),
        (
            {
                "a": {"extension": "csv"},
                "b": {"extension": "xlsx"},
                "c": {"extension": "txt"},
                "d": {"extension": "pptx"},
                "e": {"extension": "pdf"},
                "f": {"extension": "json"},
                "g": {"extension": "txt"},
                "h": {"extension": "txt"},
            },
            pd.DataFrame(
                data=[
                    ("csv", 1),
                    ("pdf", 1),
                    ("txt", 3),
                    ("pptx", 1),
                    ("json", 1),
                    ("xlsx", 1),
                ],
                columns=["extension", "count"],
            ),
        ),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_extension_stats_normal_input(self, input, expected):
        result = file_index.extension_stats(dict_files=input)
        result = result.sort_values(by=["extension", "count"]).reset_index(drop=True)
        expected = expected.sort_values(by=["extension", "count"]).reset_index(
            drop=True
        )
        pd.testing.assert_frame_equal(result, expected, check_like=True)


class TestSelectFiles:
    """
    all tests for select_files in file_index module
        bad argument:
            include is not a list or None
            exclude is not a list or None
            include is not a list of strings
            exclude is not a list of strings
            include is an empty list
            exclude is an empty list
        special argument:
            none
        normal argument:
            a list with paths to files (as strings)
    """

    def test_select_files_include_no_list(self):
        with pytest.raises(
            AssertionError, match=f"Include parameter should be a list of strings"
        ):
            file_index.select_files(dict_files={}, include="123", exclude=None)

    def test_select_files_include_not_list_of_strings(self):
        with pytest.raises(
            AssertionError, match=f"Include parameter should be a list of strings"
        ):
            file_index.select_files(dict_files={}, include=[1, 2, 3], exclude=None)

    def test_select_files_include_empty_list(self):
        with pytest.raises(AssertionError, match=f"Include parameter is an empty list"):
            file_index.select_files(dict_files={}, include=[], exclude=None)

    def test_select_files_exclude_no_list(self):
        with pytest.raises(
            AssertionError, match=f"Exclude parameter should be a list of strings"
        ):
            file_index.select_files(dict_files={}, include=None, exclude="123")

    def test_select_files_exclude_not_list_of_strings(self):
        with pytest.raises(
            AssertionError, match=f"Exclude parameter should be a list of strings"
        ):
            file_index.select_files(dict_files={}, include=None, exclude=[1, 2, 3])

    def test_select_files_exclude_empty_list(self):
        with pytest.raises(AssertionError, match=f"Exclude parameter is an empty list"):
            file_index.select_files(dict_files={}, include=None, exclude=[])

    base_dict = {
        "39fb72233f11607b325791982114fb74": {
            "filepath": "tests/testfiles/mysubfolderforfileindex/circuits.csv",
            "filename": "circuits.csv",
            "extension": "csv",
            "filesize": 8667,
        },
        "e36faa69cb748215e2ec00fed27badca": {
            "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xls",
            "filename": "Excel test Excel.xls",
            "extension": "xls",
            "filesize": 26112,
        },
        "8ef834c3461a7665ab8f6da2f8158c1a": {
            "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xlsx",
            "filename": "Excel test Excel.xlsx",
            "extension": "xlsx",
            "filesize": 9217,
        },
        "e4896cf93bfd7f9f170a526e530f8c9e": {
            "filepath": "tests/testfiles/mysubfolderforfileindex/HTM test.htm",
            "filename": "HTM test.htm",
            "extension": "htm",
            "filesize": 233,
        },
        "0209a7022087172f346ec133f28a1926": {
            "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/Lipsum_2.txt",
            "filename": "Lipsum_2.txt",
            "extension": "txt",
            "filesize": 116,
        },
        "778eba7ddc5ee844fcfae877843839d2": {
            "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/mysecondsubfolder/Lipsum_3.txt",
            "filename": "Lipsum_3.txt",
            "extension": "txt",
            "filesize": 116,
        },
    }

    test = [
        (
            base_dict,
            None,
            None,
            None,
            {
                "39fb72233f11607b325791982114fb74": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/circuits.csv",
                    "filename": "circuits.csv",
                    "extension": "csv",
                    "filesize": 8667,
                },
                "e36faa69cb748215e2ec00fed27badca": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xls",
                    "filename": "Excel test Excel.xls",
                    "extension": "xls",
                    "filesize": 26112,
                },
                "8ef834c3461a7665ab8f6da2f8158c1a": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xlsx",
                    "filename": "Excel test Excel.xlsx",
                    "extension": "xlsx",
                    "filesize": 9217,
                },
                "e4896cf93bfd7f9f170a526e530f8c9e": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/HTM test.htm",
                    "filename": "HTM test.htm",
                    "extension": "htm",
                    "filesize": 233,
                },
                "0209a7022087172f346ec133f28a1926": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/Lipsum_2.txt",
                    "filename": "Lipsum_2.txt",
                    "extension": "txt",
                    "filesize": 116,
                },
                "778eba7ddc5ee844fcfae877843839d2": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/mysecondsubfolder/Lipsum_3.txt",
                    "filename": "Lipsum_3.txt",
                    "extension": "txt",
                    "filesize": 116,
                },
            },
        ),
        (
            base_dict,
            None,
            ["CSV"],
            None,
            {
                "e36faa69cb748215e2ec00fed27badca": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xls",
                    "filename": "Excel test Excel.xls",
                    "extension": "xls",
                    "filesize": 26112,
                },
                "8ef834c3461a7665ab8f6da2f8158c1a": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xlsx",
                    "filename": "Excel test Excel.xlsx",
                    "extension": "xlsx",
                    "filesize": 9217,
                },
                "e4896cf93bfd7f9f170a526e530f8c9e": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/HTM test.htm",
                    "filename": "HTM test.htm",
                    "extension": "htm",
                    "filesize": 233,
                },
                "0209a7022087172f346ec133f28a1926": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/Lipsum_2.txt",
                    "filename": "Lipsum_2.txt",
                    "extension": "txt",
                    "filesize": 116,
                },
                "778eba7ddc5ee844fcfae877843839d2": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/mysecondsubfolder/Lipsum_3.txt",
                    "filename": "Lipsum_3.txt",
                    "extension": "txt",
                    "filesize": 116,
                },
            },
        ),
        (
            base_dict,
            ["Xlsx"],
            None,
            None,
            {
                "8ef834c3461a7665ab8f6da2f8158c1a": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xlsx",
                    "filename": "Excel test Excel.xlsx",
                    "extension": "xlsx",
                    "filesize": 9217,
                }
            },
        ),
        (
            base_dict,
            ["csv", "xls", "htm"],
            ["TXT"],
            None,
            {
                "39fb72233f11607b325791982114fb74": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/circuits.csv",
                    "filename": "circuits.csv",
                    "extension": "csv",
                    "filesize": 8667,
                },
                "e36faa69cb748215e2ec00fed27badca": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xls",
                    "filename": "Excel test Excel.xls",
                    "extension": "xls",
                    "filesize": 26112,
                },
                "e4896cf93bfd7f9f170a526e530f8c9e": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/HTM test.htm",
                    "filename": "HTM test.htm",
                    "extension": "htm",
                    "filesize": 233,
                },
            },
        ),
        (
            base_dict,
            ["csv", "xls", "htm"],
            ["XLS"],
            None,
            {
                "39fb72233f11607b325791982114fb74": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/circuits.csv",
                    "filename": "circuits.csv",
                    "extension": "csv",
                    "filesize": 8667,
                },
                "e4896cf93bfd7f9f170a526e530f8c9e": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/HTM test.htm",
                    "filename": "HTM test.htm",
                    "extension": "htm",
                    "filesize": 233,
                },
            },
        ),
        (
            base_dict,
            None,
            None,
            0.01,
            {
                "39fb72233f11607b325791982114fb74": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/circuits.csv",
                    "filename": "circuits.csv",
                    "extension": "csv",
                    "filesize": 8667,
                },
                "8ef834c3461a7665ab8f6da2f8158c1a": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xlsx",
                    "filename": "Excel test Excel.xlsx",
                    "extension": "xlsx",
                    "filesize": 9217,
                },
                "e4896cf93bfd7f9f170a526e530f8c9e": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/HTM test.htm",
                    "filename": "HTM test.htm",
                    "extension": "htm",
                    "filesize": 233,
                },
                "0209a7022087172f346ec133f28a1926": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/Lipsum_2.txt",
                    "filename": "Lipsum_2.txt",
                    "extension": "txt",
                    "filesize": 116,
                },
                "778eba7ddc5ee844fcfae877843839d2": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/mysecondsubfolder/Lipsum_3.txt",
                    "filename": "Lipsum_3.txt",
                    "extension": "txt",
                    "filesize": 116,
                },
            },
        ),
        (
            base_dict,
            ["xls"],
            None,
            0.01,
            {},
        ),
        (
            base_dict,
            None,
            ["csv", "json"],
            0.01,
            {
                "8ef834c3461a7665ab8f6da2f8158c1a": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xlsx",
                    "filename": "Excel test Excel.xlsx",
                    "extension": "xlsx",
                    "filesize": 9217,
                },
                "e4896cf93bfd7f9f170a526e530f8c9e": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/HTM test.htm",
                    "filename": "HTM test.htm",
                    "extension": "htm",
                    "filesize": 233,
                },
                "0209a7022087172f346ec133f28a1926": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/Lipsum_2.txt",
                    "filename": "Lipsum_2.txt",
                    "extension": "txt",
                    "filesize": 116,
                },
                "778eba7ddc5ee844fcfae877843839d2": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/mysecondsubfolder/Lipsum_3.txt",
                    "filename": "Lipsum_3.txt",
                    "extension": "txt",
                    "filesize": 116,
                },
            },
        ),
    ]

    @pytest.mark.parametrize("input, include, exclude, size_cap_mb, expected", test)
    def test_select_files_normal_input(
        self, input, include, exclude, size_cap_mb, expected
    ):
        assert file_index.select_files(input, include, exclude, size_cap_mb) == expected


class TestCreateFileDict:
    """
    all tests for create_file_dict in file_index module
        bad argument:
            none
        special argument:
            none
        normal argument:
            a list with paths to files (as strings)
    """

    test = [
        (
            [
                "test1.Csv",
                "test2.xlsx",
                "test3.txt",
                "test4.pptx",
                "test5.PDF",
                "test6.json",
                "test7",
            ],
            {
                "63dc5420b1e2c67f2696d0f8245e71d8": {
                    "filepath": "test1.Csv",
                    "filename": "test1.Csv",
                    "extension": "csv",
                    "filesize": None,
                },
                "6fac7fa087d81047bb6135feb6023162": {
                    "filepath": "test2.xlsx",
                    "filename": "test2.xlsx",
                    "extension": "xlsx",
                    "filesize": None,
                },
                "1be3ad6175e27573e78b7ed0d6d718c8": {
                    "filepath": "test3.txt",
                    "filename": "test3.txt",
                    "extension": "txt",
                    "filesize": None,
                },
                "cf42381d1374c46d8fc2e6f72261ca21": {
                    "filepath": "test4.pptx",
                    "filename": "test4.pptx",
                    "extension": "pptx",
                    "filesize": None,
                },
                "71b0d45497f5282b23a2977e31554822": {
                    "filepath": "test5.PDF",
                    "filename": "test5.PDF",
                    "extension": "pdf",
                    "filesize": None,
                },
                "91286cda3229d4504bb5366b3ff54057": {
                    "filepath": "test6.json",
                    "filename": "test6.json",
                    "extension": "json",
                    "filesize": None,
                },
                "b04083e53e242626595e2b8ea327e525": {
                    "filepath": "test7",
                    "filename": "test7",
                    "extension": "",
                    "filesize": None,
                },
            },
        ),
        (
            ["test.csv", "hoi.json", "sdc.csv", "svvw.txt", "ascvwev.txt"],
            {
                "531f844bd184e913b050d49856e8d438": {
                    "filepath": "test.csv",
                    "filename": "test.csv",
                    "extension": "csv",
                    "filesize": None,
                },
                "52e2483e022917396fb563f0eae618cf": {
                    "filepath": "hoi.json",
                    "filename": "hoi.json",
                    "extension": "json",
                    "filesize": None,
                },
                "dc47b9b3dd0ccb57ad6b376bf5d055c2": {
                    "filepath": "sdc.csv",
                    "filename": "sdc.csv",
                    "extension": "csv",
                    "filesize": None,
                },
                "adc648a9a7f0394af47cf91429d1f934": {
                    "filepath": "svvw.txt",
                    "filename": "svvw.txt",
                    "extension": "txt",
                    "filesize": None,
                },
                "affdbd8c36920eaa3b05c7785f598fcb": {
                    "filepath": "ascvwev.txt",
                    "filename": "ascvwev.txt",
                    "extension": "txt",
                    "filesize": None,
                },
            },
        ),
        (
            [
                "[CC] Cmotions - Documents/.849C9593-D756-4E56-8D6E-42412F2A707B",
                "[CC] Cmotions - Documents/Data use cases.pptx",
                "[CC] Cmotions - Documents/Handleiding intranet Cmotions - nieuwste.docx",
                "[CC] Cmotions - Documents/Middelenoverzicht Cmotions-intern 2022.xlsx",
                "[CC] Cmotions - Documents/Acquisitie/NOC/NOC Data & Analytics Beheerder.docx",
                "[CC] Cmotions - Documents/Administratie/Cloud9.zip",
            ],
            {
                "98c7f2ce0e37e803a9fc13b760c96dd6": {
                    "filepath": "[CC] Cmotions - Documents/.849C9593-D756-4E56-8D6E-42412F2A707B",
                    "filename": ".849C9593-D756-4E56-8D6E-42412F2A707B",
                    "extension": "849c9593-d756-4e56-8d6e-42412f2a707b",
                    "filesize": None,
                },
                "5d488bb8f78cf77aa0a6eaf5c38a2401": {
                    "filepath": "[CC] Cmotions - Documents/Data use cases.pptx",
                    "filename": "Data use cases.pptx",
                    "extension": "pptx",
                    "filesize": None,
                },
                "5fbfdcc9f7e07976c44766c45abcee60": {
                    "filepath": "[CC] Cmotions - Documents/Handleiding intranet Cmotions - nieuwste.docx",
                    "filename": "Handleiding intranet Cmotions - nieuwste.docx",
                    "extension": "docx",
                    "filesize": None,
                },
                "f051c010189a7c523fffcd5c6adf6eed": {
                    "filepath": "[CC] Cmotions - Documents/Middelenoverzicht Cmotions-intern 2022.xlsx",
                    "filename": "Middelenoverzicht Cmotions-intern 2022.xlsx",
                    "extension": "xlsx",
                    "filesize": None,
                },
                "2871b90c4cb5e7f20e9bba52a820813b": {
                    "filepath": "[CC] Cmotions - Documents/Acquisitie/NOC/NOC Data & Analytics Beheerder.docx",
                    "filename": "NOC Data & Analytics Beheerder.docx",
                    "extension": "docx",
                    "filesize": None,
                },
                "786a63cd3bb2ea2b9ae83a57f8a84026": {
                    "filepath": "[CC] Cmotions - Documents/Administratie/Cloud9.zip",
                    "filename": "Cloud9.zip",
                    "extension": "zip",
                    "filesize": None,
                },
            },
        ),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_create_file_dict_normal_argument(self, input, expected):
        result = file_index._create_file_dict(list_files=input)
        assert (
            result == expected
        ), f"the expected output was {expected}, but the output is {result}"
