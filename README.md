# Custom_ner

1. Install the requirements by running following command in cmd <br>
   pip install -r path/to/requirements.txt
   
2. Problem statement: To extract living beings, places, objects from the given text.<br>
   
3. <b>Approach</b>: Pretrained NER (Name entity recognition) pipelines are already available in frameworks like spacy,nltk which are trained on massive data of a particular 
  language and different entities like Person, organization etc. In our case we got entites which have different definitions and interpretations. In short we got a Custom 
  entity Ner problem.<br>
  My approach is to manually annotate the data with custom entities and train it using spaCy pipeline.
  (Please go through custom_ner.ipynb for the whole process.)
    * We got the dataset (data.csv) in csv format with 5 sentences as column. Therefore first concatenated it in one column ('paragrapgh') and converting it into text file
      (data.txt).
    * For manually annotating I used this [web app](https://manivannanmurugavel.github.io/annotating-tool/spacy-ner-annotator/) where it takes a text file(data.txt) and 
      after annotating it returns a json file(doc.json).
    * As spaCy takes input as list of tuple, transformed docs.json (to train_data) and stored in doc.pickle.
    * In spaCy we can create a blank 'ner' pipeline for english language and train model on it on our data.
    * spaCy’s tagger, parser, text categorizer and many other components(ner also) are powered by statistical models. Every “decision” these components make – for example, 
    whether a word is a named entity – is a prediction based on the model’s current weight values. The weight values are estimated based on examples the model has seen during 
    training.
    * Training is an iterative process in which the model’s predictions are compared against the reference annotations in order to estimate the gradient of the loss. 
    The gradient of the loss is then used to calculate the gradient of the weights through backpropagation.
    * After Training storing the pipeline in 'model' folder.
    
4. Usage: python ner.py path/to/input/text/file path/to/output/json/file <br>
          For e.g. python ner.py example_input.txt output.json
