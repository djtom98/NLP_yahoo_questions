## this 

import ktrain
from ktrain import text

# upload the preprocessed data
# cleaned_data = # read csv from processed data
cleaned_data = cleaned_data.sample(frac=0.13).reset_index(drop=True)
cleaned_data = cleaned_data[['class', 'text']]
cleaned_data.head(2) 

# 2. Create train, validation & preprocessing datasets using texts_from_df in ktrain
(X_train, y_train), (X_test, y_test), preproc = text.texts_from_df(train_df=cleaned_data,
                                                                  text_column='text',
                                                                  label_columns='class',
                                                                  maxlen=64,
                                                                  preprocess_mode='bert')       
     

# 3. Create and Train the BERT Model
model = text.text_classifier(name='bert',
                             train_data=(X_train, y_train),
                             preproc=preproc) 

#@ Setting up learner
learner = ktrain.get_learner(model=model,
                             train_data=(X_train, y_train),
                             val_data=(X_test, y_test),
                             batch_size=64)

#@ Fitting model using one-cycle poliy, lr=2e-5 from research paper
learner.fit_onecycle(lr=2e-5, epochs=3); 
     
#@ Get predictor using preproc dataset
predictor = ktrain.get_predictor(learner.model, preproc)   
     
classes = predictor.get_classes()  
classes
