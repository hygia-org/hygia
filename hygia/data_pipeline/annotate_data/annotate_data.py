import pandas as pd
from colorama import Fore, Style

class AnnotateData:
    """
    A class to incorporate the data annotation phase, starting from the thresholds 
    (e.g., count sequence squared vowels, count sequence squared consonants) can tell if it's a ksmash.

    Examples
    --------
    Use this class like this:

    .. code-block:: python

        annotate_data = hg.AnnotateData()
        key_smash_thresholds = {
        'count_sequence_squared_vowels': 1.00,
        'count_sequence_squared_consonants': 1.999,
        'count_sequence_squared_special_characters': 2.2499,
        'ratio_of_numeric_digits_squared': 2.9,
        'average_of_char_count_squared': 2.78,
        }

        df = annotate_data.annotate_data(df, concatened_column_name, key_smash_thresholds)
        print(df)
    """
    def annotate_data(self, df, concatened_column_name, ks_thresholds):
        """
        Annotate data function.
        
        :param df: Dataframe to extract features from.
        :type df: pandas.DataFrame
        :param concatened_column_name: Dataframe column to be used
        :type concatened_column_name: List
        :param ks_thresholds: List of thresholds
        :type ks_thresholds: List

        :return: The input dataframe with additional columns for key smashing and word embedding features.
        :rtype: pandas.DataFrame
        """

        print(f'{Fore.YELLOW}running annotate data with configs below...{Fore.WHITE}')
        
        print(f'{Style.BRIGHT}thresholds -> {Style.NORMAL}{ks_thresholds}')
        print(f'column -> {concatened_column_name}')
        
        df['target'] = 'valid'
        
        ks_colummns = [col for col in df if col.startswith('feature_ks')]
        for ks_colummn in ks_colummns:
            threshold = float("inf")
            for th in ks_thresholds:
                if th in ks_colummn:
                    threshold = ks_thresholds[th]
            df['target'] = df.apply(lambda x: 'key_smash' if x[ks_colummn] >= threshold else x['target'], axis=1) 
        
        re_colummns = [col for col in df if col.startswith('feature_re')]
        for re_colummn in re_colummns:
            target_name = re_colummn.replace('feature_re_', '').replace(f'_{concatened_column_name}', '')
            df['target'] = df.apply(lambda x: target_name if x[re_colummn] else x['target'], axis=1) 
        
        return df

