import requests
import json


def fetch_facts(number_of_facts=5):
    facts = []
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    for _ in range(number_of_facts):
        response = requests.get(url)
        if response.status_code == 200:
            facts.append(response.json().get("text"))
        else:
            print("Failed to fetch a fact")

    return facts


def fetch_fun_facts(n=5):
    url = 'https://thefact.space/random'
    facts = []

    for _ in range(n):
        response = requests.get(url)
        if response.status_code == 200:
            fact_json = response.text.strip()
            try:
                # Parse the JSON object
                fact = json.loads(fact_json)
                # Extract and print the text part of the fact
                fact_text = fact.get("text", "No text available")
                print(fact_text)
                facts.append(fact_text)
            except json.JSONDecodeError:
                print("Failed to parse JSON response")
        else:
            print(f"Failed to fetch fact: {response.status_code}")
    return facts
