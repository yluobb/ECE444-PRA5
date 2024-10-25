import requests

# URL = "http://myece444-p5.us-east-2.elasticbeanstalk.com/predict"
# test_input = {
#     "input": [
#         "The day light saving time changes in November", 
#         "Trump won the 2020 election",
#         "The weather in Vancouver is rainy on October 31st, 2024",
#         "The flushot is available for everyone in Ontario",
#     ]
# }
# response = requests.post(URL, json=test_input)
# print(f"Status Code: {response.status_code}")
# print(f"Response: {response.json()}")

def test_predictions(test_cases, URL):
    for i, text in enumerate(test_cases):
        response = requests.post(URL, json={"input": [text]})
        print(f"Test {i + 1}: Input = '{text}', Prediction = {response.text}")

if __name__ == "__main__":
    URL = "http://myece444-p5.us-east-2.elasticbeanstalk.com/predict"
    test_cases = [
        "The day light saving time changes in November", 
        "Trump won the 2020 election",
        "The weather in Vancouver is rainy on October 31st, 2024",
        "The flushot is available for everyone in Ontario",
    ]
    test_predictions(test_cases=test_cases, URL=URL)


