import pandas as pd
from tsfresh import extract_features
import argparse
import warnings
warnings.filterwarnings("ignore")

def transfrom(input_file):
    df_re_im = pd.read_csv(input_file)

    parameters = {
    's0':{'fft_coefficient':[{'attr':'real','coeff':17},{'attr':'real','coeff':33},{'attr':'real','coeff':96}],'number_cwt_peaks':[{'n':1}]},
    's2':{'fft_coefficient':[{'attr':'angle','coeff':72}]},
    's1':{'fft_coefficient':[{'attr':'real','coeff':15}],'ar_coefficient':[{'coeff':1,'k':10}]},
    's3':{'fft_coefficient':[{'attr':'angle','coeff':77},{'attr':'real','coeff':48}]},
    }

    feature = extract_features(df_re_im, column_id="ID", column_sort="time",kind_to_fc_parameters=parameters)

    def cutoff(x,cutpoint):
        if x<=cutpoint:
            y = 0
        elif x>cutpoint :
            y = 1
        else:
            y = 2
        return y

    cols = feature.columns
    cols1 = cols.sort_values()
    df_reduced2 = feature[cols1]
    cols_rename = ['s0_fc_real_17','s0_ft_real_33','s0_ft_real_96','s0_np_1','s1_ar_10','s1_fc_real_15','s2_fc_angle_72','s3_fc_angle_77','s3_fc_real_48']
    df_reduced2.columns = cols_rename

    df_reduced2['s0_fc_real_17_group'] = df_reduced2['s0_fc_real_17'].apply(cutoff,args=(-18,))
    df_reduced2['s0_ft_real_33_group'] = df_reduced2['s0_ft_real_33'].apply(cutoff,args=(-3.7941,))
    df_reduced2['s0_ft_real_96_group'] = df_reduced2['s0_ft_real_96'].apply(cutoff,args=(-0.0877,))
    df_reduced2['s0_np_1_group'] = df_reduced2['s0_np_1'].apply(cutoff,args=(884,))
    df_reduced2['s1_ar_10_group'] = df_reduced2['s1_ar_10'].apply(cutoff,args=(2.3122,))
    df_reduced2['s1_fc_real_15_group'] = df_reduced2['s1_fc_real_15'].apply(cutoff,args=(-17.8,))
    df_reduced2['s2_fc_angle_72_group'] = df_reduced2['s2_fc_angle_72'].apply(cutoff,args=(-140,))
    df_reduced2['s3_fc_angle_77_group'] = df_reduced2['s3_fc_angle_77'].apply(cutoff,args=(95,))
    df_reduced2['s3_fc_real_48_group'] = df_reduced2['s3_fc_real_48'].apply(cutoff,args=(-16.0783,))

    df_reduced3 = df_reduced2.iloc[:,9:]
    return df_reduced3







