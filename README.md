# Classification of Yahoo Answers

### Introduction

### Data

[Yahoo! Answers](https://en.wikipedia.org/wiki/Yahoo!_Answers) was a forum where users could ask and answer questions that other users have posted. These posts go under ‘topics’, which naturally allows for a classification task- classifying these posts to the correct topic based on textual content. Huggingface provides a [large dataset](https://huggingface.co/datasets/yahoo_answers_topics) comprised of 2 million Yahoo! Answers posts, which includes Topic, Question Title, Question Content, and Best Answer. Within this dataset, there are ten balanced topics/classes, namely:

In order to be less constrained by computational power and allow for more exploration of the data and models, we select the first three topics. These topics are: Health, Science & Mathematics,  and Society & Culture. We also sample 100,000 rows from the dataset of 2 million.


### Preprocessing

# Models

### Baseline Model - Logistic Regression

A baseline model is a simple model that serves as a starting point for building more complex models. It provides a reference point for evaluating the performance of more sophisticated models.
In order to analize different starting points we defined two different baseline models.

#### Ruled based model

+ Gets as inputs a dictionnary for each topic with the fifty most common words
+ For each sentence find the dictionary with more coincidences and classify the text under that topic
+ Calculate precision, recall, f1-score and the confusion matrix for the model

#### TF-IDF + Logistic Regression

+ Create a bag of words with Count Vectorizer 
+ Use a TF-IDF transformer
+ Run a Logistic Regression

### RNN-LSTM

### BERT

# Analysis

*A few examples with their predicted outputs for each of the three implementations - maybe with lime or something?*

### Performance Comparison
|                      | Avg Precision | Avg Recall | Avg Accuracy |
|----------------------|---------------|------------|--------------|
| Baseline             |    0.88       |            |              |
| RNN                  |               |            |              |
| Bert                 |               |            |              |


*A few examples with their predicted outputs for each of the three implementations
Error Analysis of the models: where did it learn well / bad ?
Comment the metrics: can you explain the metrics difference between implementations? Where do you stand regarding SOA/random classifiers?
Biases: Try to identify any type of bias in the models
Improve your BERT solution depending on error analysis, biases or other analysis you think is relevant*

# Discussion and Conclusion
*Next steps: What are the main limitations of your models? What would be the next steps to improve it?*
