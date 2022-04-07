import pyshorteners

login_url = input('enter your link please : ')

type_tiny = pyshorteners.Shortener()

short_url = type_tiny.tinyurl.short(login_url)



print(short_url)