# -*- coding: utf-8 -*
#python parse_badge_json.py z1oSWa9YFJNUXTk93RyCSc4JGJBiVfNXfdD
import json
import sys,os
#reload(sys)
#sys.setdefaultencoding('utf8')
import importlib
importlib.reload(sys)

#创建徽章压缩内容存储目录
assets_content_path = '../data/devcon_did_' + sys.argv[1] + '/'
if not os.path.exists(assets_content_path):
    os.makedirs(assets_content_path)

#创建徽章分析结果文件
badge_text_file = '../data/devcon_did_' + sys.argv[1] + '.md'
if os.path.exists(badge_text_file):
    os.remove(badge_text_file)

if not os.path.exists(badge_text_file):
    f = open(badge_text_file, 'w')
    f.write('# <center>徽章分析</center>\n')
    f.close()
badge_text = ''

#获取一个devcon_did账户的所有徽章压缩数据（包括门票、证书、徽章）
raw_file = '../data/devcon_did_' + sys.argv[1] + '_all_badges_raw.log'
with open(raw_file, 'r') as f:
    res = json.load(f)

if len(res['data']['listAssets']['assets']) == 0:
    exit(-1)

#筛选徽章，并对其内容解压分析
have_dog_num = 0
have_sheep_num = 0
have_rabbit_num = 0
for k, v in enumerate(res['data']['listAssets']['assets']):
    #过滤门票、证书
    if str(v['moniker']).endswith('证书') or str(v['moniker']).endswith(' 票'):
        continue

    #徽章did
    asset_did = v['address']

    #徽章压缩内容
    t = json.loads(v['data']['value'].encode('utf-8'))
    c = t['credentialSubject']['display']['content']

    #徽章压缩内容写入文件
    raw_path = assets_content_path + asset_did + '.raw'
    f = open(raw_path, 'w')
    f.write(c)
    f.close()

    #徽章内容解压缩，并写入文件
    abs_raw_path = os.path.abspath(raw_path)
    os.system('cd /root/arcblock-nft-starter/api/libs; node gzip_to_svg.js ' + abs_raw_path)

    #分析徽章内容，并写入文件
    abs_rope_path = abs_raw_path.replace('.raw', '.rope', 1)
    text = os.popen('sh badge_analysis.sh ' + abs_rope_path).read()
    if len(text) > 0:
        arr_tmp = text.split('|')
        if int(arr_tmp[6]) > 0:
            have_dog_num += 1
        if int(arr_tmp[11]) > 0:
            have_rabbit_num += 1
        if int(arr_tmp[10]) > 0:
            have_sheep_num += 1

        badge_text = badge_text + '|[' + asset_did + '](https://xenon.abtnetwork.io/node/explorer/assets/'+ asset_did +')'
        badge_text = badge_text + text

#徽章分析结果写入文件
with open(badge_text_file, 'a+') as f:
    badge_total = int(os.popen('ls -al ../data/devcon_did_' + sys.argv[1] + '/*.rope | wc -l').read())
    #f.write('## 徽章总数：' + str(badge_total) + ' did:[' + sys.argv[1] + '](https://xenon.abtnetwork.io/node/explorer/accounts/' + sys.argv[1] + ')\n')
    f.write('## 徽章共' + str(badge_total) + '张 有狗' + str(have_dog_num) + '张 有兔' + str(have_rabbit_num) + '张 有羊' + str(have_sheep_num) + '张 \n')
    f.write('|徽章did|徽章标题|太阳|月亮|云|大雁|狗|男人|女人|孩子|羊|兔子|'+"\n")
    f.write('|:---|:---|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|'+"\n")
    f.write(badge_text)
