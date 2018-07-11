import os.path
from pathlib import Path

def python_file_check():
	#File paths containing required files for check
	with open("bootstrap.txt") as f:
		content = f.readlines()

	#String whitespace characters from eachline
	content = [x.strip() for x in content]
	_counter_=0
	_index_=1
	_valid_=True

	for x in content:
		_file_ = Path(x)
		if _file_.is_file():
			_valid_=True
		else:
			_counter_ = _counter_ + _index_

	if _counter_ > 0:
		_valid_=False

	return _valid_
