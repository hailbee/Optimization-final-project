import csv
import random
import pandas as pd

def condense_data(df):
    # Convert the list of dictionaries to a pandas DataFrame

    numeric_columns = [
        'Duration', 'Conversion_Rate', 'Acquisition_Cost', 'ROI', 'Clicks', 'Likes', 
        'Comments', 'Shares', 'Impressions', 'Reach', 'Engagement_Rate', 'Click_Rate', 
        'Impression_Rate', 'Avg_Freq_Ad', 'r_pc', 's_p'
    ]

    # Ensure all numeric columns are actually numeric, coerce errors to NaN for proper averaging
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # Group by 'Platform'/or/and 'Company', and calculate the mean for each group only for numeric columns
    grouped = df.groupby('Company', as_index=False)[numeric_columns].mean()

    condensed_data = grouped.to_dict(orient='records')


    return condensed_data

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
    # file_path = './merged_data.csv'
    # data = pd.read_csv(file_path)
    # new_data = condense_data(data) # average all the numeric columns with the same platform and company

    # file_path = './condensed_data.csv'
    # data = pd.read_csv(file_path)
    # new_data = condense_data(data) # average all the numeric columns with the same platform
    # df = pd.DataFrame(new_data)
    # df.to_csv('final_condensed.csv', index=False)

    # file_path = './condensed_platform_company.csv'
    # data = pd.read_csv(file_path)
    # new_data = condense_data(data) # average all the numeric columns with the same company
    # df = pd.DataFrame(new_data)
    # df.to_csv('condensed_companies.csv', index=False)


    ###### CREATE CLEAN CSV FILE ######
    # constant for all companies need for each platform, 
    # w_p: click_rate
    # i_p: impression_rate
    # f_p: average_impression_rate
    # c_p: conversion rate
    # s_p: cost per click 

    # platform_csv = './condensed_platforms.csv'
    # data = pd.read_csv(platform_csv)
    # clean_data = {}
    # for index, row in data.iterrows():
    #     platform = row['Platform']
    #     clean_data[platform] = {
    #         'w_p': row['Click_Rate'],
    #         'i_p': row['Impression_Rate'],
    #         'f_p': row['Avg_Freq_Ad'],
    #         'c_p': row['Conversion_Rate'],
    #         's_p': row['s_p']
    #     }
    
    # print(clean_data)
    # df = pd.DataFrame(clean_data)
    # df.to_csv('platform_variables.csv', index=False)

    # already have in other csv
    # impression rate per age group (a_ap*i_p)
    # R_a: total reach demanded for each age group

    # different for each company
    # r_c: revenue per conversion
    companies_csv = './condensed_companies.csv'
    data = pd.read_csv(companies_csv)
    clean_data = {}
    for index, row in data.iterrows():
        company = row['Company']
        clean_data[company] = {
            'r_c': row['r_pc']
        }
    df = pd.DataFrame(clean_data)
    df.to_csv('company_rps.csv', index=False)

    # other csv have for each company
    # R_a: total reach demanded for each age group
    # B: budget




    # print(f"CSV file created successfully at: {file_path}")
    