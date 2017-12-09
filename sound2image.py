import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import glob


'''음악소스와 생성한 웨이브를 합친 오디오들을 이미지화합니다.'''
source_lst = glob.glob('/Users/junksound/문서/프로젝트 학기제/특허/특허피피티관련/171116/waves_combined/*')
data_lst = []
fs_lst = []
for idx, source in enumerate(source_lst):
    source_wa_name = source.split('/')[-1]
    source_name = '/Users/junksound/문서/프로젝트 학기제/특허/특허피피티관련/171116/imgs_combined/' + source_wa_name.split('.')[0]
    data, fs = librosa.load(source, sr=44100)
    melspecs = librosa.feature.melspectrogram(y=data, sr=fs, n_fft=2048, n_mels=128)
    librosa.display.specshow(librosa.power_to_db(melspecs, ref=np.max),x_axis='time', y_axis='mel', fmax=fs)
    if idx == 0:
        plt.colorbar(format='%+2.0f dB')
    plt.savefig(source_name)




