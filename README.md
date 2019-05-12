一个以 Django 作为框架搭建的个人博客。

博客效果： https://tendcode.com/

## 功能介绍
- Django 自带的后台管理系统，方便对于文章、用户及其他动态内容的管理
- 文章分类、标签、浏览量统计以及规范的 SEO 设置
- 用户认证系统，在 Django 自带的用户系统的基础上扩展 Oauth 认证，支持微博、Github 等第三方认证
- 文章评论系统，炫酷的输入框特效，支持 markdown 语法，二级评论结构和回复功能
- 信息提醒功能，登录和退出提醒，收到评论和回复提醒，信息管理
- 强大的全文搜索功能，只需要输入关键词就能展现全站与之关联的文章
- RSS 博客订阅功能及规范的 Sitemap 网站地图
- 实用的在线工具
- 友情链接和推荐工具网站的展示
- 缓存系统，遵循缓存原则，加速网站打开速度
- RESTful API 风格的 API 接口

## Todo
- [ ] 添加一个博客信息播报的版块，播报博客动态
- [ ] 添加定时任务，提取Github上面项目的信息，显示到博客前台

## 博客主页效果
![博客主页 PC 效果](https://user-images.githubusercontent.com/30201215/54125719-b3ffeb00-4440-11e9-9edd-e2eabf2a9dd5.png)

## 博客ipad显示效果（响应式）
![ipad 竖屏效果](https://user-images.githubusercontent.com/30201215/54197732-aeb5a580-44ff-11e9-8d2c-8b02335b3826.png)

## 博客手机端显示效果（响应式）
![博客手机端效果](https://user-images.githubusercontent.com/30201215/54195790-9727ee00-44fa-11e9-91aa-7b5e9852f1f7.png)

## 运行指导
- 由于本项目分为几个不同的分支，每个分支的功能是一样的，但是运行的方式不同，所以需要根据分支查看对应的运行wiki
- 指导 wiki：https://github.com/Hopetree/izone/wiki
