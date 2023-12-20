import pandas as pd
import os
import csv
from sklearn.preprocessing import minmax_scale
import numpy as np

# D:\Edu_main\3. Immersion_score\total
root_path = 'D:\\Edu_main\\3. Immersion_score\\total'
score_dir_list = os.listdir(root_path)
score_dir_list.sort()

res_file = os.path.join('output', 'output_i_score_norm_v2.csv')
# res_col = ['No.', 'participant', 'type', 'exp_cnt', 'test', 'i_score_prompt']
res_col = ['No.', 'participant', 'type', 'exp_cnt', 'test', 'i_score_prompt', 'norm_i_score_prompt']
if not os.path.exists(res_file):
    with open(res_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(res_col)

for p_dir in score_dir_list:
    elem = p_dir.split('_')
    no = elem[0]
    participant = elem[1]
    # type = 'post'

    p_dir_path = os.path.join(root_path, p_dir)
    lec_list = os.listdir(p_dir_path)
    lec_list.sort()
    print('working on ', p_dir)

    for score_dir in lec_list:
        test = 1
        exp_cnt = score_dir.split('_')[0][-1]
        score_path = os.path.join(root_path, p_dir, score_dir)
        score_df = pd.read_csv(os.path.join(score_path, 'score.txt'), sep=",", engine='python', encoding="cp949")

        with open(os.path.join(score_path, 'score.txt'), 'r') as f:
            data = f.readlines()

        # 각 행의 숫자를 더하고 평균값 구하기
        averages = []
        tmp_numbers = []
        norm_averages = []
        for dline in data:
            row = dline.split(',')
            numbers = row[1:5]  # 2번째부터 5번째까지의 숫자 선택
            numbers = list(map(int, numbers))
            tmp_numbers.append(numbers)

            total = sum(numbers)  # 숫자들의 합 구하기
            average = total / len(numbers)  # 평균값 계산
            averages.append(average)

            # norm_numbers = minmax_scale(numbers) -> 다시 작성필요 (한 사람 데이터 모두 모은 뒤에 minmax norm 필요 / 4회차 x 회차 당 3회 x 1회 당 점수 4개 평균)
            # norm_total = sum(norm_numbers)
            # norm_average = norm_total / len(norm_numbers)
            # norm_averages.append(norm_average)

        # flatten = sum(tmp_numbers, [])
        flatten = np.concatenate(tmp_numbers).tolist()
        norm_numbers = minmax_scale(flatten)
        reshape_norm_numbers = np.array(norm_numbers).reshape(3, 4)
        for norm_num_row in reshape_norm_numbers:
            total = sum(norm_num_row.tolist())
            # total = sum(norm_num_row)
            average = total / len(norm_num_row)
            norm_averages.append(average)

        res_row_list = []
        # for avg in averages:
        #     res_row_list.append([no, participant, 'post', exp_cnt, test, avg])
        #     res_row_list.append([no, participant, 'pre', exp_cnt, test, avg])
        #     test += 1
        #     res_row_list.append([no, participant, 'post', exp_cnt, test, avg])
        #     res_row_list.append([no, participant, 'pre', exp_cnt, test, avg])
        #     test += 1


        # ver. normalization
        for avg, norm_avg in zip(averages, norm_averages):
            res_row_list.append([no, participant, 'post', exp_cnt, test, avg, norm_avg])
            res_row_list.append([no, participant, 'pre', exp_cnt, test, avg, norm_avg])
            test += 1
            res_row_list.append([no, participant, 'post', exp_cnt, test, avg, norm_avg])
            res_row_list.append([no, participant, 'pre', exp_cnt, test, avg, norm_avg])
            test += 1

        with open(res_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(res_row_list[0])
            writer.writerow(res_row_list[1])
            writer.writerow(res_row_list[2])
            writer.writerow(res_row_list[3])
            writer.writerow(res_row_list[4])
            writer.writerow(res_row_list[5])
            writer.writerow(res_row_list[6])
            writer.writerow(res_row_list[7])
            writer.writerow(res_row_list[8])
            writer.writerow(res_row_list[9])
            writer.writerow(res_row_list[10])
            writer.writerow(res_row_list[11])
