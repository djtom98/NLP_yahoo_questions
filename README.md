# Classification of Yahoo Answers

### Introduction

### Data

[Yahoo! Answers](https://en.wikipedia.org/wiki/Yahoo!_Answers) was a forum where users could ask and answer questions that other users have posted. These posts go under ‘topics’, which naturally allows for a classification task- classifying these posts to the correct topic based on textual content. Huggingface provides a [large dataset](https://huggingface.co/datasets/yahoo_answers_topics) comprised of 2 million Yahoo! Answers posts, which includes Topic, Question Title, Question Content, and Best Answer. Within this dataset, there are ten balanced topics/classes, namely:

In order to be less constrained by computational power and allow for more exploration of the data and models, we select the first three topics. These topics are: Health, Science & Mathematics,  and Society & Culture. We also sample 100,000 rows from the dataset of 2 million.


### Preprocessing

# Models

### Baseline Model - Logistic Regression

### RNN-LSTM

### BERT
To implement BERT, we used a package called ktrain. One of the pre-trained models included in ktrain is BERT, which stands for Bidirectional Encoder Representations from Transformers. BERT is a type of deep neural network that's been pre-trained on a large corpus of text data, using a technique called masked language modeling. This involves randomly masking out words from a sentence and training the model to predict the masked words based on the surrounding context.

# Analysis

*A few examples with their predicted outputs for each of the three implementations - maybe with lime or something?*

### Performance Comparison
|                      | Avg Precision | Avg Recall | Avg Accuracy |
|----------------------|---------------|------------|--------------|
| Baseline             |               |            |              |
| RNN                  |               |            |              |
| Bert                 |     .896      |    .896    |     .896     |


*A few examples with their predicted outputs for each of the three implementations
Error Analysis of the models: where did it learn well / bad ?
Comment the metrics: can you explain the metrics difference between implementations? Where do you stand regarding SOA/random classifiers?
Biases: Try to identify any type of bias in the models
Improve your BERT solution depending on error analysis, biases or other analysis you think is relevant*

# Discussion and Conclusion
*Next steps: What are the main limitations of your models? What would be the next steps to improve it?*
