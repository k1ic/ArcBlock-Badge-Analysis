#!/usr/bin/sh
#sh do.sh z1oSWa9YFJNUXTk93RyCSc4JGJBiVfNXfdD

devcon_account_did=$1

#1.通过资产链api获取一个账户的所有资产（徽章、证书、门票）
curl 'https://xenon.abtnetwork.io/api'   -H 'authority: xenon.abtnetwork.io'   -H 'accept: application/json, text/plain, */*'   -H 'dnt: 1'   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'   -H 'content-type: application/json;charset=UTF-8'   -H 'origin: https://devcon.arcblockio.cn'   -H 'sec-fetch-site: cross-site'   -H 'sec-fetch-mode: cors'   -H 'sec-fetch-dest: empty'   -H 'referer: https://devcon.arcblockio.cn/zh/mybadges'   -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fr;q=0.6'   --data-binary '{"query":"{\n  listAssets(ownerAddress: \"'$devcon_account_did'\", paging: {size: 400}) {\n    code\n    account {\n      address\n      balance\n      genesisTime\n      migratedFrom\n      migratedTo\n      moniker\n      nonce\n      numAssets\n      numTxs\n      recentNumTxs\n      renaissanceTime\n      totalReceivedStakes\n      totalStakes\n      totalUnstakes\n    }\n    assets {\n      address\n      consumedTime\n      genesisTime\n      issuer\n      moniker\n      owner\n      parent\n      readonly\n      renaissanceTime\n      transferrable\n      ttl\n      data {\n        typeUrl\n        value\n      }\n    }\n    page {\n      cursor\n      next\n      total\n    }\n  }\n}\n"}' -s > ../data/devcon_did_${devcon_account_did}_all_badges_raw.log

#2.过滤徽章内容，并解压分析
res=`python parse_badge_json.py ${devcon_account_did}`
echo $res
