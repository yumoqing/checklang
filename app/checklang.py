import os
from ahserver.webapp import webapp
from ahserver.serverenv import ServerEnv
from appPublic.registerfunction import RegisterFunction

import fasttext

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
	engine = kw.get('engine')
	text = params_kw.text
	pred = engine.predict(text)
	d = pred[0][0][9:]
	return {
		'lang':d
	}

def init():
	p = os.path.join(os.path.dirname(__file__), 'lid.176.ftz')
	print(f'model path={p}')
	model = fasttext.load_model(p)
	# 需先下载模型：https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz
	env = ServerEnv()
	env.engine = model
	rf = RegisterFunction()
	rf.register('checklang', checklang)

if __name__ == '__main__':
	rf = RegisterFunction()
	rf.register('checklang', checklang)
	rf.register('docs', docs)
	webapp(init)

