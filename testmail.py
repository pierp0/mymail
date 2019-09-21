import mymail

srvaddr = ""
pwd = ""
port = 465

sender = ""
receiver = ""
receiver_lst = ["", ""]

sbj = ""
body = ""

attachpath = "spam.jpg"
attachpath_lst = ["eggs.jpg", "spam.pdf"]

# Test: send an email to one address with zero or one attachment
mymail.sendmymail(srvaddr, sender, receiver, pwd, port, sbj, body, attachpath)

# Test: send an email to more then one address (address list) with one or more attachment files (list with one or more paths)
mymail.sendmymail(srvaddr, sender, receiver, pwd, port, sbj, body, attachpath_lst)
