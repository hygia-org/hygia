import re
import pandas as pd
class Regex:
    def contains_exactly_the_word_dell(self, text:str) -> bool:
        pattern = r'\bdell\b'
        return bool(re.search(pattern, text, re.IGNORECASE))
    
    def contains_exactly_the_word_test(self, text:str) -> bool:
        pattern = r'\btest\b'
        return bool(re.search(pattern, text, re.IGNORECASE))
    
    def only_numbers(self, text:str) -> bool:
        pattern = r'^[0-9]+$'
        return bool(re.search(pattern, text, re.IGNORECASE))
    
    def only_special_characters(self, text:str) -> bool:
        pattern = r'^[^a-zA-Z0-9]+$'
        return bool(re.search(pattern, text, re.IGNORECASE))
    
    def contains_email(self, text:str) -> bool:
        pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
        return bool(re.search(pattern, text, re.IGNORECASE))
    
    def contains_url(self, text:str) -> bool:
        pattern = r'\b(https?:\/\/|www\.)[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
        return bool(re.search(pattern, text, re.IGNORECASE))
    
    def contains_date(self, text:str) -> bool:
        pattern = r'^(?P<day>\d{1,2})(?:-|\.|/)(?P<month>\d{1,2})(?:-|\.|/)(?P<year>\d{4})$'
        return bool(re.search(pattern, text, re.IGNORECASE))
    
    def contains_invalid_words(self, text:str) -> bool:
        pattern = r'\b(null|undefined|dummy)\b'
        return bool(re.search(pattern, text, re.IGNORECASE))
    
    def is_substring_of_column_name(self, text:str, column_name:str) -> bool:
        return text.lower() in column_name.lower()
    
    def only_one_char(self, text:str) -> bool:
        return len(text.strip()) == 1

    def only_one_word(self, text:str) -> bool:
        return len(text.strip().split()) == 1
    
    def only_white_spaces(self, text:str) -> bool:
        return text != '' and not text.strip()
    
    def empty(self, text:str) -> bool:
        return text == ''
    
    def extract_regex_features(self, df:pd.DataFrame, column_name:str) -> pd.DataFrame:
        regex_features = [
            self.contains_exactly_the_word_dell,
            self.contains_exactly_the_word_test,
            self.only_numbers,
            self.only_special_characters,
            self.contains_email,
            self.contains_url,
            self.contains_date,
            self.contains_invalid_words,
            self.is_substring_of_column_name,
            self.only_one_char,
            self.only_white_spaces,
            self.empty
        ]
        for regex_feature in regex_features:
            df[f'feature_re_{regex_feature.__name__}_{column_name}'] = df[column_name].apply(lambda x: regex_feature(x) if regex_feature.__code__.co_argcount == 2 else regex_feature(x, column_name))
        return df
    