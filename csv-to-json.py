import pandas as pd
import json

def csv_to_json(csv_file_path, json_file_path, chunk_size=10000):
    # Create an empty list to store chunks
    chunks = []

    # Iterate through CSV file in chunks
    for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
        # Process each chunk as needed
        # For simplicity, we're just converting each chunk to a list of dictionaries
        chunk_dict_list = chunk.to_dict(orient='records')
        chunks.append(chunk_dict_list)

    # Concatenate all chunks into a single list
    data = [record for chunk in chunks for record in chunk]

    # Write JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)

csv_file_path = 'input.csv'  # Replace with large CSV file path
json_file_path = 'output.json'  # Replace with desired JSON output file path

csv_to_json(csv_file_path, json_file_path)