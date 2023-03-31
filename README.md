# Classification of Yahoo Answers

### Introduction

The goal of this project is to classify [Yahoo! Answers](https://en.wikipedia.org/wiki/Yahoo!_Answers) posts into their respective topics. We use a [dataset](https://huggingface.co/datasets/yahoo_answers_topics) provided by Huggingface, which includes 2 million Yahoo! Answers posts categorized into ten topics. We select three topics - Health, Science & Mathematics, and Society & Culture - and sample 100,000 posts from the dataset for training and testing.

We apply several models to the task of classification, including rule-based models, traditional machine learning models, and deep learning models. We evaluate the performance of each model using metrics such as precision, recall, and accuracy.

### How to run this code?

The summary.ipynb notebook contains an overview of the models used. This comes from combining the notebooks in the src folder, namely data_preprocessing.ipynb, baseline_models.ipynb RNN.ipynb, and BERT.ipynb. Please note that you may need to change the path(s) to the 'yahoo_train.csv' file after writing the preprocessed data to a csv, depending on your specific directory.

# Data

The Yahoo! Answers dataset includes ten balanced topics/classes. We select the first three topics for our classification task, as described in the Introduction section. In order to be less constrained by computational power and allow for more exploration of the data and models, we select the first three topics. These topics are: Health, Science & Mathematics,  and Society & Culture. We also sample 100,000 rows from the dataset of 2 million. We split this sample of 100,000 observations into 70,000 training observations and 30,000 test observations.

# Preprocessing

We preprocess the data by performing the following operations:
+ Replace the topic number with its name to have a general understanding about the data
+ Remove the punctuation and stopwords
+ Remove the special characters (html tags) e.g '<br />' , '\\n' with regex
+ Optional:stemming,lemmatization
+ Merge title, question and answer into one column

We also provide exploratory data analysis (EDA) by plotting histograms of topic distribution, exploring NaN values in the dataset, and generating word clouds of the most frequent words in the dataset and by topic.

# Models

### Baseline Model 

A baseline model is a simple model that serves as a starting point for building more complex models. It provides a reference point for evaluating the performance of more sophisticated models.
In order to analyze different starting points we defined three different baseline models:

#### Rule-based Model

The rule-based model is a simple model that uses a dictionary for each topic with the fifty most common words. For each sentence, the model finds the dictionary with the most coincidences and classifies the text under that topic. We evaluate the model's performance using precision, recall, f1-score, and the confusion matrix.

#### TF-IDF + Logistic Regression

The TF-IDF + Logistic Regression model creates a bag of words with Count Vectorizer, applies a TF-IDF transformer, and then runs a Logistic Regression to classify the data. We evaluate the model's performance using precision, recall, and accuracy.

#### Decision Tree Classifier

The Decision Tree Classifier model applies a decision tree to classify the data. We evaluate the model's performance using precision, recall, and accuracy.

### RNN-LSTM

To implement RNN, we used the Keras package to create a neural network, by using LSTM layers which are part of the implementation. Embedding layer using Glove is also added to the model to improve the performance. Initially our performance with this was poor, so we added dropout layers, which seems to reduce overfitting, and we got a better performance as a result. 

### BERT
To implement BERT, we used a package called ktrain. One of the pre-trained models included in ktrain is BERT, which stands for Bidirectional Encoder Representations from Transformers. BERT is a type of deep neural network that's been pre-trained on a large corpus of text data, using a technique called masked language modeling. This involves randomly masking out words from a sentence and training the model to predict the masked words based on the surrounding context.

This network took the most time to train, yet in the end it yielded the best results- slightly above our baseline logistic regression model.

### Evaluation Metrics

We evaluate each model's performance using precision, recall, and accuracy. Precision measures the percentage of true positives among all positive predictions, recall measures the percentage of true positives among all actual positive instances, and accuracy measures the percentage of correct predictions overall.

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

This suggests that the model is unbiased, as it doesn't perform particularly bad on any of the classes.

Below we provide a few test prompts, the probability of each class, as well as the class with the highest probability for the BERT model:
![example predictions](https://github.com/djtom98/NLP_yahoo_questions/blob/main/images/example_predictions.png)

# Discussion and Conclusion
Here we see BERT outperform RNN and logistic regression. The reason why BERT performs slightly better than logistic regression and RNN could be attributed to its ability to capture more nuanced features and contextual information from the text data. Since BERT is pre-trained on a large corpus of text data, it has a deeper understanding of the language structure and can capture more subtle relationships between words and phrases. 

### Error analysis
Due to computational constraints we only used a subset of the data. As a result, it could be that the BERT model performs better using more training data. To investigate this hypothesis, we sample 150,000 observations from the original dataset, take 70% as the training dataset and train the BERT model once again.

### Limitations and next steps
Because Yahoo! Answers is a website that's no longer used, this model is limited in the sense that it has no real external application.

The next steps we could try would be to train on all ten classes and see how each of the models perform.

