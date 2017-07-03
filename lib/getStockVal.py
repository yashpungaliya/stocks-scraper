import re
import time
import urllib.request
from datetime import datetime
import os.path

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_html_data(stock):
	global stock_code
	stock_code=stock
	url = "https://www.google.com/finance?q="
	url = url + stock
	r = urllib.request.urlopen(url).read()
	data = r.decode("utf-8")
	return data


def find_stock_val(data):
	global finalVal
	val = re.search('meta itemprop="price"', data)
	if val is None:
		print("Not Found")
	start = val.start()
	end = start + 50
	newVal = data[start:end]
	m = re.search('content="', newVal)
	start = m.end()
	newVal = newVal[start:]
	m = re.search("/", newVal)
	start = 0
	end = m.end() - 3
	finalVal = newVal[:end]
	return finalVal


def write_to_csv(filename,finalVal):
	print("Filename:" + filename)
	parentPath=os.path.abspath('.')
	p1 = os.path.abspath('..')
	foldername=datetime.now().strftime("%D")
	foldername=foldername.replace("/","-")
	myPath=p1+'/data/'+foldername
	if not os.path.exists(myPath):
		os.makedirs(myPath)
	with open(myPath+'/'+filename, 'a') as f:
		dt = str(datetime.now().time())
		dt = dt[:8]
		dt = dt.replace(":", "")
		dt=float(dt[:2])+float(dt[2:4])/60+float(dt[4:])/3600
		finalVal = finalVal.replace(",", '')
		print("Writing at " + str(dt) + " a value of " + finalVal+' to '+filename)
		f.write(finalVal + ';' + str(dt) + '\n')


def random_loop(times,delay):
	for i in range(0,int(times)-1):
		data = get_html_data(stock_code)
		finalval = find_stock_val(data)
		filename=stock_code+'.csv'
		write_to_csv(filename,finalVal)
		time.sleep(float(delay))

#uncomment and replace relevant spaces to send mail
# def send_mail():
# 	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
# 	s.starttls()
# 	s.login('MY_MAIL_ADDR', 'MY_PASSWORD')
# 	msg = MIMEMultipart()
# 	msg['From'] = 'MY_MAIL_ADDR'
# 	msg['To'] = 'THEIR_MAIL_ADDR'
# 	msg['Subject'] = "This is a TEST"
# 	# add in the message body
# 	msg.attach(MIMEText(statement, 'plain'))
# 	# send the message via the server set up earlier.
# 	s.send_message(msg)
# 	del msg
# 	s.quit()


# send_mail()
