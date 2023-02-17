import pandas as pd
from colorama import Fore, Style

class AnnotateData:
    """A class to incorporate the data annotation phase, starting from the thresholds 
    (e.g., count sequence squared vowels, count sequence squared consonants) can tell if it's a ksmash.

    Examples
    
    Use this class like this:

    \code{.py}

        annotate_data = hg.AnnotateData()
        key_smash_thresholds = {
        'count_sequence_squared_vowels': ['above', 1.00],
        'count_sequence_squared_consonants': ['above', 1.999],
        'count_sequence_squared_special_characters': ['above', 2.2499],
        # 'ratio_of_numeric_digits_squared': ['above', 2.9],
        'average_of_char_count_squared': ['above', 2.78],
        'shannon_entropy' : ['below', 2.0]
        }

        df = annotate_data.annotate_data(df, concatened_column_name, key_smash_thresholds)
        print(df)
    \endcode
    """
    def annotate_data(self, df, concatened_column_name, ks_thresholds):
        """
        Annotate data function.
        
        \param df (Type: DataFrame) Dataframe to extract features from.
        \param concatened_column_name (Type: List) List of columns to be used
        \param ks_thresholds (Type: List) List of thresholds

        \return (Type: DataFrame) The input dataframe with additional columns for key smashing and word embedding features.
        """

        print(f'{Fore.YELLOW}running annotate data with configs below...{Fore.WHITE}')
        
        print(f'{Style.BRIGHT}thresholds -> {Style.NORMAL}{ks_thresholds}')
        print(f'column -> {concatened_column_name}')
        
        df['target'] = 'valid'
        
        ks_colummns = [col for col in df if col.startswith('feature_ks') and col.endswith(concatened_column_name)]
        for ks_colummn in ks_colummns:
            threshold = ks_thresholds[ks_colummn.replace('feature_ks_', '').replace(f'_{concatened_column_name}', '')]
            if threshold[0] == 'above':
                df['target'] = df.apply(lambda x: 'key_smash' if x[ks_colummn] >= threshold[1] else x['target'], axis=1) 
            elif threshold[0] == 'below':
                df['target'] = df.apply(lambda x: 'key_smash' if x[ks_colummn] <= threshold[1] else x['target'], axis=1)
        
        re_colummns = [col for col in df if col.startswith('feature_re')]
        for re_colummn in re_colummns:
            target_name = re_colummn.replace('feature_re_', '').replace(f'_{concatened_column_name}', '')
            df['target'] = df.apply(lambda x: target_name if x[re_colummn] else x['target'], axis=1) 
        
        return df

