import os
from ahserver.webapp import webapp
from ahserver.serverenv import ServerEnv
from appPublic.registerfunction import RegisterFunction

from checklang.init import load_checklang

def docs(request, *args, **kw):
	return """Check langage for text
path: /v1/checklang
method: POST
headers:
	Content-Text: application/json

data:
	{
		"text": "what is language of this sentence? "
	}
response:
{
	"lang": "en"
}
"""
def checklang(request, params_kw, *args, **kw):
	env = request._run_ns
	engine = env.language_checker
	text = params_kw.text
	pred = engine.predict(text)
	d = pred[0][0][9:]
	return {
		'lang':d
	}

def init():
	load_checklang()
	rf = RegisterFunction()
	rf.register('checklang', checklang)
	rf.register('docs', docs)

if __name__ == '__main__':
	webapp(init)

