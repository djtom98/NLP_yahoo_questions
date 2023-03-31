# Classification of Yahoo Answers

### Introduction

### Data

[Yahoo! Answers](https://en.wikipedia.org/wiki/Yahoo!_Answers) was a forum where users could ask and answer questions that other users have posted. These posts go under ‘topics’, which naturally allows for a classification task- classifying these posts to the correct topic based on textual content. Huggingface provides a [large dataset](https://huggingface.co/datasets/yahoo_answers_topics) comprised of 2 million Yahoo! Answers posts, which includes Topic, Question Title, Question Content, and Best Answer. Within this dataset, there are ten balanced topics/classes, namely:

In order to be less constrained by computational power and allow for more exploration of the data and models, we select the first three topics. These topics are: Health, Science & Mathematics,  and Society & Culture. We also sample 100,000 rows from the dataset of 2 million.


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

### BERT
To implement BERT, we used a package called ktrain. One of the pre-trained models included in ktrain is BERT, which stands for Bidirectional Encoder Representations from Transformers. BERT is a type of deep neural network that's been pre-trained on a large corpus of text data, using a technique called masked language modeling. This involves randomly masking out words from a sentence and training the model to predict the masked words based on the surrounding context.

This network took the most time to train, yet in the end it yielded the best results- slightly above our baseline logistic regression model.

# Analysis

We provide a comparison of the models based on the average precision, recall, and accuracy for the three classes:
## Performance Comparison
|                      | Avg Precision | Avg Recall | Avg Accuracy |
|----------------------|---------------|------------|--------------|
| Baseline             |     .880      |    .880    |     .880     |
| RNN                  |               |            |              |
| Bert                 |     .896      |    .896    |     .896     |

## Baseline Model
Below we provide the probability of each class for the TF-IDF + Logistic Regression model:
![TF_IDF_Logistic_regression.png](https://github.com/djtom98/NLP_yahoo_questions/blob/main/images/TF_IDF_Logistic_regression.png)

It's possible to see acording to the confusion matrix to the baseline model, that the correct predictions are well-balanced among all three topics.

## Bert Model
Below we provide a few test prompts, the probability of each class, as well as the class with the highest probability for the BERT model:
![example predictions](https://github.com/djtom98/NLP_yahoo_questions/blob/main/images/example_predictions.png)

*A few examples with their predicted outputs for each of the three implementations
Error Analysis of the models: where did it learn well / bad ?
Comment the metrics: can you explain the metrics difference between implementations? Where do you stand regarding SOA/random classifiers?
Biases: Try to identify any type of bias in the models
Improve your BERT solution depending on error analysis, biases or other analysis you think is relevant*

We can see from the confusion matrix that the BERT model did fairly well among all three classes, as the accuracy is well-balanced:
![Bert Confusion Matrix](https://github.com/djtom98/NLP_yahoo_questions/blob/main/images/BERT_CM.png)

# Discussion and Conclusion
*Next steps: What are the main limitations of your models? What would be the next steps to improve it?*

- We could train on all classes and see how it works.
- Yahoo! Answers is a website that's no longer used- so this model is limited in the sense that it has no real external application.
