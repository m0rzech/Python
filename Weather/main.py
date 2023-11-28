import re
import urllib.request


def main():
	f=urllib.request.urlopen('https://pogoda.onet.pl/prognoza-pogody/warszawa-357732')
	automat = []
	values = []
	pat=[r'([-]?[0-9]+)',r'<span>Prognoza pogody dla: (.*?)</span>']
	tag_list=['<div class="temp">','<h2 class="blockHeader"><span>Prognoza pogody dla: ']

	for i in range(2):
		automat.append(re.compile(tag_list[i]))	
		line=f.readline()
		while automat[i].search(str(line))==None:
			line=f.readline()
		#loop ends - value has been found
		result = re.findall(pat[i],str(line))

		values.append(result[0])

	print (f'What temperature is now in {values[1]}?  {values[0]}')
		
if __name__ == '__main__':
	main()