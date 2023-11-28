import sys
import pandas as pd
import os
import csv

ans_dict = {'1_1_1': 3, '1_1_2': 1, '1_1_3': 2, '1_1_4': 4,
            '1_2_1': 5, '1_2_2': 2, '1_2_3': 5, '1_2_4': 5,
            '1_3_1': 1, '1_3_2': 1, '1_3_3': 5, '1_3_4': 4,

            '2_1_1': 4, '2_1_2': 3, '2_1_3': 4, '2_1_4': 2,
            '2_2_1': 5, '2_2_2': 5, '2_2_3': 1, '2_2_4': 4,
            '2_3_1': 3, '2_3_2': 3, '2_3_3': 1, '2_3_4': 5,

            '3_1_1': 2, '3_1_2': 1, '3_1_3': 5, '3_1_4': 5,
            '3_2_1': 3, '3_2_2': 5, '3_2_3': 5, '3_2_4': 4,
            '3_3_1': 4, '3_3_2': 3, '3_3_3': 3, '3_3_4': 3,

            '4_1_1': 1, '4_1_2': 2, '4_1_3': 5, '4_1_4': 4,
            '4_2_1': 4, '4_2_2': 4, '4_2_3': 5, '4_2_4': 3,
            '4_3_1': 4, '4_3_2': 5, '4_3_3': 4, '4_3_4': 2
            }

res_file = os.path.join('output', 'output_full_v1.csv')
if not os.path.exists(res_file):
    df = pd.DataFrame(columns=['No.', 'participant', 'type', 'exp_cnt', 'test', 'conf', 'ans', 'real_ans', 'res', 'te_time', 'res_time'])
    df.to_csv(res_file)

te_res_path = os.path.join('output', 'test', 'post_A')
te_res_list = os.listdir(te_res_path)

for te_f in te_res_list:
    elem = te_f.split('_')
    no = elem[1]
    participant = elem[2]
    type = elem[3] + elem[4]
    exp_cnt = elem[5].split('.')[0]

    df = pd.read_csv(os.path.join(te_res_path, te_f))
    test = 1
    for idx in range(1, 12, 2):
         ans = df.loc[idx+1]['ans']
         res = df.loc[idx+1]['res']
         conf = df.loc[idx+2]['confidence']
         # real_ans =
         te_time = df.loc[idx+1]['ts'] - df.loc[idx]['ts']
         conf_time = df.loc[idx+2]['ts'] - df.loc[idx+1]['ts']
         dict_key = exp_cnt + '_' + str(test) + '_' + str(idx%4)
         res_row = [no, participant, type, exp_cnt, test, conf, ans, ans_dict[dict_key], res, te_time, conf_time]
         test += 1
         #
         # with open(os.path.join(te_res_path, te_f), 'a', newline='') as f:
         #     writer = csv.writer(f)
         #     writer.writerow(res_row)