import tkinter as tk
from tkinter import ttk
import subprocess
import sys

# Check if requests and beautifulsoup4 modules are installed
reqs = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
installed_packages = [r.decode().split("==")[0] for r in reqs.split()]
if "requests" not in installed_packages or "beautifulsoup4" not in installed_packages:
    # Install the missing modules
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4"], stdout=subprocess.DEVNULL)

from bs4 import BeautifulSoup
import requests

def get_website_subpages():
    website_url = website_url_entry.get()
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")
    hrefs = [link.get("href") for link in links]
    subpages = [href for href in hrefs if href and not href.startswith("http") and (href.startswith("/") or href == "/")]
    unique_subpages = sorted(list(set(subpages)))
    full_links = [website_url + subpage if subpage.startswith("/") else subpage for subpage in unique_subpages]
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "\n".join(full_links))

# create the GUI
root = tk.Tk()
root.geometry("500x300")
root.title("Website Subpage Viewer")

# create the widgets
style = ttk.Style()
style.configure("TButton", font=("Arial", 14))
style.configure("TLabel", font=("Arial", 14))
style.configure("TEntry", font=("Arial", 14))

website_url_label = ttk.Label(root, text="Enter website URL:")
website_url_entry = ttk.Entry(root)
get_subpages_button = ttk.Button(root, text="Get Subpages", command=get_website_subpages)
output_label = ttk.Label(root, text="Website Subpages:")
output_text = tk.Text(root, font=("Arial", 14), wrap="word")

# arrange the widgets
website_url_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
website_url_entry.grid(row=0, column=1, padx=10, pady=10)
get_subpages_button.grid(row=1, column=1, padx=10, pady=10)
output_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# configure grid weights
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

# start the event loop
root.mainloop()
