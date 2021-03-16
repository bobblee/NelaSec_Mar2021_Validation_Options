import json
from pathlib import Path
import os
import pandas as pd
from jsonschema import Draft7Validator

class FormatData():
    def __init__(self, json_file_name:str, schema_file_name:str):
        self.json_file_name = json_file_name
        self.schema_file_name = schema_file_name

        self.json_object_list = []
        self.json_object = {}
        self.good_list = []
        self.good_step_list = []
        self.good_ingre_list = []
        self.error_list = []

    def is_json(self, raw_json_text:str):
        json_file_wrapper = open(raw_json_text,'r')
        json_file_text = json_file_wrapper.read()
        json_file_wrapper.close()

        try:
            if type(json.loads(json_file_text)) == list:
                self.json_object_list = json.loads(json_file_text)
            elif type(json.loads(json_file_text)) == dict:
                self.json_object = json.loads(json_file_text)
            else:
                self.error_list.append( [
                                        'JSON_TEXT_ERROR',
                                        'String is not list or dict',
                                        'JSON Data',
                                        #raw_json_instance,
                                    ] )
                return False    
        except:
            self.error_list.append( [
                                        'JSON_PARSE_ERROR',
                                        'String is not valid json',
                                        'JSON Data',
                                        #raw_json_instance,
                                    ] )
            return False
        return True

    def is_schema(self, schema:str):
        json_schema_wrapper = open(schema,'r')
        json_schema_text = json_schema_wrapper.read()
        json_schema_wrapper.close()

        try:
            self.schema_dict = json.loads(json_schema_text)
        except:
            self.error_list.append( [
                                        'JSON_PARSE_ERROR',
                                        'String is not valid json',
                                        'JSON Schema',
                                        #raw_json_instance,
                                    ] )
            return False
        
        self.validator = Draft7Validator(self.schema_dict)
        return True

    def schema_validation(self):
        
        errors = sorted( self.validator.iter_errors( self.json_object ), key=lambda e: e.path )
        if len(errors) > 0:
            for error in errors:
                self.error_list.append( [
                                'JSON_SCHEMA_ERROR',
                                error.context,
                                error.absolute_path,
                                self.json_object,
                            ] )
        else:
            self.good_list.append(self.json_object)

    def organizer(self) :

        #Validate the Schema
        self.is_schema(self.schema_file_name)
        self.is_json(self.json_file_name)

        if len(self.json_object_list) > 0:
            for x in self.json_object_list:
                self.json_object = x
                self.schema_validation()

        elif len(self.json_object_list) == 0:
            self.schema_validation()
        else:
            print("Nothing to read")
        
        print(f"Print Errors : count ({str(len(self.error_list))})")
        print(f"Print Good : count ({str(len(self.good_list))})")

#        for x in self.error_list:
#            print(x)
        df_error = pd.DataFrame(self.error_list)        
        df_error.to_csv('outputData/error.csv')

        df_good = pd.DataFrame(self.good_list)
        df_good.to_csv('outputData/good.csv')

        df_good_steps = pd.json_normalize(self.good_list, 'steps',['name'])
        df_good_steps.to_csv('outputData/good_steps.csv')

        df_good_ingre = pd.json_normalize(self.good_list, 'ingredients',['name']) 
        df_good_ingre.to_csv('outputData/good_ingre.csv')

if __name__ == '__main__':

    # Ensure correct Working Directory
    print(os.getcwd())
    path = Path('NewThoughts')
    os.chdir(path)
    print(os.getcwd())

    json_file = 'inputData/recipe_example_list.json'
    #json_file = 'inputData/recipe_example_dict.json'
    json_schema = 'inputData/recipe_example_schema.json'

    FormatData( json_file , json_schema ).organizer()
