import logging
import json
import csv 

logging.basicConfig(
    filename="parser.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def parse_json(file_path):
    logging.info(f"Attempting to parse json file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logging.info(f"Successfully parsed JSON file: {file_path}")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON format in file: {file_path}")
    except Exception as e:
        logging.Exception("Unexpected error occurred while parsing JSON")               

def parse_csv(file_path):
    logging.info(f"Attempting to parse csv file: {file_path}")
    try:
        with  open(file_path, "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            logging.info(f"Successfully parsed CSV file: {file_path}")
            return data
    except FileNotFoundError:
        logging.error(f"File not Found: {file_path}")
    except csv.error:
        logging.error(f"Invalid CSV format in file: {file_path}") 
    except Exception as e:
        logging.Exception("Unexpected error occured while parsing CSV")               

if __name__ == "__main__":
    json_data = parse_json('data.json')
    csv_data =  parse_csv('data.csv')

    if json_data:
        logging.debug(f"First JSON record: {json_data[0] if isinstance(json_data, list) else json_data}")

    if csv_data:
        logging.debug(f"First CSV record: {csv_data[0]}")    