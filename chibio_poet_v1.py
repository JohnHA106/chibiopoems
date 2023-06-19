import openai
import datetime
import pandas as pd

data = pd.read_csv(r'C:\Users\jhall\OneDrive - Nexus365\Data\ChiBioTalks\data_small.csv')
print('got data')

# Access specific columns
growth_rate = data['growth_rate']

# Calculate average growth rate between two most recent timepoints
growth_rate_now = data['growth_rate'].iloc[-1]
prev_growth_rate = data['growth_rate'].iloc[-2]

points = range(0, len(data))
print('got points')

now = datetime.datetime.now()
current_date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

file_name = f"{current_date_time}_poem.txt"

with open(file_name, 'w') as file:
    file.write("I am a culture of bacteria and I feel")

with open(file_name, 'r') as file:
    poem = file.readlines()

#lastline = poem[-1]
#print(lastline)


openai.organization = "org-gaHs3EuFQhEvTmJToEIg1Ux2"
openai.api_key = "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"

for point in points:
    growth_rate_now = data['growth_rate'].iloc[point]
    prev_growth_rate = data['growth_rate'].iloc[point-1]
    lastline = poem[-1]
    print(lastline)
    inspo = "inpo goes here"
    print(inspo)

    if growth_rate_now < prev_growth_rate:
        inspo = "using language that conveys a sense of desperation and hunger"
        print(inspo)
    elif growth_rate_now == prev_growth_rate :
        inspo = "using language that conveys a sense of boredom"
        print(inspo)
    elif growth_rate_now > prev_growth_rate:
        inspo = "using language that conveys a sense of speed, pace and power"
        print(inspo)

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt = "please write the next line of this poem about bacteria: " + lastline + inspo,
        max_tokens=100,
        temperature = 0.9
        )
    print(response)

    print(response.choices[0].text)
    newline = response.choices[0].text

    with open(file_name, 'a') as f:
        f.write(newline + "\n")

    