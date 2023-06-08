import requests
from nanonets import NANONETSOCR
import json

model = NANONETSOCR()

model.set_token('a837f17b-f0cc-11ed-98ed-c2317ca873a2')

string1 = model.convert_to_string('test.pdf')

url = "https://api.openai.com/v1/chat/completions"

custom_prompt = f"""
This is my resume string data
/--------------------------------------------------
{string1}
/--------------------------------------------------
Please response with seperated JSON data by keywords (i.e. summary, skills, education, experiences, hobeys, etc).
Keywords are property and content is the value.
"""
# Keywords are property and content is the value.
# Please give me Markdown format.
# print(custom_prompt)

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{
        "role": "user",
        "content": custom_prompt
    }],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    responseData = response.json()
    # data = json.loads(responseData)

    del responseData['id']
    del responseData['object']
    del responseData['created']
    del responseData['usage']
    del responseData['model']

    json_data = json.dumps(responseData)

    print(json_data)

else:
    print("Error:", response.text)