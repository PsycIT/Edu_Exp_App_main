import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import scipy.stats as stats

sns.set_theme(color_codes=True)
df = pd.read_excel(os.path.join('output', 'output_full_v2(1).xlsx'))

# 'conf' 열과 'i_score_prompt' 열의 상관관계 분석
# correlation1, p_value1 = stats.pearsonr(df['conf'], df['i_score_prompt'])
# covariance1 = df['conf'].cov(df['i_score_prompt'])
# print("상관계수(conf vs i_score_prompt):", correlation1)
# print("공분산(conf vs i_score_prompt):", covariance1)
correlation1, p_value1 = stats.pearsonr(df['conf'], df['norm_i_score_prompt'])
covariance1 = df['conf'].cov(df['norm_i_score_prompt'])
print("상관계수(conf vs norm_i_score_prompt):", correlation1)
print("공분산(conf vs norm_i_score_prompt):", covariance1)
print("상관계수 검정 결과(p-value):", p_value1)

# 'res' 열과 'conf' 열의 상관관계 분석
correlation2, p_value2 = stats.pearsonr(df['res'], df['conf'])
covariance2 = df['res'].cov(df['conf'])
print("\n상관계수(res vs conf):", correlation2)
print("공분산(res vs conf):", covariance2)
print("상관계수 검정 결과(p-value):", p_value2)

# 'res' 열과 'i_score_prompt' 열의 상관관계 분석
# correlation3, p_value3 = stats.pearsonr(df['res'], df['i_score_prompt'])
# covariance3 = df['res'].cov(df['i_score_prompt'])
# print("\n상관계수(res vs i_score_prompt):", correlation3)
# print("공분산(res vs i_score_prompt):", covariance3)
correlation3, p_value3 = stats.pearsonr(df['res'], df['norm_i_score_prompt'])
covariance3 = df['res'].cov(df['norm_i_score_prompt'])
print("\n상관계수(res vs norm_i_score_prompt):", correlation3)
print("공분산(res vs norm_i_score_prompt):", covariance3)
print("상관계수 검정 결과(p-value):", p_value3)
