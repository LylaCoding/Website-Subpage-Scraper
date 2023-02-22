# Website-Subpage-Scraper

Window View Version:
I have  created an app version of the script that runs like a normal app would. if you would like to use this version you can, it is alot simpler to use. If you decide to use the app version disregard what is mentioned below

Description:
This is a Python script that allows you to scrape all the internal links on a webpage. The script prompts the user for a URL, and then sends a GET request to the URL to retrieve the HTML content. It then uses the BeautifulSoup module to parse the HTML and find all the links on the page. The script filters out external links and links that don't start with the base URL, and removes any duplicates. Finally, the script prompts the user for an output mode and either prints the list of links to the terminal or writes them to a file. If the required modules (requests and beautifulsoup4) are not already installed, the script will automatically install them for you.

Usage:
To use this script, you must have Python installed on your computer. To run the script, open a terminal and navigate to the directory where the script is saved. Then, type "python website-subpage-scraper.py" and hit enter. The script will prompt you for a URL to scrape (please note that you must include the http/https part of the url in order for the program to work), and then ask you whether you want to print the links to the terminal or save them to a file. The output will be printed to the terminal or saved to a file named "output.txt".

Disclaimer:
This tool should only be used on websites you have permision to use it on. This tool may not work on certain larger websites but may work on smaller sites like blogs for example. I accept no responsibilty for any trouble you may encure from using this tool.

<!DOCTYPE html>
<html>
  <head>
    <title>Website Subpage Scraper</title>
  </head>
  <body>
    <h1>Website Subpage Scraper</h1>
    <h2>Window View Version</h2>
    <p>A simplified app version of the script is also available for users who prefer a more user-friendly experience.</p>
    <h2>Description</h2>
    <p>Website Subpage Scraper is a Python script designed to scrape all internal links on a webpage. The script prompts the user for a URL, sends a GET request to retrieve the HTML content, and then parses the HTML using the BeautifulSoup module. The script filters out external links and duplicates, and prompts the user to select an output mode, which can either print the list of links to the terminal or write them to a file. In case the required modules (requests and beautifulsoup4) are not already installed, the script will install them automatically.</p>
    <h2>Usage</h2>
    <p>To run this script, you must have Python installed on your computer. Open a terminal and navigate to the directory where the script is saved. Then, enter the command "python website-subpage-scraper.py". The script will prompt you for a URL to scrape (make sure to include the http/https part of the URL), and then ask whether you want to print the links to the terminal or save them to a file. The output will be displayed on the terminal or saved to a file named "output.txt".</p>
    <h2>Disclaimer</h2>
    <p>Please note that this tool should only be used on websites that you have permission to access. While it may not work on certain larger websites, it should work well on smaller sites such as blogs. The creator of this tool accepts no responsibility for any trouble you may encounter while using it.</p>
  </body>
</html>
