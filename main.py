# from satpy import available_readers
import os
import satpy
import glob
import matplotlib.pyplot as plt

# print(available_readers())

os.environ['XRIT_DECOMPRESS_PATH'] = '/opt/conda/pkgs/public-decomp-wt-2.8.1-h3fd9d12_1/bin/xRITDecompress'
channel_folders = ['IR_087___',
                   'VIS008___',
                   '_________',
                   'WV_073___',
                   'IR_016___',
                   'VIS006___',
                   'HRV______',
                   'IR_120___',
                   'IR_097___',
                   'IR_108___',
                   'IR_039___',
                   'IR_134___',
                   'WV_062___']
# file_name = "H-000-MSG2__-MSG2_IODC___-_________-EPI______-202308140600-__"

data_folder = r"/home/knn/Desktop/Test_Data/IODC/202308140600"

date_flag = "202308140600"
filenames = []
for f_ in channel_folders:
    for row in glob.glob1(os.path.join(data_folder, f_), f'H-000-MSG2*{date_flag}*'):
        print(row)
        filenames.append(os.path.join(data_folder, f_, row))

scn = satpy.Scene(reader='seviri_l1b_hrit', filenames=filenames)

seviri_data_names = ['HRV',
                     'IR_016',
                     'IR_039',
                     'IR_087',
                     'IR_097',
                     'IR_108',
                     'IR_120',
                     'IR_134',
                     'VIS006',
                     'VIS008',
                     'WV_062',
                     'WV_073']
scn.load(seviri_data_names)

scn.save_datasets(writer='cf', datasets=seviri_data_names, filename='seviri_test.nc',
                  groups={'visible': [row for row in seviri_data_names if row is not 'HRV'], 'hrv': ['HRV']})
pass
