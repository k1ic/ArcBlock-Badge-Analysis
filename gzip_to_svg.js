//node gzip_to_svg.js /root/devcon/data/devcon_did_z1oSWa9YFJNUXTk93RyCSc4JGJBiVfNXfdD/zjddhjWzFHr5qXwt2KpfFtzZjtyDmmE9a51c.raw
var fs = require("fs")
var pako = require('pako');
var atob = require("atob");

//读取徽章压缩内容
var raw_file = process.argv[2];
var raw = fs.readFileSync(raw_file).toString();
//console.log(raw)

//徽章内容解压缩（先base64 decode，在ungzip）
var b = pako.ungzip(atob(raw), {});
var rope = Buffer.from(b).toString('utf8');
//console.log(rope)

//徽展解压后内容写入文件
var rope_file = raw_file.replace('.raw', '.rope');
fs.writeFileSync(rope_file, rope);
