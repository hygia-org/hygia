import pytest
import pandas as pd
from hygia.data_pipeline.feature_engineering.regex import Regex

class TestRegex:
    def setup_method(self):
        self.regex = Regex()
    
    def test_contains_exactly_the_word_dell(self):
        assert self.regex.contains_exactly_the_word_dell("A DELL LAPTOP") == True
        assert self.regex.contains_exactly_the_word_dell("a dell laptop") == True
        assert self.regex.contains_exactly_the_word_dell("MEDELLIN ST") == False
        
    def test_contains_exactly_the_word_test(self):
        assert self.regex.contains_exactly_the_word_test("THIS IS A TEST") == True
        assert self.regex.contains_exactly_the_word_test("This is a Test") == True
        assert self.regex.contains_exactly_the_word_test("TESTERMAN") == False
        
    def test_only_numbers(self):
        assert self.regex.only_numbers("12345") == True
        assert self.regex.only_numbers("12345ABC") == False
        assert self.regex.only_numbers("") == False
        
    def test_only_special_characters(self):
        assert self.regex.only_special_characters("!@#$%^&*") == True
        assert self.regex.only_special_characters("!@#$%^&*ABC") == False
        assert self.regex.only_special_characters("") == False
        
    def test_contains_email(self):
        assert self.regex.contains_email("EXAMPLE@GMAIL.COM") == True
        assert self.regex.contains_email("EXAMPLE") == False
        assert self.regex.contains_email("") == False
        
    def test_contains_url(self):
        assert self.regex.contains_url("HTTPS://WWW.EXAMPLE.COM") == True
        assert self.regex.contains_url("WWW.EXAMPLE.COM") == True
        assert self.regex.contains_url("") == False
        
    def test_contains_date(self):
        assert self.regex.contains_date("01/01/2021") == True
        assert self.regex.contains_date("01-01-2021") == True
        assert self.regex.contains_date("01.01.2021") == True
        assert self.regex.contains_date("2021/01/01") == False
        assert self.regex.contains_date("") == False
        
    def test_contains_invalid_words(self):
        assert self.regex.contains_invalid_words("NULL") == True
        assert self.regex.contains_invalid_words("A NULL") == True
        assert self.regex.contains_invalid_words("UNDEFINED") == True
        assert self.regex.contains_invalid_words("A UNDEFINED") == True
        assert self.regex.contains_invalid_words("DUMMY") == True
        assert self.regex.contains_invalid_words("A DUMMY") == True
        assert self.regex.contains_invalid_words("EXAMPLE") == False
        assert self.regex.contains_invalid_words("A EXAMPLE") == False
        assert self.regex.contains_invalid_words("") == False
    
    def test_is_substring_of_column_name(self):
        assert self.regex.is_substring_of_column_name("STREET_ADDRESS_1", "concat_STREET_ADDRESS_1_STREET_ADDRESS_2") == True
        assert self.regex.is_substring_of_column_name("STREET", "concat_STREET_ADDRESS_1_STREET_ADDRESS_2") == True
        assert self.regex.is_substring_of_column_name("123 STREET", "concat_STREET_ADDRESS_1_STREET_ADDRESS_2") == False
    
    def test_only_one_char(self):
        assert self.regex.only_one_char("a") == True
        assert self.regex.only_one_char(" ") == False
        assert self.regex.only_one_char("  ") == False
        assert self.regex.only_one_char(" a ") == True
        assert self.regex.only_one_char("") == False
        
    def test_only_one_word(self):
        assert self.regex.only_one_word("a") == True
        assert self.regex.only_one_word("word") == True
        assert self.regex.only_one_word("word ") == True
        assert self.regex.only_one_word(" word") == True
        assert self.regex.only_one_word("  word  ") == True
        assert self.regex.only_one_word("") == False
    
    def test_only_white_spaces(self):
        assert self.regex.only_white_spaces("\t\t") == True
        assert self.regex.only_white_spaces("\t") == True
        assert self.regex.only_white_spaces(" ") == True
        assert self.regex.only_white_spaces("    ") == True
        assert self.regex.only_white_spaces("") == False
        assert self.regex.only_white_spaces("EXAMPLE") == False
        assert self.regex.only_white_spaces("EXAMPLE 1") == False
        
    def test_empty(self):
        assert self.regex.empty("") == True
        assert self.regex.empty("EXAMPLE") == False
    