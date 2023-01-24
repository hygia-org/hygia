from statistics import mean
import pandas as pd
import re

class KeySmash:
    """
    A class for calculating metrics to indicate key smashing behavior in a text.

    Key smashing is the act of typing on a keyboard in a rapid and uncontrolled manner,
    often resulting in a series of random characters being entered into a document or text field.

    Examples
    --------
    Use this class like this:

    .. code-block:: python

        key_smash = KeySmash()
        df = key_smash.extract_key_smash_features(df, "text_column")
        print(df)
    """
    
    def __init__(self):
        self.char_sets = {
            "vowels": 'aeiouáéíóúãõ',
            "consonants": 'bcdfghjklmnñpqrstvwxyz',
            "special_characters": '!@#$%^¨|\'\"&*()_+:;~`´]}{[}ºª=-.¿¡'
        }
    
    def average_of_char_count_squared(self, text:str) -> float:
        """
        The function takes a string text as input and splits it into words.
        For each word, it counts the number of occurrences of each character in the word, squares those counts, and then sums them.
        It then divides the sum by the length of the word and appends the result to a list words_results.
        Finally, it returns the mean of the words_results list, if the list is not empty, otherwise it returns 0.

        :param text: The text to use for the calculation.
        :type text: str
        :return: The calculated Char Frequency Metric.
        :rtype: float

        Examples
        --------
        Use this function like this:

        .. code-block:: python
        
            key_smash = KeySmash()

            res = key_smash.average_of_char_count_squared("PUENTECILLA KM. 1.7")
            print(res)
            # Output: 1.121212121212121

            res = key_smash.average_of_char_count_squared("ASDASD XXXX")
            print(res)
            # Output: 3.0
        """
        text = text.lower()
        text = re.sub(r'\s', ' ', text)
        words_results = []
        words = text.split(' ')
        for word in words:
            if word and len(word) > 0:
                char_count = 0
                for char in set(word):
                    char_count += word.count(char) ** 2
                words_results.append(char_count / len(word))
        if words_results:
            return sum(words_results) / len(words_results)
        else:
            return 0
    
    def count_sequence_squared(self, text:str, opt:str) -> float:
        """
        This function takes a text and opt as input. It checks a set of characters, converts text to lowercase, iterates through characters,
        increments counter if finds a sequence of characters in set, if not it adds square of counter to a list, resets counter to 1.
        After iterating it returns sum of list divided by length of text.
        
        :param text: The text to use for the calculation.
        :type text: str
        :param opt: The type of characters to consider for the calculation, can be one of 'vowels', 'consonants', or 'special_characters'.
        :type opt: str
        :return: The calculated Irregular Sequence Metric.
        :rtype: float

        Examples
        --------
        Use this function like this:

        .. code-block:: python
        
            key_smash = KeySmash()

            res = key_smash.count_sequence_squared("PUENTECILLA KM. 1.7", "vowels")
            print(res)
            # Output: 0.21052631578947367

            res = key_smash.count_sequence_squared("ASDASD XXXX", "consonants")
            print(res)
            # Output: 2.1818181818181817

            res = key_smash.count_sequence_squared("!@#$% ASDFGHJKL", "special_characters")
            print(res)
            # Output: 1.5625
        """
        text = text.lower()
        count_sequence = 1
        sequences = []
        char_set = self.char_sets[opt]

        for i in range(len(text) - 1):
            if text[i] in char_set and text[i + 1] in char_set:
                count_sequence += 1
            else:
                if count_sequence > 1:
                    sequences.append(count_sequence ** 2)
                    count_sequence = 1

        if count_sequence > 1:
            sequences.append(count_sequence ** 2)

        return sum(sequences) / len(text)
    
    def ratio_of_numeric_digits_squared(self, text:str) -> float:
        """
        This function takes text as input, splits it into a list of words, initializes a variable to 0.
        It iterates through list of words, checking if each word contains both numeric digits and non-numeric characters.
        If yes, it counts number of numeric digits, squares it and adds to variable.
        It returns the value of that variable divided by length of original text, if the list is empty it returns 0.

        :param text: The text to extract the metric from.
        :type text: str
        :return: The calculated Number Count Metric.
        :rtype: float

        Examples
        --------
        Use this function like this:

        .. code-block:: python

            key_smash = KeySmash()
            
            res = key_smash.ratio_of_numeric_digits_squared("ABC 123 !@#")
            print(res)
            # Output: 0.0

            res = key_smash.ratio_of_numeric_digits_squared("ABC123 !@#")
            print(res)
            # Output: 0.9
        """
        text = text.lower()
        text_list = text.split()
        num_of_numeric_digits = 0

        for word in text_list:
            if any(c.isdigit() for c in word) and any(not c.isdigit() for c in word):
                num_of_numeric_digits += len([c for c in word if c.isdigit()]) ** 2

        if text_list:
            return num_of_numeric_digits / len(' '.join(text_list))
        else:
            return 0
    
    def _normalize_column(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        """
        Normalize a given column in a dataframe.
        
        :param df: Dataframe to normalize the column in.
        :type df: pandas.DataFrame
        :param column: Name of the column to be normalized.
        :type column: str

        :return: The input dataframe with the normalized column.
        :rtype: pandas.DataFrame
        """
        return df[column]  / df[column].abs().max() if df[column].abs().max() != 0.0 else 0.0

    
    def extract_key_smash_features(self, df:pd.DataFrame, column_name:str, normalize:bool=False) -> pd.DataFrame:
        """
        Extract key smash features from a given dataframe and column.

        :param df: Dataframe to extract key smash features from.
        :type df: pandas.DataFrame
        :param column_name: Name of the column in the dataframe that contains the text data to extract features from.
        :type column_name: str
        :param normalize: Indicates whether to normalize the key smash feature columns. Default is True.
        :type normalize: bool, optional

        :return: The input dataframe with additional columns for key smash features: 'irregular_sequence_vowels', 'irregular_sequence_consonants', 'irregular_sequence_special_characters', 'number_count_metric', 'char_frequency_metric'
        :rtype: pandas.DataFrame

        Examples
        --------
        Use this function like this:

        .. code-block:: python

            import pandas as pd
            key_smash = KeySmash()
            df = pd.DataFrame({"text_column": ["abcdefgh", "ijklmnop", "qrstuvwxyz"]})
            df = key_smash.extract_key_smash_features(df, "text_column", normalize=False)
            print(df.head())
        """
        df[f'feature_ks_count_sequence_squared_vowels_{column_name}'] = df[column_name].fillna('').apply(lambda x: self.count_sequence_squared(x, 'vowels') if len(x) > 0 else 0.0)
        df[f'feature_ks_count_sequence_squared_consonants_{column_name}'] = df[column_name].fillna('').apply(lambda x: self.count_sequence_squared(x, 'consonants') if len(x) > 0 else 0.0)
        df[f'feature_ks_count_sequence_squared_special_characters_{column_name}'] = df[column_name].fillna('').apply(lambda x: self.count_sequence_squared(x, 'special_characters') if len(x) > 0 else 0.0)
        df[f'feature_ks_ratio_of_numeric_digits_squared_{column_name}'] = df[column_name].fillna('').apply(lambda x: self.ratio_of_numeric_digits_squared(x) if len(x) > 0 else 0.0)
        df[f'feature_ks_average_of_char_count_squared_{column_name}'] = df[column_name].fillna('').apply(lambda x: self.average_of_char_count_squared(x) if len(x) > 0 else 0.0)
        
        if normalize:
            key_smash_columns = [f'feature_ks_count_sequence_squared_vowels_{column_name}',
                                f'feature_ks_count_sequence_squared_consonants_{column_name}',
                                f'feature_ks_count_sequence_squared_special_characters_{column_name}',
                                f'feature_ks_ratio_of_numeric_digits_squared_{column_name}',
                                f'feature_ks_average_of_char_count_squared_{column_name}']
            for column in key_smash_columns:
                df[column] = self._normalize_column(df, column)
        
        return df