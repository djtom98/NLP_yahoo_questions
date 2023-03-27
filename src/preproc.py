#%%
from datasets import load_dataset
data = load_dataset("../../NLP_yahoo_questions/tools/yahoo_answers_topics/yahoo_answers_topics.py")
# %%
import pandas as pd
# data['train']
'''
Dataset({
    features: ['id', 'topic', 'question_title', 'question_content', 'best_answer'],
    num_rows: 1400000
})
'''
#%%
import json
f = open('../../NLP_yahoo_questions/tools/yahoo_answers_topics/dataset_infos.json')
f1    = json.load(f)
f.close()
topics=f1['yahoo_answers_topics']['features']['topic']['names']
topics={k+1:v for k,v in enumerate(topics)}
# %%
import polars as pl
df=pl.from_arrow(data['train'].data.table)


####preprocessing
#%%
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string 

# %%
#@ Remove capitalization, stopwords, and punctuation
def process(text) : 
    #@ Remove punctuation/captizalization
    text = str(text)
    text = text.lower()
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    #@ Remove stopwords
    procList = [word for word in nopunc.split() if word not in stopwords.words('english')]
    return ' '.join(procList)

def cleanAndSave(df, dest) : 
    #@ Load data
    # df = pd.read_csv(source, names=['class', 'title', 'content', 'answer'])
    X1, X2, X3, Y = df['question_title'], df['question_content'], df['best_answer'], df['topic']
    #@ Empty lists to append everything to one column
    title, question, answer, topic = [], [], [], []
    
    #@ Process text
    for i in range(0, len(X1)) :  
        title.append(process(X1[i]))
        question.append(process(X2[i]))
        answer.append(process(X3[i]))
        topic.append(Y[i])

    #@ Merge processed text columns into dataframe and save
    df = pl.DataFrame({"title" : title, "question" : question, "answer" : answer, "topic" : topic})
    df['text'] = df['title'].map(str) + ' ' + df['question'].map(str) + ' ' + df['answer'].map(str)

    df_save = pl.DataFrame({'text': df['text'], "class" : df['class']})
    df_save.to_csv(dest, index=False)

cleanAndSave(df, '../../NLP_yahoo_questions/data/yahoo_train_notnull_clean.csv')
print('done') 
# %%
