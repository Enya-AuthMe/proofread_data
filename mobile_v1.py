import cv2
import authmecv as acv
import os
import pandas as pd

folder_path = '/Volumes/T7/TrainingDataPro/mobile_selfie'

row_dict = {'video_path': [0], 'error_flg_0': [0]}
row_df = pd.DataFrame.from_dict(row_dict)
out_df = row_df.copy()

for file_name in acv.Tqdm(os.listdir(folder_path)):
    row_df.loc[:] = 0
    file_path = os.path.join(folder_path, file_name)
    vid = cv2.VideoCapture(file_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    if height > width:
        if width >= 720:
            row_df.video_path = file_path
            if vid.read()[0] == False:
                row_df.error_flg_0 = 1
            out_df = pd.concat([out_df, row_df], ignore_index=True)
out_df.drop([0], inplace=True)


'''
error_flg | Problem
0 | Couldn't read video 
1 | Could'nt open file
2 | Total Frames equl to zero
3 | ???
4 | ???

'''
breakpoint()
