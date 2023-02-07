import pandas as pd
from hygia.paths.paths import root_path

class AugmentData:
    """
        This class present a validations based on zipocde data from this website:
        https://www.listendata.com/2020/11/zip-code-to-latitude-and-longitude.html?m=1
        we downloaded data from some continents and we filter based in the 'country' code
        we saved the data as pickle files in order to not overwhelm git history.
    """
    
    def __init__(self, country:str) -> None:
        """
        Initialize the AugmentData class.
        
        :param country: Zipcode list of the region or country used.
        :type country: str
        """
        continent_files = {
            'north_america': 'zip_to_lat_lon_North America.pkl',
            'south_america': 'zip_to_lat_lon_South America.pkl'
        }
        country_mappings = {
            # TODO implement only numbers validation in zipcode
            'BRAZIL': {'code': 'BR', 'zipcode_file': continent_files['south_america'], 'length':7, 'only_numbers':True},
            'US': {'code': 'US', 'zipcode_file': continent_files['north_america'], 'length':5, 'only_numbers':True},
            'MEXICO': {'code': 'MX', 'zipcode_file': continent_files['north_america'], 'length':5, 'only_numbers':True},
        }
        country_code = country_mappings[country]['code']
        zipcode_file = country_mappings[country]['zipcode_file']
        zipcode_df = pd.read_pickle(root_path + f"/data/zipcode/{zipcode_file}")
        country_zipcode_df_raw = zipcode_df[zipcode_df['country code']== country_code].copy()
        if country_mappings[country]['length']:
            country_zipcode_df_raw['postal code'] = country_zipcode_df_raw['postal code'].str.pad(country_mappings[country]['length'],fillchar='0')
        self.country_zipcode_df = country_zipcode_df_raw.drop_duplicates(subset=['postal code'])
    
    def validate_zipcode(self, text:str) -> bool:
        """
        Check if a zipcode is valid.
        
        :param text: Zipcode list of the region or country used.
        :type text: str

        :return: Return if the zipcode is valid
        :rtype: bool
        """
        return text in self.country_zipcode_df['postal code'].values
    
    def validate_zipcodes(self, df:pd.DataFrame, zipcode_column_name:str) -> pd.DataFrame:
        """
        Check if all zipcode in a data is valid.
        
        :param df: Dataframe to extract features from.
        :type df: pandas.DataFrame

        :param zipcode_column_name: Zipcode column name
        :type zipcode_column_name: str

        :return: Return a dataframe with a new column.
        :rtype: DataFrame
        """
        if zipcode_column_name not in df:
            return
        validated_column = f"{zipcode_column_name}_is_valid"
        indicator_column = f"{zipcode_column_name}_is_valid_indicator"
        df_aux = pd.merge(df, self.country_zipcode_df, how='left', left_on=zipcode_column_name, right_on='postal code', indicator=indicator_column)
        df_aux[validated_column] = df_aux[indicator_column] == 'both'
        return df_aux[[validated_column]]
    
    def augment_data(self, df:pd.DataFrame, zipcode_column_name:str) -> pd.DataFrame:
        """
        Function that uses the validate_zipcodes function and concatenates the result to the database
        
        :param df: Dataframe to extract features from.
        :type df: pandas.DataFrame

        :param zipcode_column_name: Zipcode column name
        :type zipcode_column_name: str

        :return: Return a dataframe with a new column.
        :rtype: DataFrame
        """
        df = pd.concat([df, self.validate_zipcodes(df, zipcode_column_name)], axis=1)
        return df
    
