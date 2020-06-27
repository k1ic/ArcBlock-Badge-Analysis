# ArcBlock-Badge-Analysis
将链接中的devcon_did替换成自己的，即可查看自己拥有的徽章统计情况

[https://hashnews.k1ic.com/badge_stat/?devcon_did=z1oSWa9YFJNUXTk93RyCSc4JGJBiVfNXfdD](https://hashnews.k1ic.com/badge_stat/?devcon_did=z1oSWa9YFJNUXTk93RyCSc4JGJBiVfNXfdD)

# 实现原理
1. 通过资产链api获取devcon账户下的所有资产
2. 过滤出所有徽章（此时徽章内容为压缩数据）
3. 遍历上一步过滤出的徽章并解压缩
4. 分析每个徽章中的元素（徽章为svg格式，目前通过统计特定元素对应的标签个数计算元素个数。亦可通过机器学习方式识别）
5. 将分析结果写入markdown文件
6. 将markdown文件转换为html，并输出展示
