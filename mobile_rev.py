import cv2
import authmecv as acv
import os
import pandas as pd

all_path = './mobile/mobile_v2_fin.csv'
v1_path = './mobile/mobile_v1.csv'

all_df = pd.read_csv(all_path)
v1_df = pd.read_csv(v1_path)

all_qualified = all_df.loc[all_df.qualified==1, :]
all_unqualified = all_df.loc[all_df.qualified==0, :]
all_err0_df = all_df.loc[all_df.error_0==1, :]
all_err1_df = all_df.loc[all_df.error_1==1, :]
all_err2_df = all_df.loc[all_df.error_2==1, :]


v1_err0_df = v1_df.loc[v1_df.error_flg_0==1, :]


breakpoint()