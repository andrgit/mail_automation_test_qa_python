import yagmail

mymail = 'andrmytest1@gmail.com'
mail_password = 'password123@'

yag = yagmail.SMTP(mymail, mail_password)
contents = [
    "This is the letter, and here test text."
]
# yag.send('mailrecipient@mail.com', 'Title', contents(with text and url if necessary)
yag.send('mytestand1@gmail.com', 'Test Letter', contents)

# Alternatively, with a simple one-liner:
# yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', contents)
