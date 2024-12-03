import csv
import random

def read_csv(file_path):
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Read the CSV as dictionaries
            for row in reader:
                data.append(row)
        return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []
    
if __name__ == '__main__':
    file_path = './merged_data.csv'
    data = read_csv(file_path)
    companies = set()
    # age_groups = set() # {'45-60', '18-24', '35-44', '25-34'}
    for row in data:
        companies.add(row['Company'])
        # age_groups.add(row['Age_Range'])

    file_path = "./budgets_demand.csv"
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
            
        # If headers are provided, write them as the first row
        
        csv_writer.writerow(['Company', 'Budget', '18-24', '25-34','35-44','45-60'])
        # company_numbers = {company: random.randint(500, 2000) for company in companies}

        # Write the data
        for company in companies:
            csv_writer.writerow([company, random.randint(500, 3000),
                                random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000)])
            
    print(f"CSV file created successfully at: {file_path}")
    