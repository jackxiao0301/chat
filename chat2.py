
def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def no_empty(lines):
	for line in lines:
		if line == '':
			lines.remove(line)
	return lines


def no_date(lines):
	new = []
	for line in lines:
		s = line.split(',')
		new.append(s[0])
	return new


def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Jack X':
			person = 'Jack X'
			continue
		elif line == 'Huang Yv':
			person = 'Huang Yv'
			continue
		if person:
			new.append(person + ':' + line)
	return new 


def write_file(filename, lines, encoding='utf-8-sig'):
	with open (filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('-LINE-Viki.txt')
	lines = no_empty(lines)
	lines = no_date(lines)
	lines = convert(lines)
	write_file('output2.txt', lines)
	

main()