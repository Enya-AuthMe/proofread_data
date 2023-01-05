import cv2
import authmecv as acv
import os
import pandas as pd


folder_path = '/Volumes/T7/TrainingDataPro/ori'
csv1_path = '/Volumes/T7/TrainingDataPro/selfie_video_dataset.csv'
csv2_path = '/Volumes/T7/TrainingDataPro/SelfieVideoDataset_151.csv'

csv1 = pd.read_csv(csv1_path, sep=';')
csv2 = pd.read_csv(csv2_path, sep=';')

main_ls = []
for f_name in os.listdir(folder_path):
    main_ls.append(f_name)
main_df = pd.DataFrame(main_ls, columns=['file_name'])

csv1_df = csv1.Link.drop_duplicates().to_frame()
csv2_df = csv2.Link.drop_duplicates().to_frame()

for i, path in enumerate(csv1_df.Link):
    csv1_df.Link.iloc[i] = path.split('/').pop()
for i, path in enumerate(csv2_df.Link):
    csv2_df.Link.iloc[i] = path.split('/').pop()

csv1_df = csv1_df.rename(columns={'Link': 'file_name'})
csv2_df = csv2_df.rename(columns={'Link': 'file_name'})

mrg1 = pd.merge(main_df, csv1_df, on='file_name', how='outer', indicator=True)
mrg2 = pd.merge(main_df, csv2_df, on='file_name', how='outer', indicator=True)

missing1_df = mrg1.loc[mrg1._merge=='right_only', 'file_name']
missing2_df = mrg2.loc[mrg2._merge=='right_only', :]

missing1_df.to_csv('./tmp.csv', index=False)

breakpoint()
