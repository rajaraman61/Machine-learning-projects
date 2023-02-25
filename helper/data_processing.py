# import the libraries
import numpy as np
import pandas as pd
import yaml

def get_files(path):
    '''
        Get All records from the dataset
    '''
    return pd.read_csv(path);

def load_data(path):
    with open(path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if (data != None):
            return data
        
def process_data_from_yaml(dataset_query, dataset_book):

    entities_query = dataset_query['entity']
    utterances_query = dataset_query['utterances']
    
    entities_book = dataset_book['entity']
    utterances_book = dataset_book['utterances']
    
    intent_query = dataset_query['intent']
    intent_book = dataset_book['intent']
    
    intents = []    
    modified_utterances = []
    for entity in entities_query:
        for utterance in utterances_query:
            utterance = utterance.replace("[entity]", entity)
            modified_utterances.append(utterance)
            intents.append(intent_query)

            
    
    for entity in entities_book:
        for utterance in utterances_book:
            utterance = utterance.replace("[entity]", entity)
            modified_utterances.append(utterance)
            intents.append(intent_book)
            
    return modified_utterances, intents
        