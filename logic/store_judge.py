from pymongo import MongoClient
from logic.reinforce import relearning
import os
import csv

conn = MongoClient("mongodb://windup_dba:lotsamhwa@114.129.200.203:28018")
db = conn['windup']
col = db['reinforce']
count = 0

def storeDB(article_sentences, labels):
    for i in range(len(labels)):
        doc = {'sentence': article_sentences[i], 'label': labels[i]}
        try:
            col.insert(doc)
        except:
            print('cannot insert data')
    print('DB 저장 완료!')


def makeCSV():
    path = 'C:/Users/DeepLearning_1/PycharmProjects/WindUp/static/data'
    file_name = 'reinforce.csv'

    judges = list(col.find({}))
    with open(os.path.join(path, file_name), 'w', newline='', encoding='utf-8') as output:
        csvout = csv.DictWriter(output,['id', 'sentence', 'label'])
        csvout.writeheader()
        for judge in judges:
            wr = csv.writer(output)
            wr.writerow([ judge['_id'] , judge['sentence'], judge['label'] ])
    print('CSV 저장 완료!')


def start_reinforce():
    relearning()
    print('강화 학습 완료!')
    judges = list(col.find({}))
    for judge in judges:
        col.remove(judge)
    print('기존 데이터 삭제 완료!')