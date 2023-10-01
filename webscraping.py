import os
import requests
from bs4 import BeautifulSoup
from docx import Document

# Define the base URL
base_url = "http://www.liiofindia.org/in/cases/cen/INSC/"

# Define the range of years and numbers
years_range = range(1950, 2024)
numbers_range = range(1, 21)

# Create a directory to store Word files
output_directory = "legal_notices"
os.makedirs(output_directory, exist_ok=True)

# Loop through the combinations of year and number
for year in years_range:
    for num in numbers_range:
        # Construct the full URL for the combination
        url = f"{base_url}{year}/{num}.html"
        print(url)

        try:
            # Send a GET request to the URL
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract the relevant data (you may need to inspect the website's HTML structure)
                legal_notice = soup.find('div', p_="ACT:").get_text()

                # Create a Word document for the combination and save the data
                doc = Document()
                doc.add_paragraph(legal_notice)
                output_filename = os.path.join(output_directory, f"Notice_{year}_{num}.docx")
                doc.save(output_filename)

                print(f"Saved data for Year: {year}, Number: {num}")

            else:
                print(f"Failed to retrieve data for Year: {year}, Number: {num}. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred for Year: {year}, Number: {num}: {e}")

