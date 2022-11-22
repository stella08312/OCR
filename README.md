# Summary

> [DACON] SW Centered AI Competetion </br>
> Solution of [한밭대학교] AIM. Lab. team </br>

Prize : 🥉10th (10/77) </br>
Valid Accuracy : 96.209 </br>
Private Score : 93.343 </br>


## Image_Crop
Some python files to make crop images, target file. </br>
</br>
**create_valid_target.py** : Create target.txt file to make LMDB</br>

**image_crop.py** : Create crop images to make LMDB</br>
</br>

## deep-text-recognition-benchmark
Everything is same as clova-ai deep-text-recognition-benchmark model, except **make_csv.py** that i added to make submission file. </br>
And i changed load model(39\~47 line), print and write prediction(102\~105 line) part in **demo.py** </br>
</br>

## experiment_setting
Literally the environments i used for train & predict. </br>
</br>
**OS.txt** : Settings such as GPU, CUDA...</br>
**requirements.txt** : these are package settings</br>
**torch_requirements.txt** : these are torch settings</br>
</br>

## [HNU]AIM_Lab_Reproduce.pdf
Explain how to reproduce my competition solution. </br>
</br>
language : Korean</br>
</br>

## Links
#### Model source : https://github.com/clovaai/deep-text-recognition-benchmark
#### Using Image : https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=105
