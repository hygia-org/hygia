from statistics import mean

class KeySmash:
    """
    A class for calculating metrics to indicate key smashing behavior in a text.

    Key smashing is the act of typing on a keyboard in a rapid and uncontrolled manner,
    often resulting in a series of random characters being entered into a document or text field.

    Examples
    --------
    Use this class like this:

    .. code-block:: python

        keysmash = KeySmash()
        df = keysmash.extract_key_smash_features(df, "text_column")
        print(df)
    """
    
    
    def __init__(self):
        self.char_sets = {
            "vowels": 'aeiouáéíóúãõ',
            "consonants": 'bcdfghjklmnñpqrstvwxyz',
            "special_characters": '!@#$%^¨|\'\"&*()_+:;~`´]}{[}ºª=-.¿¡'
        }
    
    def calculate_char_frequency_metric(self, text:str) -> float:
        """
        Calculate the Char Frequency Metric.

        :param text: The text to use for the calculation.
        :type text: str
        :return: The calculated Char Frequency Metric.
        :rtype: float

        Examples
        --------
        Use this function like this:

        .. code-block:: python

            res = calculate_char_frequency_metric("PUENTECILLA KM. 1.7")
            print(res)
            # Output: 1.121212121212121

            res = calculate_char_frequency_metric("ASDASD XXXX")
            print(res)
            # Output: 3.0
        """
        word_results = []

        for w in text.split(' '):
            char_count = []
            if w and len(w) > 0:
                for e in set(w):
                    char_count.append(w.count(e)**2)
                word_results.append(sum(char_count)/len(w))

        if word_results == 0 or len(word_results) == 0:
            return 0
        else:
            return mean(word_results)
    
    def calculate_irregular_sequence_metric(self, text:str, opt:str) -> float:
        """
        Calculate the Irregular Sequence Metric.
        
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

            res = calculate_irregular_sequence_metric("PUENTECILLA KM. 1.7", "vowels")
            print(res)
            # Output: 0.21052631578947367

            res = calculate_irregular_sequence_metric("ASDASD XXXX", "consonants")
            print(res)
            # Output: 2.1818181818181817

            res = calculate_irregular_sequence_metric("!@#$% ASDFGHJKL", "special_characters")
            print(res)
            # Output: 1.5625
        """
        count_sequence = 1
        sequence_regex = []

        text = str(text).lower()
        opt = self.char_sets[opt]

        for i in range(len(text) - 1):
            if text[i] in opt and text[i + 1] in opt:
                count_sequence = count_sequence + 1
            else:
                if (count_sequence != 1):
                    sequence_regex.append(count_sequence**2)
                    count_sequence = 1

        if (count_sequence != 1):
            sequence_regex.append(count_sequence**2)
            
        return sum(sequence_regex)/len(text)
    
    def calculate_number_count_metric(self, text:str) -> float:
        """
        Calculate the Number Count Metric for a given text.

        :param text: The text to extract the metric from.
        :type text: str
        :return: The calculated Number Count Metric.
        :rtype: float

        Examples
        --------
        Use this function like this:

        .. code-block:: python

            res = calculate_number_count_metric("ABC 123 !@#")
            print(res)
            # Output: 0.0

            res = calculate_number_count_metric("ABC123 !@#")
            print(res)
            # Output: 0.9
        """
        text_list = text.split()
        calc_num_line = 0

        if text_list:
            for word in text_list:
                if any(char.isdigit() for char in word) and any(not char.isdigit() for char in word):
                    num = len([char for char in word if char.isdigit()])
                    calc_num = num**2
                    calc_num_line += calc_num

            return calc_num_line / len(' '.join(text_list))
        return 0
    
    def extract_key_smash_features(self, df:pd.DataFrame, column_name:str, normalize:bool=True) -> pd.DataFrame:
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
            keysmash = KeySmash()
            df = pd.DataFrame({"text_column": ["abcdefgh", "ijklmnop", "qrstuvwxyz"]})
            df = keysmash.extract_key_smash_features(df, "text_column", normalize=False)
            print(df.head())
        """
        df['irregular_sequence_vowels'] = df[column_name].fillna('').apply(lambda x: self.calculate_irregular_sequence_metric(x, 'vowels'))
        df['irregular_sequence_consonants'] = df[column_name].fillna('').apply(lambda x: self.calculate_irregular_sequence_metric(x, 'consonants'))
        df['irregular_sequence_special_characters'] = df[column_name].fillna('').apply(lambda x: self.calculate_irregular_sequence_metric(x, 'special_characters'))
        df['number_count_metric'] = df[column_name].fillna('').apply(lambda x: self.calculate_number_count_metric(x))
        df['char_frequency_metric'] = df[column_name].fillna('').apply(lambda x: self.calculate_char_frequency_metric(x))
        
        if normalize:
            key_smash_columns = ['irregular_sequence_vowels',
                            'irregular_sequence_consonants',
                            'irregular_sequence_special_characters',
                            'number_count_metric',
                            'char_frequency_metric']
            for column in key_smash_columns:
                df[column] = self.__normalize_column(df, column)
        
        return df