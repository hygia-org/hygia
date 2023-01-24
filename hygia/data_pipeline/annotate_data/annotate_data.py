import pandas as pd

class AnnotateData:

    def annotate_data(self, df, concatened_column_name, ks_thresholds):
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

