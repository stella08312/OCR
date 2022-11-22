# -*- coding: utf-8 -*-

"""
대회훈련데이터의 csv파일을 불러와 LMDB생성에 필요한 라벨을 만듦

csv_file : 대회훈련데이터 csv파일 경로
txt_file : 라벨을 저장할 txt파일의 경로
"""
def csv_to_target(csv_file, txt_file):
    with open(txt_file, 'w', encoding='UTF-8') as txt_file:
        with open(csv_file, 'r', encoding='UTF-8') as csv_file:
            csv = csv_file.readlines()
            csv = list(map(lambda s: s.strip('./train'), csv))
            csv = list(map(lambda s: s.strip(), csv))
            csv = list(map(lambda s: s.split(','), csv))
            for i in range(1, len(csv)):
                txt_file.write('train' + csv[i][0] + '\t' + csv[i][1] +'\n')

csv_to_target(R'{대회훈련데이터.csv파일의 경로}', 'asset/label_data/competition_train_data/dacon_train_target.txt')