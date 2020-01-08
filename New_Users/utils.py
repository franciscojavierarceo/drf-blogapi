import yagmail
yagmail.register("roughosh47@gmail.com", "babi21091992#")
yag = yagmail.SMTP("roughosh47@gmail.com", "babi21091992#")
email = form.cleaned_data['email_address']
default_subject = "HouseHold income memeber mail confirmation"
user = form.cleaned_data['request_user']
msg = yag.inline("Hi {}, You have been added as a memeber to view/edit financial data".format(user))
yag.send(email, default_subject, msg)