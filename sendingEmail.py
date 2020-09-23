import smtplib,ssl

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'samp06.09.1998@gmail.com'
receiver_email = ['gheewalakartik1233@gmail.com']
msg = 'Hello kartik'
password = input('Enter Password:')
context = ssl.create_default_context()

try:	
	server = smtplib.SMTP(smtp_server,port)
	server.ehlo()			
	server.starttls(context = context)
	server.ehlo()
	server.login(sender_email,password)
	server.sendmail(sender_email,receiver_email,msg)
	print("Msg Sent Successfully")

except Exception:
	print("Unable to send mail") 
finally:
	server.quit()