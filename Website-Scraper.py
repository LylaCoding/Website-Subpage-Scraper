import subprocess
import sys

# Check if requests and beautifulsoup4 modules are installed
reqs = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
installed_packages = [r.decode().split("==")[0] for r in reqs.split()]
if "requests" not in installed_packages or "beautifulsoup4" not in installed_packages:
    # Install the missing modules
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4"])

# Now you can import the modules and use them in your script
import requests
from bs4 import BeautifulSoup


# Prompt the user for the website URL to scrape
url = input("Enter the website URL to scrape: ")

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all links on the page
links = soup.find_all("a")

# Extract the href attribute of each link
hrefs = [link.get("href") for link in links]

# Filter out external links and links that don't start with the base URL
subpages = [href for href in hrefs if href and not href.startswith("http") and (href.startswith("/") or href == "/")]

# Remove duplicates and sort the subpages
unique_subpages = sorted(list(set(subpages)))

# Add the base URL to relative links (i.e. links that start with "/")
full_links = [url + subpage if subpage.startswith("/") else subpage for subpage in unique_subpages]

# Prompt the user for the output mode
output_mode = input("Enter the output mode (terminal or file): ")

# Print the list of full links to the terminal or write them to a file
if output_mode == "file":
    with open("output.txt", "w") as f:
        for link in full_links:
            f.write(link + "\n")
    print("Output written to output.txt")
else:
    for link in full_links:
        print(link)
