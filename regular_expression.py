import requests
import re
import PyPDF2
from bs4 import BeautifulSoup  
def readWebsite (url):
    # This function reads html code of a website 
    # and returns a string after extracting all the text from the Html coed with teh hekp of BeautifulSoup
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    a=requests.get(url, headers=headers)
    html_doc = a.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    return soup.get_text()
    
def readResume(path):
    # This function reads a pdf file and returns all the text in the form of String
    a = PyPDF2.PdfReader('resume.pdf')
    return a.pages[0].extract_text()

print("Enter 0 to extract from a website, else enter 1 to extract from a pdf")
var = int(input())
if var == 0:
    print("Enter the url")
    url = input()
    text = readWebsite(url)
elif var == 1:
    print("Enter the name of pdf file")
    path = input()
    path += ".pdf"
    text = readResume(path)

matchesPhoneNumbers = re.findall(r'\+\d{2}[ -]?\d{3}[ -]?\d{7}|\+\d{2}[ -]?\d{2}[ -]?\d{4}[ -]?\d{4}|\+\d{2}[ -]?\d{5}[ -]?\d{5}', text);
matchesEmail = re.findall(r'[\w.\.-]+@[\w\.-]+', text)
matchesDate = re.findall(r'\d{2}[\/-]\d{2}[\/-]\d{4}', text)
print(matchesPhoneNumbers)
print(matchesEmail)
print(matchesDate)



