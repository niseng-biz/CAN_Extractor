#-------------------------------------------------------------------------------
# Name:        CAN Extractor
# Author:      Naoshi Nishihashi
# Created:     16/07/2022
#
# Licence: GNU LESSER GENERAL PUBLIC LICENSE
#          Version 3, 29 June 2007
# ----------------------------------------------------------------------
# Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.
# ----------------------------------------------------------------------
#-------------------------------------------------------------------------------

import can.io.blf as can_io_blf
import can.io.asc as can_io_asc
import pickle
from CDW import CANDataWrapper


def main():
    csv_flag = 1
    path_config = 'Configuration.cfg'
    with open(path_config ,encoding="utf-8") as f_r_cfg:
        cfg_line = f_r_cfg.readlines()

    data_file_path = cfg_line[0].replace('\n','')

    #get extention
    ext_index = data_file_path.rfind('.')
    ext = data_file_path[ext_index:]

    # Read Data File
    if ext == '.blf':
        can_data = can_io_blf.BLFReader(data_file_path)
    elif ext == '.asc':
        can_data = can_io_asc.ASCReader(data_file_path)

    msg_list = [x for x in can_data]

    #time length of data
    if ext == '.blf':
        max_data_count = can_data.object_count
        file_time_start = can_data.start_timestamp
        file_time_end =can_data.stop_timestamp
    else:
        with open(data_file_path) as f_r_asc:
            asc_line = f_r_asc.readlines()
        max_data_count = len(asc_line)

        for i in range(len(asc_line)):
            split_id = asc_line[i].index(' ')
            file_time_start = asc_line[i][:split_id-2].replace(' ', '').replace('\n','')
            try:
                file_time_start = float(file_time_start)
                break
            except:
                pass

        for i in range(len(asc_line)):
            split_id = asc_line[-i-1].index(' ')
            file_time_end = asc_line[-i-1][:split_id-2].replace(' ', '').replace('\n','')
            try:
                file_time_end = float(file_time_end)
                break
            except:
                pass

    can_data_wrap = CANDataWrapper(DataCount = max_data_count, StartTime = file_time_start, EndTime = file_time_end, Contents = msg_list)

    file_name = 'CAN_Data.pkl'
    try:
        with open(file_name, 'wb') as f:
                pickle.dump(can_data_wrap, f)
        state = 'finish'

    except:
        state = 'error'

    # read for check
    with open(file_name, 'rb') as f:
        CANDatas = pickle.load(f)
    CANDatas.show_attributes()

    print(CANDatas.Contents[1])
    print(type(CANDatas.Contents[1]))


    return state


if __name__ == '__main__':
    main()
