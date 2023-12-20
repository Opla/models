# Desc: Validates model files against the schema
import json
import sys
from jsonschema import validate
import os

def validate_model(model_file):
    print("Validating model file: {}".format(model_file))
    if not model_file.endswith('.json'):
        with open(model_file, 'r') as f:
            model = json.load(f)

        with open('./schema/v1/model.schema.json', 'r') as f:
            schema = json.load(f)

        validate(model, schema)

def validate_model_file(model_file):
    if os.path.isdir(model_file):
        for file in os.listdir(model_file):
            validate_model_file(os.path.join(model_file, file))
    else:
        try:
            validate_model(model_file)
            print("Model file is valid.")
        except Exception as e:
            print("Model file is invalid.")
            print(e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate.py <model_file>")
        sys.exit(1)

    model_file = sys.argv[1]
    validate_model_file(model_file)


