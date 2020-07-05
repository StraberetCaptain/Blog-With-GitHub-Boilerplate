# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "straberetcaptain/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
# 站点设置
site_name = "虎抓板2号"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-07-05T00:00-06:00"
author = "StraberetCaptain"
email = "taemtoeatjin@gmail.com"
author_homepage = "https://www.straberrycaptain.com"
description = "🐯🐹"
key_words = ['Maverick', '虎抓板', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Weibo",
        "url": "https://www.weibo.com/u/6517142916",
        "brief": "虎抓板1号"
    },  
    {
        "name": "Bilibili",
        "url": "https://space.bilibili.com/1761554?from=search&seid=524068925455877553",
        "brief": "乱码乱码乱码啦"
    },
    {
        "name": "有求必应箱",
        "url": "http://www.popiask.cn/8Btjjn",
        "brief": "popi2252588"
    },
    {
        "name": "有问必答的回复",
        "url": "https://m.weibo.cn/6517142916/4522875904286610",
        "brief": "在这里"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Weibo",
        "url": "https://www.weibo.com/u/6517142916",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
