
# -*- coding: utf-8 -*-
import smtplib as envio

#Envio de e-mail
def send(status, file, start, end, diff):
	de = 'wallacerobinson90@gmail.com'
	para = ['wallace_robinson@hotmail.com']
	assunto = '[FILE-COPY] ' + status + ': ' + file
	mensagem = ("""From: %s
To: %s
Subject: %s
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Disposition: inline
Content-Transfer-Encoding: 8bit

ARQUIVO: %s

>> TEMPO DE TRANSFERENCIA <<
Inicio: %s
Final: %s
Duracao: %s

Atenciosamente;
Wallace Salles
""" % (de, para, assunto, file, start, end, diff))

	try:
		mail = envio.SMTP('IP_OU_DNS_SERVIDOR_SMTP', 25)
		mail.ehlo()
		mail.sendmail(de, para, mensagem.encode("utf8"))
		mail.close()
	except:
		pass
