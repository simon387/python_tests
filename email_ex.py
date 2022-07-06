#
# esempio mando email
#
import smtplib


# lui manda una email, noi facciamo altro, come mandare su telegram un messaggio
def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('ed.magician@gmail.com', 'askjndo3n4424')
	subject = 'Price fell down!'
	body = 'Check the amazon link https............'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'ed@asd.com',
		'simosad@asd.com',
		msg
	)
	print('HEY MAIL HAS BEEN SENT!')

	server.quit()
