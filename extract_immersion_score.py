import pandas as pd

# 엑셀 파일을 DataFrame으로 읽어오기
data = pd.read_excel('파일경로/파일이름.xlsx')

# 각 행의 숫자를 더하고 평균값 구하기
averages = []
for i in range(len(data)):
    row = data.iloc[i]
    numbers = row[1:5]  # 2번째부터 5번째까지의 숫자 선택
    total = sum(numbers)  # 숫자들의 합 구하기
    average = total / len(numbers)  # 평균값 계산
    averages.append(average)

# 평균값 출력
for i, average in enumerate(averages):
    print(f'{i+1}번째 행의 평균값: {average}')