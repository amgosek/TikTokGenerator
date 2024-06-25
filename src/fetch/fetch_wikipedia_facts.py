import requests


def fetch_wikipedia_facts(subject, number_of_facts=5):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{subject}"
    response = requests.get(url)
    facts = []

    if response.status_code == 200:
        page = response.json()
        extract = page.get('extract', '')

        # Split the extract into sentences and take the required number of facts
        sentences = extract.split('. ')
        for i in range(min(number_of_facts, len(sentences))):
            facts.append(sentences[i])

    return facts
