from lxml import html
import time
import requests
from tkinter import*
import random
import re


stud_ID=0
books_read= ""
authors_read = ""
recc_auth = ""
new_rec_auth = ""
new_str = ""
random.seed(time.clock())

def get_info(book_author):
    url = 'https://www.google.co.in/search?q='+book_author+'+similar+authors'
    i = random.randint(1,7);
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6'}
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)
    recc_auth = [tree.xpath('///*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[%d]/a/div[2]/text()' %i)]
    print(recc_auth[0][0])
    new_rec_auth = recc_auth[0][0]
    get_books_rec(new_rec_auth)
    Label(master, text="Recommended Author: %s"%recc_auth).grid(row=2)

def get_books_rec(authy):

	a_string = authy
	new_str = replace(a_string)
	url = 'https://isbndb.com/search/books/'+new_str
	i = random.randint(1,7);
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6'}
	page = requests.get(url, headers=headers)
	tree = html.fromstring(page.content)
	recc_auth_books = [tree.xpath('//*[@id="block-multipurpose-business-theme-content"]/div[2]/div[1]/div[2]/h2/a/text()')]
	print(recc_auth_books[0][0])

def replace(s):
    str = ""
    for x in s:
        if x == " ":
            str += "%20"
        else:
            str += x
    return str


master = Tk()

Label(master, text="Student ID").grid(row=0)
Label(master, text="Authors").grid(row=1)
Label(master, text="").grid(row=2)
var_book = StringVar()
def getlol():
	stud_ID = (e1.get())
	authors_read = (e2.get())
	#books_read = (e3.get())
	print(authors_read)
	get_info(authors_read)


e1 = Entry(master)
e2 = Entry(master)
#e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=2, sticky=W, pady=4)
Button(master,text="submit",command = getlol).grid(row=3, column=1, sticky=W, pady=4)
mainloop( )
