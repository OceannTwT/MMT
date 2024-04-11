import time

from openai import OpenAI

def predict(args, prompt):
    my_key = args.api_key
    print(len(prompt))
    max_length = 3800 - len(prompt)
    temperature = 0.3
    top_p = 1
    frequency_penalty = 0
    presence_penalty = 0
    client = OpenAI(api_key = my_key)
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct", # text-davinci-003 is deprecated
        prompt=prompt,
        max_tokens=max_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    return response.choices[0].text