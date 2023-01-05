import cv2
import authmecv as acv
import os
import pandas as pd

folder_path = '/Volumes/T7/TrainingDataPro/mobile_selfie'


'''
error | Problem
0 | Couldn't read video 
1 | Couldn't open file
2 | Total Frames equl to zero
'''

row_dict = {'video_path': [0], 'qualified': [0],
            'error_0': [0], 'error_1': [0], 'error_2': [0]}
row_df = pd.DataFrame.from_dict(row_dict)
out_df = row_df.copy()

for file_name in acv.Tqdm(os.listdir(folder_path)):
    row_df.loc[:] = 0
    file_path = os.path.join(folder_path, file_name)
    vid = cv2.VideoCapture(file_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    row_df.video_path = file_path

    if height > width:
        if width >= 720:
            row_df.qualified = 1

    if vid.read()[0] == False:
        row_df.error_0 = 1
    if vid.isOpened() == False:
        row_df.error_1 = 1
    if vid.get(cv2.CAP_PROP_FRAME_COUNT) == 0:
        row_df.error_2 = 1
    out_df = pd.concat([out_df, row_df], ignore_index=True)
out_df.drop([0], inplace=True)

out_df.loc[out_df.error_0 == 1, 'qualified'] = 0
out_df.loc[out_df.error_1 == 1, 'qualified'] = 0
out_df.loc[out_df.error_2 == 1, 'qualified'] = 0

breakpoint()
