# transform_trg
- 영화진흥위원회 openAPI 을 이용한 영화 박스오피스 데이터 ETL 과정 중 변환단계
- 특정 날짜의 박스오피스 데이터를 Parquet 파일에서 읽어와서 필요한 열만 추출하고, 중복된 영화 데이터를 처리한 후, 최종적으로 결과를 반환하는 기능을 수행

## 실행
```bash
# 레퍼지토리 clone, 해당 디렉터리 이동
$ git clone git@github.com:7-TRG/transform_trg.git
$ cd ~/code/transform_trg

# 가상환경 활성화 및 필요 패키지 설치
$ pdm init
$ source .venv/bin/activate
$ pdm install
$ pdm add 
```

