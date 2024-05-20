from typing import re

import requests
from bs4 import BeautifulSoup

print('Write a script to produce a list of every file under https://gentoo.osuosl.org/distfiles/')


def find_files_dirs(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    list_of_files_dirs = []

    for a in soup.find_all('a'):
        list_of_files_dirs.append(a['href'])
    return list_of_files_dirs

url = "https://gentoo.osuosl.org/distfiles"
# Display Files and Dirs in the Dir:
for file_dir in find_files_dirs(url):
    print(file_dir)


# URL on the Github where the csv files are stored
github_url = 'https://github.com/USERNAME/REPOSITORY/tree/master/FOLDER'  # change USERNAME, REPOSITORY and FOLDER with actual name

#result = requests.get(github_url)
#requests.get(url).text
soup2 = BeautifulSoup(requests.get(github_url).text, 'html.parser')
csvfiles = soup2.find_all(title=re.compile("\.csv$"))

filename = [ ]
for i in csvfiles:
        filename.append(i.extract().get_text())

print(filename)