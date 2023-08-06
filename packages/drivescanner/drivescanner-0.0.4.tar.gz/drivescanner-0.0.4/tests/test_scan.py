"""This module tests the methods of the rules module in rules.py."""

import pytest
from drivescanner import scan


class TestScanFile:
    """
    all tests for _scan_file module in scan.py
        bad argument:
            input tuple is not a tuple
        special argument:
            none
        normal argument:
            a input tuple is a tuple
    """

    def test_scan_file_tuple_no_tuple_int(self):
        with pytest.raises(AssertionError, match=f"Input should be a tuple"):
            scan._scan_file(file_tuple="this string is not a tuple")

    def test_scan_file_tuple_no_tuple_str(self):
        with pytest.raises(AssertionError, match=f"Input should be a tuple"):
            scan._scan_file(file_tuple=123)

    def test_scan_file_none_input(self):
        with pytest.raises(AssertionError, match=f"Input should be a tuple"):
            scan._scan_file(file_tuple=None)

    test = [
        (
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
            False,
            {
                "39fb72233f11607b325791982114fb74": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/circuits.csv",
                    "filename": "circuits.csv",
                    "extension": "csv",
                    "filesize": 8667,
                    "content_processed": True,
                    "bsn": [],
                    "iban": [],
                    "email": [],
                    "telnr": [
                        ("0644157226", "Europe/Amsterdam"),
                        ("0613752832", "Europe/Amsterdam"),
                        ("0657916735", "Europe/Amsterdam"),
                        ("0617135855", "Europe/Amsterdam"),
                        ("0621143269", "Europe/Amsterdam"),
                        ("0610045854", "Europe/Amsterdam"),
                        ("0613251462", "Europe/Amsterdam"),
                        ("0663274547", "Europe/Amsterdam"),
                    ],
                    "zip": [],
                    "address": [],
                    "cv": False,
                    "credentials": False,
                    "creditcard": [],
                    "passport": [],
                },
                "e36faa69cb748215e2ec00fed27badca": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xls",
                    "filename": "Excel test Excel.xls",
                    "extension": "xls",
                    "filesize": 26112,
                    "content_processed": False,
                    "processing_error": "File of type xls is not supported",
                },
                "8ef834c3461a7665ab8f6da2f8158c1a": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/Excel test Excel.xlsx",
                    "filename": "Excel test Excel.xlsx",
                    "extension": "xlsx",
                    "filesize": 9217,
                    "content_processed": True,
                    "bsn": [],
                    "iban": [],
                    "email": [],
                    "telnr": [],
                    "zip": [],
                    "address": [],
                    "cv": False,
                    "credentials": False,
                    "creditcard": [],
                    "passport": [],
                },
                "e4896cf93bfd7f9f170a526e530f8c9e": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/HTM test.htm",
                    "filename": "HTM test.htm",
                    "extension": "htm",
                    "filesize": 233,
                    "content_processed": True,
                    "bsn": [],
                    "iban": [],
                    "email": [],
                    "telnr": [],
                    "zip": [],
                    "address": [],
                    "cv": False,
                    "credentials": False,
                    "creditcard": [],
                    "passport": [],
                },
                "0209a7022087172f346ec133f28a1926": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/Lipsum_2.txt",
                    "filename": "Lipsum_2.txt",
                    "extension": "txt",
                    "filesize": 116,
                    "content_processed": True,
                    "bsn": [],
                    "iban": [],
                    "email": [],
                    "telnr": [],
                    "zip": [],
                    "address": [],
                    "cv": False,
                    "credentials": False,
                    "creditcard": [],
                    "passport": [],
                },
                "778eba7ddc5ee844fcfae877843839d2": {
                    "filepath": "tests/testfiles/mysubfolderforfileindex/myfirstsubfolder/mysecondsubfolder/Lipsum_3.txt",
                    "filename": "Lipsum_3.txt",
                    "extension": "txt",
                    "filesize": 116,
                    "content_processed": True,
                    "bsn": [],
                    "iban": [],
                    "email": [],
                    "telnr": [],
                    "zip": [],
                    "address": [],
                    "cv": False,
                    "credentials": False,
                    "creditcard": [],
                    "passport": [],
                },
            },
        )
    ]

    @pytest.mark.parametrize("input, NER, expected", test)
    def test_scan_drive_normal_input(self, input, NER, expected):
        assert scan.scan_drive(input, NER) == expected
