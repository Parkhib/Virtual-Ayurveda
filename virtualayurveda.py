import wikipediaapi
import requests
from bs4 import BeautifulSoup

class AyurvedaAssistant:
    def __init__(self):
        self.local_symptom_to_medicine = {
            "cough": "Honey and black pepper",
            "common cold": "Honey and Lemon",
            "sore throat": "Gargling with warm salt water",
            "runny nose": "Steam inhalation",
            "sneezing": "Ginger tea",
            "fever": "Tulsi and honey tea",
            "chills": "Warm milk with turmeric",
            "muscle pain": "Massage with sesame oil",
            "fatigue": "Ashwagandha",
            "itchy eyes": "Cucumber slices",
            "loss of taste or smell": "Ginger and honey"
        }
        self.api_url = "https://en.wikipedia.org/w/api.php"
        self.user_agent = "AyurvedaAssistant/1.0 (https://yourwebsite.com; your-email@example.com)"
        self.headers = {
            'User-Agent': self.user_agent
        }
        self.wiki = wikipediaapi.Wikipedia('en', headers=self.headers)

    def get_local_solution(self, symptom):
        return self.local_symptom_to_medicine.get(symptom, None)

    def get_api_solution(self, symptom):
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': symptom,
            'format': 'json'
        }
        try:
            response = requests.get(self.api_url, headers=self.headers, params=params)
            response.raise_for_status()  # Check if the request was successful
            data = response.json()
            if 'query' in data and 'search' in data['query']:
                search_results = data['query']['search']
                if search_results:
                    title = search_results[0]['title']
                    page = self.wiki.page(title)
                    return page.summary[:500]  # Return a summary of the page content
                else:
                    return "No Ayurvedic solution found for this symptom. Please consult an Ayurvedic practitioner."
            else:
                return "No Ayurvedic solution found for this symptom. Please consult an Ayurvedic practitioner."
        except requests.exceptions.RequestException as e:
            return f"An error occurred while fetching data from the API: {e}"

    def get_ayurvedic_solution(self, symptom):
        # First, try to get the solution from local data
        local_solution = self.get_local_solution(symptom)
        if local_solution:
            return local_solution

        # If not found locally, try to get the solution from the API
        return self.get_api_solution(symptom)

    def get_detailed_usage(self, symptom):
        url = f"https://en.wikipedia.org/wiki/{symptom.replace(' ', '_')}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Check if the request was successful
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the first two paragraphs of the page content
            paragraphs = soup.find_all('p')
            usage_info = []
            for paragraph in paragraphs:
                if paragraph.text.strip():
                    usage_info.append(paragraph.text.strip())
                    if len(usage_info) == 2:  # Get only the first two non-empty paragraphs
                        break

            return "\n\n".join(usage_info)
        
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

    def run(self):
        print("Welcome to Virtual Ayurveda!")
        symptom = input("Please enter your symptom: ").lower().strip()

        if not symptom:
            print("Invalid input. Please enter a valid symptom.")
            return

        solution = self.get_ayurvedic_solution(symptom)
        print(f"Recommended Ayurvedic solution: {solution}")

        detailed_usage = self.get_detailed_usage(symptom)
        print(f"Brief explanation of your sympton:\n{detailed_usage}")
        
        print("Thank you for consulting and spending the time with us.")
        print("Take care of your health and keep smiling!")

if __name__ == "__main__":
    assistant = AyurvedaAssistant()
    assistant.run()


