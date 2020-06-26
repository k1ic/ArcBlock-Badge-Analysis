#coding=utf-8
from flask import Flask, request
import os, time, markdown
from bs4 import BeautifulSoup
import os.path as op

class Markdown2Html:
    def __init__(self, cssfile=None):
        '''
        初始化 Markdown2Html 类，可传入特定 css 文件作为样式
        '''
        self.headTag = '<head><meta charset="utf-8" /><title>DevCon2020 徽章分析</title></head>'
        if cssfile:
            self.setStyle(cssfile)

    def setStyle(self, cssfile=None):
        '''
        设置样式表文件
        '''
        if cssfile is None:
            self.headTag = '<head><meta charset="utf-8" /></head>'
        else:
            with open(cssfile, 'r') as f:
                css = f.read()
                self.headTag = self.headTag[:-7] + f'<style  type="text/css">{css}</style>' + self.headTag[-7:]

    def convert(self, markdownText):
        rawhtml = self.headTag + markdown.markdown(markdownText, output_format='html5', extensions=['extra'])
        return BeautifulSoup(rawhtml, 'html5lib').prettify()

app = Flask(__name__)

@app.route('/badge_stat/', methods = ['GET'])
def badge_stat():
    devcon_did = request.args.get('devcon_did')
    #devcon_did = 'z1oSWa9YFJNUXTk93RyCSc4JGJBiVfNXfdD'
    if len(devcon_did) < 10:
        return 'devcon_did:' + devcon_did + ' illegal!'

    badge_stat_md = '../data/devcon_did_' + devcon_did + '.md'
    #if os.path.exists(badge_stat_md) and len(open(badge_stat_md).read()) < 300:
    #    return 'devcon_did:' + devcon_did + ' illegal!'

    if os.path.exists(badge_stat_md):
        mtime = int(str(os.stat(badge_stat_md).st_mtime).split('.')[0])
    else:
        mtime = 0
    now = int(str(time.time()).split('.')[0])

    #badge_stat_md最后更新时间不足2小时，直接展示；超过2小时，重新生成badge_stat_md并展示
    if mtime == 0 or round((now - mtime)/3600) > 2:
        res = os.system('sh do.sh ' + devcon_did)
        if res == -1:
            return 'devcon_did:' + devcon_did + ' illegal!'

    md_text = open(badge_stat_md).read()
    if len(md_text) > 300:
        md_html = markdown.markdown(md_text, output_format='html5', extensions=['extra'])

        m2h = Markdown2Html('github.css')
        rope_html = m2h.convert('<div>' + md_html + '</div>').replace('<table>', '<table border="1" cellpadding="3" cellspacing="0" style="width: 60%;margin:auto">', 1)

        return rope_html
    else:
        return 'devcon_did:' + devcon_did + ' illegal!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
