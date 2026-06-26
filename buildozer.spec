[app]
title = FileSender
package.name = filesender
package.domain = org.moon
source.dir = .
source.include_exts = py,png,jpg,kv,txt
version = 0.1

# 核心依赖：必须包含 python3, kivy 和网络传输需要的库
requirements = python3,kivy,requests,urllib3,idna,certifi

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a