import csv
import os

def calculate_average_confidence(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        if len(rows) < 80:
            return 0

        confidence_values = []
        for key, value in rows[-2].items():
            if key.endswith('Confidence'):
                if value is not None and value != '':
                    try:
                        float_value = float(value)
                        if float_value == 0.0:
                            confidence_values.append(0.5)
                        else:
                            confidence_values.append(float_value)
                    except ValueError:
                        confidence_values.append(0.5)
                else:
                    confidence_values.append(0)  # Assuming 0 for missing values

        if not confidence_values:
            return 0
        
        average_confidence = sum(confidence_values) / len(confidence_values)
        return average_confidence

def process_folder(folder_path):
    results = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                csv_file = os.path.join(root, file)
                average_confidence = calculate_average_confidence(csv_file)
                results.append((csv_file, average_confidence))
    
    for result in results:
        print(f"{result[0]}: {result[1]}")

folder_path = r'C:\Users\anshi\code\kinectv1-skeleton-recorder\new-occlusion-tests\Akpandu'
process_folder(folder_path)
