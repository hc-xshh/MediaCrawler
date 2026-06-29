# MediaCrawler

> 多平台自媒体爬虫。支持抖音、小红书、微博、B站、知乎等平台的内容抓取。

**本项目为 clone（上游：NanmiCoder/MediaCrawler）。仅作学习和参考使用。**

## Build & Run

```bash
pip install -r requirements.txt
python main.py --platform xhs --type search --keywords "关键词"
```

## Structure

```
main.py           # CLI 入口
media_platform/   # 各平台爬虫实现
config/           # 配置
database/         # 数据存储
store/            # 爬取结果存储
libs/             # 通用库
```

## Platforms

- 小红书 (xhs)
- 抖音 (dy)
- 微博 (weibo)
- B站 (bilibili)
- 知乎 (zhihu)
- 快手 (ks)

## Notes

- 这是 clone，未经修改，上游有 776 commits
- 各平台需要有效的 Cookie/Token 才能正常抓取
- 目前仅作技术参考，未接入 Hermes 自动化 pipeline
