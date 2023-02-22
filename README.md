# Website-Subpage-Scraper

Description:
This is a Python script that allows you to scrape all the internal links on a webpage. The script prompts the user for a URL, and then sends a GET request to the URL to retrieve the HTML content. It then uses the BeautifulSoup module to parse the HTML and find all the links on the page. The script filters out external links and links that don't start with the base URL, and removes any duplicates. Finally, the script prompts the user for an output mode and either prints the list of links to the terminal or writes them to a file. If the required modules (requests and beautifulsoup4) are not already installed, the script will automatically install them for you.

Usage:
To use this script, you must have Python installed on your computer. To run the script, open a terminal and navigate to the directory where the script is saved. Then, type "python website-subpage-scraper.py" and hit enter. The script will prompt you for a URL to scrape (please note that you must include the http/https part of the url in order for the program to work), and then ask you whether you want to print the links to the terminal or save them to a file. The output will be printed to the terminal or saved to a file named "output.txt".
