import pandas as pd

# 원본 CSV 파일 경로
input_file_path = './RAM_CSV_ORIGINAL.csv'
# 저장할 새 CSV 파일 경로
output_file_path = './data/RAM_CSV.csv'

# CSV 파일을 읽어들임. 이 파일에는 헤더가 없다고 가정합니다.
# 헤더가 있다면 header=None 부분을 제거하세요.
df = pd.read_csv(input_file_path, header=None, engine='python')

# 새로운 데이터프레임을 초기화합니다.
new_df = pd.DataFrame()

# 모든 행에 대해 반복
for index, row in df.iterrows():
    # 현재 행의 첫 번째 열을 '/'로 나눕니다. expand=True는 나눈 결과를 새로운 데이터프레임으로 확장합니다.
    split_data = row[0].split(' / ')
    # 나누어진 데이터를 새로운 데이터프레임에 추가합니다.
    new_df = new_df._append([split_data], ignore_index=True)

# 열 이름 설정 (필요한 경우에 따라 조정하세요)
#new_df.columns = ['Column1', 'Column2', 'Column3', 'Column4']

# 결과 데이터프레임을 새로운 CSV 파일로 저장합니다.
new_df.to_csv(output_file_path, index=False)

print(f"'{output_file_path}' 파일에 데이터 저장 완료.")
