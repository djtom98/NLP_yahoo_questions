# Classification of Yahoo Answers

### Introduction

### Data

[Yahoo! Answers](https://en.wikipedia.org/wiki/Yahoo!_Answers) was a forum where users could ask and answer questions that other users have posted. These posts go under ‘topics’, which naturally allows for a classification task- classifying these posts to the correct topic based on textual content. Huggingface provides a [large dataset](https://huggingface.co/datasets/yahoo_answers_topics) comprised of 2 million Yahoo! Answers posts, which includes Topic, Question Title, Question Content, and Best Answer. Within this dataset, there are ten balanced topics/classes, namely:

In order to be less constrained by computational power and allow for more exploration of the data and models, we select the first three topics. These topics are: Health, Science & Mathematics,  and Society & Culture. We also sample 100,000 rows from the dataset of 2 million. We split this sample of 100,000 observations into 70,000 training observations and 30,000 test observations.


### Preprocessing

Data preprocessing:
+ Replace the topic number with its name to have a general understanding about the data
+ Remove the punctuation and stopwords
+ Remove the special characters (html tags) e.g '<br />' , '\\n' with regex
+ Optional:stemming,lemmatization
+ Merge title, question and answer into one column

EDA:
+ Plot histogram of topic distribution
+ Exploring NaN values in dataset
+ Word cloud:show the most frequent words in the all columns and by topic

# Models

### Baseline Model 

A baseline model is a simple model that serves as a starting point for building more complex models. It provides a reference point for evaluating the performance of more sophisticated models.
In order to analize different starting points we defined three different baseline models.

#### Ruled based model

+ Gets as inputs a dictionnary for each topic with the fifty most common words
+ For each sentence find the dictionary with more coincidences and classify the text under that topic
+ Calculate precision, recall, f1-score and the confusion matrix for the model

#### TF-IDF + Logistic Regression

+ We create a bag of words with Count Vectorizer 
+ Then we used a TF-IDF transformer
+ Finally we run a Logistic Regression can calculate the metrics

#### Decision Tree Classifier

+ Run a Decision Tree Classifier 

### RNN-LSTM
To implement RNN, we used the Keras package to create a neural network, by using LSTM layers which are part of the implementation. Embedding layer using Glove is also added to the model to improve the performance. Initially our performance with this was poor, so we added dropout layers, which seems to reduce overfitting, and we got a better performance as a result. 
### BERT
To implement BERT, we used a package called ktrain. One of the pre-trained models included in ktrain is BERT, which stands for Bidirectional Encoder Representations from Transformers. BERT is a type of deep neural network that's been pre-trained on a large corpus of text data, using a technique called masked language modeling. This involves randomly masking out words from a sentence and training the model to predict the masked words based on the surrounding context.

This network took the most time to train, yet in the end it yielded the best results- slightly above our baseline logistic regression model.

# Analysis

We provide a comparison of the models based on the average precision, recall, and accuracy for the three classes:
## Performance Comparison
|                      | Avg Precision | Avg Recall | Avg Accuracy |
|----------------------|---------------|------------|--------------|
| Baseline             |     .880      |    .880    |     .880     |
| RNN                  |     .809      |    .808    |     .808     |
| Bert                 |     .896      |    .896    |     .896     |

## Baseline Model
Below we provide the probability of each class for the TF-IDF + Logistic Regression model:
![TF_IDF_Logistic_regression.png](https://github.com/djtom98/NLP_yahoo_questions/blob/main/images/TF_IDF_Logistic_regression.png)

It's possible to see acording to the confusion matrix to the baseline model, that the correct predictions are well-balanced among all three topics.

## RNN Model
From the below confusion matrix we can see that the RNN has well-balanced predictions, although the accuracy could be better.
![example predictions](https://github.com/djtom98/NLP_yahoo_questions/blob/main/images/rnnconfusion.jpg)

## Bert Model
We can see from the confusion matrix that the BERT model did fairly well among all three classes, as the accuracy is well-balanced:
![Bert Confusion Matrix](https://github.com/djtom98/NLP_yahoo_questions/blob/main/images/BERT_CM.png)

Below we provide a few test prompts, the probability of each class, as well as the class with the highest probability for the BERT model:
![example predictions](https://github.com/djtom98/NLP_yahoo_questions/blob/main/images/example_predictions.png)

# Discussion and Conclusion
Here we see BERT outperform RNN and logistic regression. The reason why BERT performs slightly better than logistic regression and RNN could be attributed to its ability to capture more nuanced features and contextual information from the text data. Since BERT is pre-trained on a large corpus of text data, it has a deeper understanding of the language structure and can capture more subtle relationships between words and phrases. 

### Error analysis
Due to computational constraints we only used a subset of the data. As a result, it could be that the BERT model performs better using more training data. To investigate this hypothesis, we sample 150,000 observations from the original dataset, take 70% as the training dataset and train the BERT model once again.


- We could train on all classes and see how it works.
- Yahoo! Answers is a website that's no longer used- so this model is limited in the sense that it has no real external application.
