"""This module tests the methods of the rules module in rules.py."""

import pytest
from drivescanner import rules

class TestRemoveEntities:
    """
    all tests for _remove_entities module in rules.py
        bad argument:
            input 'txt' is not a str
            input 'found_list' is a list, but not of strings
        special argument:
            none
        normal argument:
            a txt file as string
            a list of files as strings
    """

    def test_remove_entities_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._remove_entities(txt=123, entity_list=['test'])

    def test_remove_entities_list_no_str(self):
        with pytest.raises(AssertionError, match=f"found_list should be a list of strings"):
            rules._remove_entities(txt='test', entity_list=[12, 14])

    def test_remove_entities_none_input(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._remove_entities(txt=None, entity_list=['test'])

    test = [
                ("hallo test", ["hallo"], " test"),
                ("hallo test", ["test"], "hallo "),
                ("hallo test", ["hallo test"], ""),
                ("hallo test", [], "hallo test"),
                ("", [], "")
    ]

    @pytest.mark.parametrize("input1, input2, expected", test)
    def test_remove_entities_normal_input(self, input1, input2, expected):
        assert rules._remove_entities(input1, input2) == expected

class TestExtractSsn:
    """
    all tests for _extract_ssn module in rules.py
        bad argument:
            input 'txt' is not a str
        special argument:
            none
        normal argument:
            input 'txt' is a str
    """

    def test_extract_ssn_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_ssn(txt=123)

    def test_extract_ssn_txt_none(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_ssn(txt=None)

    test = [
        ("000000000 123456782 ", ["123456782"]),
        ("hallo dit is een test", []),
        ("000000000 123456782 0623359335", ["123456782"]),
        ("", [])
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_extract_ssn_normal_input(self, input, expected):
        assert rules._extract_ssn(input) == expected

class TestValidIban:
    """
    all tests for _valid_iban module in rules.py
        bad argument:
            input 'iban' is not a str
        special argument:
            none
        normal argument:
            input 'iban' is a str
    """

    def test_valid_iban_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"iban should be a str"):
            rules._valid_iban(iban=123)

    def test_valid_iban_txt_none(self):
        with pytest.raises(AssertionError, match=f"iban should be a str"):
            rules._valid_iban(iban=None)

    test = [
        ("NL98TEBU0869698303", True),
        ("NL98TEBU0869698", False),
        ("NL73RABO0@3!", False),
        ("NL12RABO0114573622 NL98TEBU0869698303 233", False),
        ("", False)
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_valid_iban_normal_input(self, input, expected):
        assert rules._valid_iban(input) == expected

class TestExtractIban:
    """
    all tests for _extract_iban module in rules.py
        bad argument:
            input 'txt' is not a str
        special argument:
            none
        normal argument:
            input 'txt' is a str
    """

    def test_extract_iban_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_iban(txt=123)

    def test_extract_iban_txt_none(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_iban(txt=None)

    test = [
        ("NL98TEBU0869698303", ["NL98TEBU0869698303"]),
        ("NL98TEBU086969", []),
        ("NL12RABO0114573622 NL98TEBU0869698303 233", ["NL98TEBU0869698303"]),
        ("", [])
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_extract_iban_normal_input(self, input, expected):
        assert rules._extract_iban(input) == expected

class TestExtractEmail:
    """
    all tests for _extract_email module in rules.py
        bad argument:
            input 'txt' is not a str
        special argument:
            none
        normal argument:
            input 'txt' is a str
    """

    def test_extract_email_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_email(txt=123)

    def test_extract_email_txt_none(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_email(txt=None)

    test = [
        ("d.voorman@cmotions.nl w1#$@hotmail.com", ["d.voorman@cmotions.nl"]),
        ("d.voorman@cmotions.nl w1-d@hotmail.com", ["d.voorman@cmotions.nl", "w1-d@hotmail.com"]),
        ("hallo test", []),
        ("", [])
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_extract_email_normal_input(self, input, expected):
        assert rules._extract_email(input) == expected

class TestExtractPhoneNumber:
    """
    all tests for _extract_phonenumbers module in rules.py
        bad argument:
            input 'txt' is not a str
            input phonenumber with non existing country code
        special argument:
            none
        normal argument:
            input 'txt' is a str
    """

    def test_extract_phonenumbers_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_phonenumbers(txt=123)

    def test_extract_phonenumbers_txt_none(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_phonenumbers(txt=None)


    test = [
        ("+316 399 023 43 (+31)(0)610223710 32498232",
         [('+31639902343', 'Europe/Amsterdam'),
          ('+310610223710', 'Europe/Amsterdam')]),
        ("+06 399 023 43",
         [('0639902343', 'Europe/Amsterdam')]),
        ("d.voorman@cmotions.nl w1-d@hotmail.com", []),
        ("", []),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_extract_phonenumbers_normal_input(self, input, expected):
        assert rules._extract_phonenumbers(input) == expected

class TestExtractZip:
    """
    all tests for _extract_zip module in rules.py
        bad argument:
            input 'txt' is not a str
        special argument:
            none
        normal argument:
            input 'txt' is a str
    """

    def test_extract_zip_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_zip(txt=123)

    def test_extract_zip_txt_none(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_zip(txt=None)

    test = [
        ("d.voorman@cmotions.nl 1327AB", ["1327AB"]),
        ("1327AB is voor 7326KA", ["1327AB", "7326KA"]),
        ("hallo test", []),
        ("", [])
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_extract_zip_normal_input(self, input, expected):
        assert rules._extract_zip(input) == expected

class TestCheckCV:
    """
    all tests for _check_cv module in rules.py
        bad argument:
            input 'txt' is not a str
        special argument:
            none
        normal argument:
            input 'txt' is a str
    """

    def test_check_cv_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._check_cv(txt=123)

    def test_check_cv_txt_none(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._check_cv(txt=None)

    test = [
        ("d.voorman@cmotions.nl 1327AB", False),
        ("1327AB test CV", True),
        ("Dit is de Resume", True),
        ("", False)
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_check_cv_normal_input(self, input, expected):
        assert rules._check_cv(input) == expected

class TestCheckCredentials:
    """
    all tests for _check_credentials module in rules.py
        bad argument:
            input 'txt' is not a str
        special argument:
            none
        normal argument:
            input 'txt' is a str
    """

    def test_check_credentials_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._check_credentials(txt=123)

    def test_check_credentials_txt_none(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._check_credentials(txt=None)

    test = [
        ("d.voorman@cmotions.nl 1327AB", False),
        ("1327AB test ww:Welkom01", True),
        ("De username is test123", True),
        ("", False)
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_check_credentials_normal_input(self, input, expected):
        assert rules._check_credentials(input) == expected

class TestValidCreditCardNumber:
    """
    all tests for _valid_cc_number module in rules.py
        bad argument:
            input 'card_number' is not a str
        special argument:
            none
        normal argument:
            input 'card_number' is a str
    """

    def test_valid_cc_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"card_number should be a str"):
            rules._valid_cc_number(card_number=123)

    def test_valid_cc_txt_none(self):
        with pytest.raises(AssertionError, match=f"card_number should be a str"):
            rules._valid_cc_number(card_number=None)

    test = [
        ("1234-1234-1832-1234", True),
        ("9000 0000 0000 0009", False),
        ("", False),
        ("NL12RABO0114573622 NL98TEBU0869698303 233", False)
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_valid_cc_normal_input(self, input, expected):
        assert rules._valid_cc_number(input) == expected

class TestExtractCreditCardNumber:
    """
    all tests for _extract_cc_number module in rules.py
        bad argument:
            input 'txt' is not a str
        special argument:
            none
        normal argument:
            input 'txt' is a str
    """

    def test_extract_cc_number_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_cc_number(txt=123)

    def test_extract_cc_number_txt_none(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_cc_number(txt=None)

    test = [
        ("You can bill my creditcard for this round, it's 1234-1234-1832-1234, or use 5674 1234 1832 5647.", ['1234-1234-1832-1234', '5674 1234 1832 5647']),
        ("My fake card number is 0867-4322-6712-1121", []),
        ("My card number is 1234-1234-1832-1234", ["1234-1234-1832-1234"]),
        ("No CC-number in this string", []),
        ("", [])
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_extract_cc_number_normal_input(self, input, expected):
        assert rules._extract_cc_number(input) == expected

class TestExtractPassportNumber:
    """
    all tests for _extract_passport module in rules.py
        bad argument:
            input 'txt' is not a str
        special argument:
            none
        normal argument:
            input 'txt' is a str
    """

    def test_extract_passport_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_passport(txt=123)

    def test_extract_passport_txt_none(self):
        with pytest.raises(AssertionError, match=f"txt should be a str"):
            rules._extract_passport(txt=None)

    test = [
        ("The number in my passport is WS00T63D0.", ['WS00T63D0']),
        ("My passport number is WS00T63D0, my sisters number is RT66Y11D9 and my bank account number is NL12RABO0114573622.", ["WS00T63D0", "RT66Y11D9"]),
        ("No passport number in this string", []),
        ("", [])
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_extract_passport_normal_input(self, input, expected):
        assert rules._extract_passport(input) == expected

class TestExtractNER:
    """
    all tests for extract_NER module in rules.py
        bad argument:
            Input should be a string
        special argument:
            none
        normal argument:
            Input should be a string
    """

    def test_extract_NER_txt_no_str(self):
        with pytest.raises(AssertionError, match=f"Input should be a string"):
            rules.extract_NER(input=123)

    def test_extract_NER_txt_none(self):
        with pytest.raises(AssertionError, match=f"Input should be a string"):
            rules.extract_NER(input=None)

    test_default = [
        ("Mijn naam is Kees Groenewoud", [['Kees Groenewoud', 'PERSON']]),
        # ("Het huis van Julia brandde op 5 october volledig af.", [['Julia', 'PERSON']]),
        ("Er zit geen entity in deze string", []),
        ("", [])
    ]

    test_multiple_entities = [
        ("Mijn naam is Kees Groenewoud", [['Kees Groenewoud', 'PERSON']]),
        # ("Het huis van Julia brandde op 5 october volledig af.", [['Julia', 'PERSON'], ['5 october', 'DATE']]),
        ("Er zit geen entity in deze string", []),
        ("", [])
    ]

    @pytest.mark.parametrize("input, expected", test_default)
    def test_extract_NER_normal_input(self, input, expected):
        assert rules.extract_NER(input) == expected

    @pytest.mark.parametrize("input, expected", test_multiple_entities)
    def test_extract_NER_normal_input_multiple(self, input, expected):
        assert rules.extract_NER(input, ['PERSON', 'DATE']) == expected