import requests


def fetch_trivia_facts(count):
    response = requests.get(f'https://opentdb.com/api.php?amount={count}&type=boolean')
    if response.status_code == 200:
        results = response.json().get('results', [])
        facts = [item['question'] for item in results]
        return facts
    else:
        print(f"Failed to fetch trivia facts: {response.status_code} - {response.text}")
        return []
