import tkinter as tk
import requests
import re
import webbrowser

def shorten_url(event=None):
    regex = r"^https?://"
    url = url_entry.get()

    if not re.match(regex, url):
        url = "https://" + url

    headers = {
        'Authorization': 'Bearer 4470665be0fdd608a6b7ed63f55cf8c893724e34',
        'Content-Type': 'application/json',
    }

    data = '{ "long_url": ' + '"' + url + '"' + ', "domain": "bit.ly" }'

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

    if response.status_code == 200:
        shortened_url_label.config(text="Shortened URL : - ")
        shortened_url = tk.Label(root, text=response.json()['link'], fg="#1a73e8", cursor="hand2", font=("Google Sans", 12))
        shortened_url.pack()
        shortened_url.bind("<Button-1>", lambda e: webbrowser.open_new(response.json()['link']))

root = tk.Tk()
root.title("URL Shortener")
root.configure(bg="#f1f3f4")

url_label = tk.Label(root, text="Enter a Url to be shorten : - ", font=("Google Sans", 12), bg="#f1f3f4")
url_label.pack()

url_entry = tk.Entry(root, font=("Google Sans", 12))
url_entry.pack()
url_entry.bind("<Return>", shorten_url)

shorten_button = tk.Button(root, text="Shorten", command=shorten_url, bg="#1a73e8", fg="white", font=("Google Sans", 12))
shorten_button.pack(pady=10)

shortened_url_label = tk.Label(root, font=("Google Sans", 12), bg="#f1f3f4")
shortened_url_label.pack()

root.mainloop()
