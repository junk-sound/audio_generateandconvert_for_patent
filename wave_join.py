import glob
from pydub import AudioSegment

'''음악소스 데이터베이스 내 음악소스 리스트입니다.'''
source_lst = glob.glob('/Users/junksound/문서/프로젝트 학기제/특허/특허피피티관련/171116/motivation_howitworks/shemakesme_snare2.wav')
'''데이터베이스 내 음악소스들과 합치기 위해 생성한 웨이브파일입니다.'''
source_mix_lst = glob.glob('/Users/junksound/문서/프로젝트 학기제/특허/특허피피티관련/171116/waves_generated/*')

'''음악소스와 그에 해당하는 웨이브들을 합쳐줍니다.'''
for source in source_lst:
    source_wa_name = source.split('/')[-1]
    sound1 = AudioSegment.from_file(source)
    for source_mix in source_mix_lst:
        print(source_mix)
        source_mix_back_name=source_mix.split('/')[-1].split('_')[1]+'_'+source_mix.split('/')[-1].split('_')[2]+'_'+source_mix.split('/')[-1].split('_')[3][:-4]
        print(source_mix_back_name)
        source_mix_front_wa_name = source_mix.split('/')[-1].split('_')[0] + '.wav'
        source_mix_front_name = source_wa_name.split('.')[0]
        print(source_wa_name)
        print(source_mix_front_name)
        sound2 = AudioSegment.from_file(source_mix)
        combined_wav = sound1.overlay(sound2)
        combined_wav.export('/Users/junksound/문서/프로젝트 학기제/특허/특허피피티관련/171116/waves_combined/'+source_mix_front_name+'_'+source_mix_back_name+'.wav', format='wav')






