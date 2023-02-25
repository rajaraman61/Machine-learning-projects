from helper import data_processing
from pprint import pprint
import pandas as pd
def main():
    """
    It loads the data from the file 'data/chatbot/vehicle.yaml' and prints it
    """
    dataset_query = data_processing.load_data('data/chatbot/vehicle_query.yaml')
    dataset_book = data_processing.load_data('data/chatbot/vehicle_book.yaml')

    result_from_load = data_processing.process_data_from_yaml(dataset_query, dataset_book)
    data = {
     "utterances" : result_from_load[0],
     "intents": result_from_load[1]
    }
    
    
    dataset = pd.DataFrame(data)
    dataset.to_csv('data/chatbot/vehicle.csv', index=False)
    
    
# A Python script that will be executed by the Python interpreter.
if __name__=="__main__":
    main()