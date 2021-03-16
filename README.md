# Taming JSON with Python

## Goal  
- Show validating JSON is easy and can provide value around data quality
- Steps : 
    - Read JSON formatted data
    - Pass it through a validation engine (JSONschema)
    - Output Valid data and Error data separately

## What is a JSON Schema?
- JSON Schema is a vocabulary that allows you to annotate and validate JSON documents.
- There are ~36 implementations across 17 languages 
    - Example uses JSONschema in python
- The schemas for complex JSON documents can be time consuming to make by hand.
    - There are online tools to build the schema, when given the JSON

## Schema Validation Basics
- Type : Does the JSON element have the correct type?
- Required : Not all elements have to be listed or present
    - Required elements that are missing will fail
- Properties, by Type :
    - pattern : regex match
    - enum : valid value list
    - length : min and max number of elements in the object/array  

## Format_Data
- Inputs :
    - JSON Data
    - JSON Schema
- Step 1 : Is the Data JSON?
- Step 2 : Does the data pass the validation tests?
- Outputs : 
    - Output Valid Data
    - Output Error Data, with details

## Why Validate JSON?
We don't always have control of upstream data quality, but are responsible for our own process flows.

# Columnar Data Validation with Great Expectations  
_Disclaimer : The validation package, Great Expectation, is designed to be used as part of a CI Pipeline. However, one off testing is possible._  

## Goal  
- Show how easy it can be to run quick validations 
- Steps : 
    - Read columnar data to Great Expectations, similar to Pandas or Spark
        - Format Examples : csv, tsv, Excel, SQL output, etc
    - Select a column and run a test

## Appendix
- JSON-Schema Spec : <https://json-schema.org/understanding-json-schema/> 
- JSONschema Python Implementation : <https://pypi.org/project/jsonschema/>
- Great Expectations : <https://greatexpectations.io/>  