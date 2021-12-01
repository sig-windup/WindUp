#wordcloud 생성
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def load_highlight_wordcloud(team, text, date):
    # db에서 team 이름 받아와서 사진 주소 들고와야함
    absolute = 'C:/Users/DeepLearning_1/PycharmProjects/WindUp/static/img/'
    logo = {'NC': 'NC.PNG', '두산': '두산.PNG', 'KT': 'KT.PNG', 'LG': 'LG.PNG', '키움': '키움.PNG',
            'KIA': 'KIA.PNG', '롯데': '롯데.PNG', '삼성': '삼성.PNG', 'SSG': 'SSG.PNG', '한화': '한화.PNG', '전체': 'cap.png'}
    mask = np.array(Image.open(absolute+logo[team]))
    mask_color = ImageColorGenerator(mask)
    wordcloud = WordCloud(font_path='C:/Users/DeepLearning_1/PycharmProjects/WindUp/static/SCDream5.otf', mask=mask, background_color='white',
                          max_words=20000, contour_color='steelblue').generate(text)
    wordcloud.recolor(color_func=mask_color)

    # 이미지 출력 및 저장
    # plt.figure(figsize=(22, 22))  # 이미지 크키
    # plt.imshow(wordcloud, interpolation='lanczos')  # 이미지의 부드럽기 정도
    # plt.axis('off')  # x y축 제거
    # plt.savefig(absolute + 'highlight/' + date + '.png')  # 파일명으로 저장
    wordcloud.to_file(absolute + 'highlight/' + team + date + '.png')

def load_predict_wordcloud(team, text, date, period):
    # db에서 team 이름 받아와서 사진 주소 들고와야함
    absolute = 'C:/Users/DeepLearning_1/PycharmProjects/WindUp/static/img/'
    logo = {'NC': 'NC.PNG', '두산': '두산.PNG', 'KT': 'KT.PNG', 'LG': 'LG.PNG', '키움': '키움.PNG',
            'KIA': 'KIA.PNG', '롯데': '롯데.PNG', '삼성': '삼성.PNG', 'SSG': 'SSG.PNG', '한화': '한화.PNG', '전체': 'cap.png'}
    mask = np.array(Image.open(absolute+logo[team]))
    mask_color = ImageColorGenerator(mask)
    wordcloud = WordCloud(font_path='C:/Users/DeepLearning_1/PycharmProjects/WindUp/static/SCDream5.otf', mask=mask, background_color='white',
                          max_words=20000, contour_color='steelblue').generate(text)
    wordcloud.recolor(color_func=mask_color)

    # 이미지 출력 및 저장
    # plt.figure(figsize=(22, 22))  # 이미지 크키
    # plt.imshow(wordcloud, interpolation='lanczos')  # 이미지의 부드럽기 정도
    # plt.axis('off')  # x y축 제거
    # plt.savefig(absolute + 'highlight/' + date + '.png')  # 파일명으로 저장
    wordcloud.to_file(absolute + 'predict/' + team + date + '_' + period+ '.png')

