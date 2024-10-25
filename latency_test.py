import requests
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

URL = "http://myece444-p5.us-east-2.elasticbeanstalk.com/predict"
test_input = {
    "input": [
        "The day light saving time changes in November", 
        "Trump won the 2020 election",
        "The weather in Vancouver is rainy on October 31st, 2024",
        "The flushot is available for everyone in Ontario",
    ]
}
num_API_calls = 100

def latency_test(csv_file="latency_results.csv"):
    results = []
    for i in range(num_API_calls):
        result = []
        for text in test_input["input"]:
            start_time = time.time()
            response = requests.post(URL, json={"input": [text]})
            end_time = time.time()
            latency = end_time - start_time
            result.append(latency)
        results.append(result)
        print(f"Call {i + 1}: Latency = {result}")

    # Save the results to a CSV file
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Call Number", "Call 1", "Call 2", "Call 3", "Call 4"])
        for i, latency in enumerate(results):
            writer.writerow([i + 1, latency[0], latency[1], latency[2], latency[3]])

def generate_boxplot(csv_file="latency_results.csv"):
    df = pd.read_csv(csv_file)
    # latency_lists = [df[f'Call {i}'].tolist() for i in range(1, 5)]
    latency_lists = df[['Call 1', 'Call 2', 'Call 3', 'Call 4']].values.tolist()
    # Convert to milliseconds
    # print(latency_lists)
    plt.figure(figsize=(12, 6))
    plt.boxplot(latency_lists, patch_artist=True)
    plt.title("Latency of News Predictor")
    plt.xticks(ticks=[1], labels=['Latency'])
    plt.ylabel("Latency (s)")
    plt.show()
    plt.savefig("latency_boxplot.png")
    averate_latency = df.mean(axis=0)
    global_average_latency = sum([sum(latency) for latency in latency_lists]) / (num_API_calls * 4)
    print("Average latency for each call:", averate_latency)
    print("Average latency for each call:", global_average_latency)


if __name__ == "__main__":
    # latency_test()
    generate_boxplot()

