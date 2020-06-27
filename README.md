# ArcBlock-Badge-Analysis

将链接中的devcon_did替换成自己的，即可查看自己拥有的徽章统计情况

[https://hashnews.k1ic.com/badge_stat/?devcon_did=z1oSWa9YFJNUXTk93RyCSc4JGJBiVfNXfdD](https://hashnews.k1ic.com/badge_stat/?devcon_did=z1oSWa9YFJNUXTk93RyCSc4JGJBiVfNXfdD)

# 项目背景
徽章玩家有统计徽章中特定元素数量（如：狗、羊、大雁等）的诉求


# 实现原理
1. 通过资产链api获取devcon账户下的所有资产
2. 过滤出所有徽章（此时徽章内容为压缩数据）
3. 遍历上一步过滤出的徽章并解压缩（先base64 decode，再ungzip）
4. 分析徽章中的元素（徽章为svg格式，目前通过统计特定元素对应的标签个数计算元素个数。亦可通过机器学习方式识别）
5. 将分析结果写入markdown文件
6. 将markdown文件转换为html，并输出展示

# 待优化
1. 对did更严谨的校验
2. 优化页面打开速度
3. 交互式排序
4. 分析结果页显示徽章
5. 采用机器学习算法识别徽章元素
