# -*- coding: utf-8 -*-
import pandas as pd
test_predicts = '{인코딩을 변경할 csv파일의 경로}'

submit = pd.read_csv(test_predicts, encoding='cp949')
submit.to_csv('{변경된 인코딩의 csv파일을 저장할 경로}', index=False, encoding="utf-8-sig")