import requests
import pandas as pd

# API run URL로변경해주세요
url = 'https://api.apify.com/'

# 전체 데이터 수로 변경해주세요
total_items = 1624  # 전체 데이터 수
limit = 1000  # 한 번에 가져올 최대 데이터 수

# 데이터를 저장할 리스트
all_items = []

# 페이지 수 계산
num_pages = (total_items // limit) + (1 if total_items % limit > 0 else 0)

for page in range(num_pages):
    offset = page * limit
    params = {
        'offset': offset,
        'limit': limit,
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        all_items.extend(data['data']['items'])  # 데이터 수집
    else:
        print("Failed to fetch data from API. Status code:", response.status_code)
        break

# DataFrame으로 변환
df_all = pd.DataFrame(all_items)

# 확인을 위해 DataFrame의 일부 출력
print(df_all.head())

# 엑셀 파일로 내보내기 (선택 사항)
df_all.to_excel('all_actor_runs.xlsx', index=False)
print("Excel file 'all_actor_runs.xlsx' has been created successfully.")
