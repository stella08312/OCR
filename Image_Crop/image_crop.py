# -*- coding: utf-8 -*-

from PIL import Image
from tqdm import tqdm
import json
import os

"""
image_path : 크롭할 이미지들이 들어있는 최상위 폴더의 경로
json_path : 크롭할 이미지들의 정보가 들어있는 json파일의 최상위 폴더 경로

log_txt : 진행 중 발생하는 예외상황들의 로그를 기록할 txt파일
target_txt : 라벨값을 저장할 txt파일
"""
image_path = '{[원천]Training 폴더 경로}'
json_path = '{[라벨]Training 폴더 경로}'

log_txt = 'asset/label_data/text_in_wild_kor/crop_log.txt'
target_txt = 'asset/label_data/text_in_wild_kor/text_in_wild_target.txt'


"""
image_folder : 최상위 폴더에서 분류된 이미지들이 들어있는 폴더를 리스트로 받음
label_folder : 최상위 폴더에서 분류된 label들이 들어있는 폴더를 리스트로 받음

data_index : 중간에 오류가 생겼을 때 돌아갈 수 있는 백업 변수
Example : 
10000번째 data_index에서 어떠한 이유로 이미지 생성이 끊기면 data_index를 10000으로 변경해 그 지점부터
이미지를 크롭할 수 있게함

crop_index : 저장할 이미지의 접미어로 들어갈 값
"""
image_folder = os.listdir(image_path)
label_folder = os.listdir(json_path)
data_index = 0
crop_index = 1


with open(target_txt, 'w', encoding='UTF-8') as target:
    with open(log_txt, 'a', encoding='UTF-8') as error:
        # crop할 이미지가 들어있는 폴더 불러오기
        for f in range (0, len(os.listdir(image_path))):
            # 이미지와 라벨파일을 리스트로 저장
            images = os.listdir(image_path+'/'+image_folder[f])
            labels = os.listdir(json_path+'/'+label_folder[f])
            # 폴더를 순회하면서 이미지 크롭 및 라벨 생성
            for i in tqdm(range(0, len(images))):
                with open(json_path+'/'+label_folder[f]+'/'+labels[i], encoding='UTF-8') as json_file:
                    """
                    json_data : json파일을 읽어온 변수
                    file_name : json_data에서 이미지의 이름을 읽어온 변수
                    """
                    json_data = json.load(json_file)
                    file_name = json_data["images"][0]["file_name"]
                    if file_name not in images:
                        # 라벨값에 존재하지만 이미지가 없는 파일 처리
                        error.write('[Not exist]data_index: ' + str(data_index) + ' crop_index: ' + str(crop_index) + ' ' + file_name + '\n')
                        data_index+=1
                        continue
                    for j in range(len(json_data["annotations"])):
                        """
                        bbox : json_data에서 크롭할 bbox값을 불러와 저장한 변수
                        text : json_data에서 크롭할 이미지의 타겟값을 불러와 저장한 변수
                        """
                        bbox = tuple(json_data["annotations"][j]["bbox"])
                        text = json_data["annotations"][j]["text"]

                        if bbox[0] == None:
                            # bbox값이 존재하지않는 오류 처리
                            error.write('[Bbox Err]data_index: ' + str(data_index) + ' crop_index: ' + str(crop_index) + ' ' + file_name + '\n')
                            continue
                        elif bbox[2] < 0 or bbox[3] < 0:
                            # bbox값이 음수값으로 되어있어 크롭이 잘 되지 않는 이미지 처리
                            error.write('[Bbox Err]data_index: ' + str(data_index) + ' crop_index: ' + str(crop_index) + ' ' + file_name +'\n')
                            continue
                        elif text != 'xxx' and text != 'XXX' and bbox is not None:
                            # 라벨값이 xxx인 이미지 처리 및 load할 수 없는 이미지 처리
                            try:
                                img = Image.open(image_path + '/' + image_folder[f] + '/' + file_name)
                                img.load()
                            except OSError as err:
                                error.write('[Trunc Err]data_index: ' + str(data_index) + ' crop_index: ' + str(crop_index) + ' ' + file_name +'\n')
                                continue

                            # 라벨데이터 생성  {대회훈련데이터_크롭_X.jpg}\t{타겟값}\n
                            target.write('대회훈련데이터_크롭'+ str(crop_index) + '.jpg\t' + text + '\n')
                            croppedImage = img.crop((bbox[0], bbox[1], bbox[0]+bbox[2], bbox[1]+bbox[3]))
                            # 크롭된 이미지 저장    {대회훈련데이터_크롭_X.jpg}
                            croppedImage.save('{크롭이미지를 저장할 폴더경로}/대회훈련데이터_크롭'+ str(crop_index) + '.jpg')
                            crop_index += 1
                    data_index+=1