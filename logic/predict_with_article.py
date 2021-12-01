from logic.language_model import test_sentences

def get_contents(article_objects):
    contents = []
    for ao in article_objects:
        contents.append(ao.content)
    return contents

def article_label(article):
    article_sentence = article.split('.')
    positive = []
    negative = []
    for sent in article_sentence:
        label = test_sentences([sent])
        #print(sent, '[predict]', label)
        if label == 1:
            positive.append('*')
        elif label == 2:
            negative.append('*')
    # print('======================')
    # print('positive:', len(positive))
    # print('negative:', len(negative))
    # print('all:', len(article_sentence))
    if len(positive)/len(article_sentence) > len(negative)/len(article_sentence):
        return 1
    else:
        return 0


def positive_score(articles):
    score = 0
    for a in articles:
        score += article_label(a)
    return score / len(articles)
