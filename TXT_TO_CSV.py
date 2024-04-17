import pandas as pd

# 원본 텍스트 파일 경로
input_file_path = './data/POWER_LIST.txt'
# 저장할 CSV 파일 경로
output_file_path = './data/POWER_LIST.csv'

# 텍스트 파일을 읽어들임. 구분자가 쉼표(,)인 경우
df = pd.read_csv(input_file_path, sep=',', engine='python', header=None)

# 열 이름을 추가할 수 있습니다. 실제 데이터에 맞게 열 이름을 조정해 주세요.
df.columns = ['Column1', 'Column2', 'Column3','Column4' ]

# 읽어들인 데이터프레임을 CSV 파일로 저장
df.to_csv(output_file_path, index=False)

print(f"'{output_file_path}' 파일에 데이터 저장 완료.")
