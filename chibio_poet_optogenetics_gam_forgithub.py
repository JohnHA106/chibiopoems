from numpy import mean
import openai
import datetime
import pandas as pd
import statistics


data = pd.read_csv(r"C:\Users\jhall\Documents\chi24\opto_gam.csv")
print('got data')

# Access specific columns
growth_rate = data['growth_rate']

# Calculate average growth rate between two most recent timepoints
#growth_rate_now = data['growth_rate'].iloc[-1]
#prev_growth_rate = data['growth_rate'].iloc[-2]

points = range(0, len(data))
print('got points')

now = datetime.datetime.now()
current_date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

file_name = f"{current_date_time}_optoprompts_poem.txt"

with open(file_name, 'w') as file:
    file.write("poem")

with open(file_name, 'r') as file:
    poem = file.readlines()

#lastline = poem[-1]
#print(lastline)

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average




openai.organization = "YOUR_ORG_HERE" 
openai.api_key = "YOUR_KEY_HERE"

for point in points:
    if point == 1 :
    
        newprompt = "Please write the title of a poem of bacteria"
        print(newprompt)
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt = newprompt,
            max_tokens=100,
            temperature = 0.9
            )
        print(response)
        title = str(response.choices[0].text)
        
    if point%10 == 0:

        growth_rate_now = data['fp_gam'].iloc[point]
        prev_growth_rate = calculate_average([data['fp_gam'].iloc[point-10],
                                     data['fp_gam'].iloc[point-9],
                                     data['fp_gam'].iloc[point-8],
                                     data['fp_gam'].iloc[point-7],
                                     data['fp_gam'].iloc[point-6],
                                     data['fp_gam'].iloc[point-5],
                                     data['fp_gam'].iloc[point-4],
                                     data['fp_gam'].iloc[point-3],
                                     data['fp_gam'].iloc[point-2],
                                     data['fp_gam'].iloc[point-1]] 
        )
        lastline = poem[-1]
        print(lastline)
        inspo = "inspo goes here"
        print(inspo)

        if growth_rate_now > prev_growth_rate:
            inspo = " using language that conveys a sense that you are building a powerful glowing protein in response to instructions given to you"
            
            print(inspo)
        elif growth_rate_now == prev_growth_rate :
            inspo = " using language that conveys a sense that your glow is being maintained, and you are feeling bored, things are being held steadily and stabily for you"
            print(inspo)
        elif growth_rate_now < prev_growth_rate:
            inspo = " using language that conveys a sense that something glowing inside you is dwindling, you are eating this glowing material and are becoming less bright"
            print(inspo)

        newprompt = "please write a rhyming couplet that would follow this previous line of a poem written from the point of view ofr bacteria: " + lastline +  inspo
        print(newprompt)
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt = newprompt,
            max_tokens=100,
            temperature = 0.9
            )
        print(response)

    print(response.choices[0].text)
    newline = response.choices[0].text

    with open(file_name, 'a') as f:
        f.write(newline + "\n")

import re

def sanitize_filename(filename):
    # Remove invalid characters from the filename
    sanitized_filename = re.sub(r'[^\w\s.-]', '', filename)
    return sanitized_filename
print(sanitize_filename(file_name))

def remove_duplicates(filename, output_title):
    # Read the contents of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove duplicate lines while preserving the order
    unique_lines = []
    seen_lines = set()

    for line in lines:
        if line not in seen_lines:
            unique_lines.append(line)
            seen_lines.add(line)
    
    sanitized_title = sanitize_filename(output_title)

    # Create the output file with the specified title
    output_filename = f"{current_date_time}_poem.txt"
    with open(output_filename, 'w') as file:
        file.writelines(unique_lines)

    print("Duplicate lines have been removed. Output file:", output_filename)



filename = file_name
output_title = title

remove_duplicates(file_name, output_title)

    