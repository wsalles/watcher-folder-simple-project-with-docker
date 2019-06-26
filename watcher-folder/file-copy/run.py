
#-*- coding: utf-8 -*-
import logging, shutil
from patience import watchers
from datetime import datetime
import config.vars as config
import config.email as SMTP

def action(file):
	start = datetime.now()
	filename = file.replace('/watcher_one/watch_folder/', '')
	logging.info(f'O arquivo {filename} foi capturado!')
	while True:
		errors = 0
		try:
			shutil.copy(file, destination_folder + filename)
			logging.info(f'O arquivo {filename} foi copiado para {output_folder}!')
			end = datetime.now()
			diff = end - start
			try:
				SMTP.send('SUCCESS', filename, str(start), str(end), str(diff))
			except:
				logging.info('Falha ao enviar e-mail...')
			logging.info('E-mail enviado com sucesso.')
			break
		except:
			errors += 1
			if errors == 3:
				end = datetime.now()
				diff = end - start
				logging.info(f'Falha ao copiar o arquivo {filename}...')
				try:
					SMTP.send('FAIL', filename, str(start), str(end), str(diff))
				except:
					logging.info('Falha ao enviar e-mail...')
				return False

if __name__ == '__main__':
	logging.basicConfig(filename="/var/log/watcher_one.log", filemode='a', datefmt='%d-%b-%y %H:%M:%S',
						format='%(asctime)s - %(message)s', level=logging.INFO)
	watch_folder = config.data['WATCH_FOLDER']
	destination_folder = config.data['DESTINATION']
	watcher = watchers.PatternWatcher(
		callback=action,
		workdir=config.data['WATCHDIR'],
		ext=config.data['EXT'],
		timeout=config.data['TIMEOUT'],
		blocking=True,
		recursive=False)
	watcher.start()
