import os
import dirtyjson
import re

invalid_escape = re.compile(r'\\[0-7]{1,3}')

def repair(exception, s):
	"""Attempts to partially fix JSON by replacing chars until it succeeds.

	Args:
	  exception - The exception thrown during parsing.
	  s - The content string to parse.

	Returns:
		A partially fixed JSON string.
	"""
  unexp = int(re.findall(r'\(char (\d+)\)', str(exception))[0])
  unesc = s.rfind(r'"', 0, unexp)
  s = s[:unesc] + r'\"' + s[unesc+1:]
  closg = s.find(r'"', unesc + 2)
  s = s[:closg] + r'\"' + s[closg+1:]
  return s

def parse_bad_contents(contents):
	"""Recursively attempts to fix JSON until it succeeds.

	Args:
		contents - String contents to try parsing.

	Returns:
		Parsed JSON result.
	"""
	try:
		return dirtyjson.loads(contents)
	except Exception as e:
		print(contents)
		return parse_bad_contents(repair(e, contents))

def main():

	results = []

	for filename in os.listdir(os.path.join('.', 'data')):
		print(filename)
		with open(os.path.join('.', 'data', filename), 'r') as f:
			file_contents = f.read()
			try:
				json_result = parse_bad_contents(file_contents)
				results.append(json_result);
			except Exception as e:
				print(e)
				raise Exception('TOTAL FAIL')


	print(len(results))

if __name__ == '__main__':
	main()