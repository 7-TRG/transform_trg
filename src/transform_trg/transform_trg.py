import pandas as pd
def mer(load_dt='20170101'):
    df = pd.read_parquet('~/code/7_TRG/data_parquet')
    cols = ['movieCd', #영화의 대표코드를 출력합니다.
       'movieNm', #영화명(국문)을 출력합니다.
        'openDt', #영화의 개봉일을 출력합니다.
        'salesAmt',
        'audiCnt', #해당일의 관객수를 출력합니다.
        'load_dt', # 입수일자
        'multiMovieYn', #다양성영화 유무
        'repNationCd', #한국외국영화 유무
       ]
    # 해당 열만 추출
    df2 = df[cols]
    # airflow 날짜 받는곳
    df_where = df2[df2['load_dt'] == int(load_dt)] # 날짜 받을때 정수형이여야 함

    result = [] # 결과 들어갈 자리

    for ind in set(df_where['movieNm']):
        if len(df_where[df_where['movieNm'] == ind]) > 1:
            df4 = df_where[df_where['movieNm'] == ind]
            df4['repNationCd'] = df_where[df_where['movieNm'] == ind].iloc[1]['repNationCd']
            result.append(list(df4.iloc[0]))
        # 아닌 애들은 그냥 list에 append
        else:
            result.append(list(df_where[df_where['movieNm'] == ind].iloc[0]))

    df_where = pd.DataFrame(result, columns = df2.columns)
    # 타입 변경
    df_where['load_dt'] = df_where['load_dt'].astype('object')
    df_where['multiMovieYn'] = df_where['multiMovieYn'].astype('object')
    df_where['repNationCd'] = df_where['repNationCd'].astype('object')
    # 결측치 값 변환
    df_where.fillna('unknown', inplace = True)

    return df_where
