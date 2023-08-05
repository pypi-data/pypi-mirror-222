#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Provides SMTP mail management.
"""

__author__ = 'ibrahim CÖRÜT'
__email__ = 'ibrhmcorut@gmail.com'

import os
import smtplib
import socket
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import time, sleep
from .. import print_error


class Smtp:
	def __init__(
			self,
			server='SMTP',  # 'LMTP', 'SMTP_SSL', 'SMTP'
			host='smtp.gmail.com',
			port=587,
			from_user=None,
			password=None
	):
		self.__session = None
		self.server = server
		self.host = host
		self.port = port
		self.from_user = from_user
		self.password = password
	
	def __enter__(self):
		self.login()
		return self
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.logout()
	
	def login(self, timeout=13):
		t = time()
		while (t + timeout) > time():
			try:
				if self.__session is None:
					context = ssl.create_default_context()
					if self.server == 'LMTP':
						self.__session = smtplib.LMTP(self.host, self.port)
					elif self.server == 'SMTP':
						self.__session = smtplib.SMTP(self.host, self.port)
						self.__session.ehlo()
						self.__session.starttls(context=context)
						self.__session.ehlo()
					elif self.server == 'SMTP_SSL':
						self.__session = smtplib.SMTP_SSL(
							self.host, self.port, context=context
						)
					else:
						raise ValueError(
							"Invalid server type. Supported values are "
							"'LMTP', 'SMTP_SSL', and 'SMTP'"
						)
					self.__session.login(self.from_user, self.password)
					print('-------> SMTP Server Login successfully...')
					break
			except (
					socket.gaierror, TimeoutError, ConnectionAbortedError,
					ConnectionError, ConnectionResetError,
					ConnectionRefusedError
			) as error:
				print_error(error, locals())
				self.__session = None
				sleep(0.5)
	
	def logout(self):
		if self.__session is not None:
			self.__session.close()
		self.__session = None
		print('-------> SMTP Server Logout successfully...')
	
	def send_email(
			self,
			mail_to,
			mail_cc='',
			mail_bcc='',
			subject='',
			text_message='',
			html_message='',
			attachment_path=None,
			embedded_image_status=True
	):
		"""

		:param mail_to: Mailing list to be seen in To
		:param mail_cc: Mailing list to be seen in CC
		:param mail_bcc: Mailing list to be seen in BCC
		:param subject: Text to be seen in the subject title
		:param text_message: Text in the post
		:param html_message: HTML in the post
		:param attachment_path: File path list if you want to add files.
				if it is singular, it can also be a string.
		:param embedded_image_status: Option to send as embedded if there are
				png, bmp, jpg in the files sent.
		"""
		msg = MIMEMultipart('related')
		try:
			msg['From'] = self.from_user
			msg['To'] = mail_to
			msg['Cc'] = mail_cc
			msg['Subject'] = subject
			msg_alternative = MIMEMultipart('alternative')
			msg.attach(msg_alternative)
			if html_message:
				msg_alternative.attach(MIMEText(html_message, 'html'))
			if text_message:
				msg_alternative.attach(MIMEText(text_message, 'plain'))
			html_link = ''
			for line in text_message.split('\n'):
				html_link += f'<br>{line}\n'
			html_link += '<br><br/>'
			if attachment_path is not None:
				for file_path in (
						attachment_path
						if isinstance(attachment_path, list)
						else [attachment_path]
				):
					try:
						fn = os.path.basename(file_path)
						with open(file_path, 'rb') as f:
							attachment = f.read()
					except Exception as error:
						attachment = None
						print(f"> Send Email Attachment File Error:{error} <")
						fn = None
					if attachment is not None:
						if (
								embedded_image_status and
								fn is not None and
								str(fn).lower().split('.')[1] in (
									'jpg', 'png', 'bmp'
								)
						):
							html_link += f'<img src="cid:{fn}"><p>{fn}</p>'
							msg_image = MIMEImage(attachment)
							msg_image.add_header('Content-ID', fn)
							msg_image.add_header('X-Attachment-Id', fn)
							c_i = f'inline; filename={fn}'
							msg_image['Content-Disposition'] = c_i
							msg.attach(msg_image)
						else:
							p = MIMEBase('application', 'octet-stream')
							p.set_payload(attachment)
							encoders.encode_base64(p)
							p.add_header(
								'Content-Disposition',
								"attachment; filename= %s" % fn
							)
							msg.attach(p)
					print(f'{file_path} file was attached to the mail...')
				msg_alternative.attach(MIMEText(html_link, 'html'))
			if self.__session is None:
				self.login()
			self.__session.sendmail(
				self.from_user,
				msg['To'].split(';') +
				msg['Cc'].split(';') +
				mail_bcc.split(';'),
				msg.as_string()
			)
			print('-------> Post sent successfully...')
		except Exception as error:
			print_error(error, locals())
			self.logout()
