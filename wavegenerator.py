import wavebender
import librosa.display
import glob

'''음악 소스 데이터베이스의 음악 소스들을 불러옵니다.'''
source_lst = glob.glob('/Users/junksound/문서/프로젝트 학기제/특허/특허피피티관련/171116/motivation_howitworks/shemakesme_snare2.wav')

'''생성하고자 하는 주파수 리스트입니다.'''
frequency_lst = [32.7032,34.6478,36.7081,38.8909,41.2032,43.6535,46.2493,48.9994, 391.9954,440.0, 493.8833, 523.2511,6644.875,7040.0000,7458.620,7902.133]
'''생성하고자 하는 볼륨 리스트입니다.'''
volume_lst = [0.1,0.5,0.9]


'''wavebender를 사용하여 음악 소스 데이터베이스 내의 음악소스들과 같은 재생 시간을 가지고, 다양한 주파수, 볼륨, 파형을 갖는 오디오를 생성합니다.'''
for source in source_lst:
    y, sr = librosa.load(source, sr=44100)
    duration = int(librosa.get_duration(y=y, sr=sr)) + 1
    source_wa_name = source.split('/')[-1]
    source_name = '/Users/junksound/문서/프로젝트 학기제/특허/특허피피티관련/171116/waves_generated/'+source_wa_name.split('.')[0]
    for frequency in frequency_lst:
        file_sine_name = source_name + '_' +'sine_'+str(frequency)+ '.wav'
        wavebender.main_sine(frequency, 0.6, duration, file_sine_name)
        file_sqaure_name = source_name +'_'+'sqare_'+str(frequency) + '.wav'
        wavebender.main_square(frequency, 0.6, duration, file_sqaure_name)






