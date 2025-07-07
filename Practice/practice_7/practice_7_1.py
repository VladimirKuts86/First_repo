mails = ["ivan@gmail.com", "kate@yahoo.com", "john@gmail.com", "test@outlook.com"]
gmail_mails = [x for x in mails if x.endswith('gmail.com')]
print(gmail_mails)