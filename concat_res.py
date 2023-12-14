import sys
import pandas as pd
import csv
import os

ans_dict = {'1_1_1': 3, '1_1_2': 1, '1_1_3': 2, '1_1_4': 4, # postA_1-1 preA_1-1 postA_1-2 preA_1-2
            '1_2_1': 5, '1_2_2': 2, '1_2_3': 5, '1_2_4': 5, # postA_1-3 preA_1-3 postA_1-4 preA_1-4
            '1_3_1': 1, '1_3_2': 1, '1_3_3': 5, '1_3_4': 4, # postA_1-5 preA_1-5 postA_1-6 preA_1-6
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

res_file = os.path.join('output', 'output_full_v2.csv')
res_col = ['No.', 'participant', 'type', 'exp_cnt', 'test', 'conf', 'ans', 'real_ans', 'res', 'te_time', 'res_time']
if not os.path.exists(res_file):
    # df = pd.DataFrame(columns=res_col)
    # df.to_csv(res_file)\
    with open(res_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(res_col)

 # 1_1_1, 1_1_3, 1_2_1, ... , 4_3_3 // line 57
# te_res_path = os.path.join('output', 'test', 'post_A')
# te_res_path = os.path.join('output', 'test', 'pre_B')

# 1_1_2, 1_1_4, 1_2_2, ... , 4_3_4 // line 58
# te_res_path = os.path.join('output', 'test', 'post_B')
te_res_path = os.path.join('output', 'test', 'pre_A')
te_res_list = os.listdir(te_res_path)

for te_f in te_res_list:
    print('working on ', te_f)
    elem = te_f.split('_')
    no = elem[1]
    participant = elem[2]
    type = elem[3] + elem[4]
    exp_cnt = elem[5].split('.')[0]

    df = pd.read_csv(os.path.join(te_res_path, te_f))
    test = 1
    dict_idx = 1
    for idx in range(1, 12, 2):
         status = df.loc[idx+1]['status']
         ans = df.loc[idx+1]['ans']
         res = df.loc[idx+1]['res']
         conf = df.loc[idx+2]['confidence']
         # real_ans =
         te_time = df.loc[idx+1]['ts'] - df.loc[idx]['ts']
         conf_time = df.loc[idx+2]['ts'] - df.loc[idx+1]['ts']
         # dict_key = exp_cnt + '_' + str(dict_idx) + '_' + str(idx%4) # for post_A & pre_B
         dict_key = exp_cnt + '_' + str(dict_idx) + '_' + str(idx%4+1) # for post_B & pre_A
         res_row = [no, participant, type, exp_cnt, test, conf, ans, ans_dict[dict_key], res, te_time, conf_time]

         # res_df = df.DataFrame(res_row, column=res_col)
         if (dict_key[-1]=='3') or (dict_key[-1]=='4'): # '3' for post_A & pre_B / '4' for post_B & pre_A
             dict_idx += 1
         test += 1
         # res_df.to_csv(res_file, header=False)

         with open(res_file, 'a', newline='') as f:
             writer = csv.writer(f)
             writer.writerow(res_row)