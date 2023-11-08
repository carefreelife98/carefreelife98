## update_blogPost.py
import feedparser

blog_url = "https://carefreelife98.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
    if idx > MAX_NUM:
        break;
    feed_date = entrie['published_parsed']
    latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """
![header](https://capsule-render.vercel.app/api?type=waving&text=CarefreeLife!&color=gradient)

<br><br>

## Today's Carefree
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FCarefreeLife98&count_bg=%23ADAB92&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=Wish+you+all+Carefree&edge_flat=false)](https://hits.seeyoufarm.com)

<br>

[![Carefreelife's GitHub stats](https://github-readme-stats.vercel.app/api?username=carefreelife98&show_icons=true&theme=dark)](https://github.com/anuraghazra/github-readme-stats)

<br><br>

## Blog
<img src="https://img.shields.io/badge/Github Pages-222222?style=for-the-badge&logo=githubpages&logoColor=white">
[CarefreeLife's Blog](https://carefreelife98.github.io/)

<br><br>

```
🧑🏻‍💻 Once I've Used 🧑🏻‍💻
```

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=carefreelife98&layout=compact&theme=swift&hide=jupyter%20notebook)](https://github.com/anuraghazra/github-readme-stats)

## Dev

>
> **Programming Languages** <br>
> <img src="https://img.shields.io/badge/JAVA-E6522C?style=for-the-badge&logo=java&logoColor=white">
> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
> 
> **Database** <br>
> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white">
> <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=MariaDB&logoColor=white">
> 
> **FrameWork** <br>
> <img src="https://img.shields.io/badge/SpringBoot-6DB33F?style=for-the-badge&logo=SpringBoot&logoColor=white">
> 
> **CI/CD** <br>
> <img src="https://img.shields.io/badge/Github Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white">
> <img src="https://img.shields.io/badge/ArgoCD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white">
> <img src="https://img.shields.io/badge/TerraformCloud-7B42BC?style=for-the-badge&logo=terraform&logoColor=white"> <br>

## Ops
> 
> **Cloud Infra** <br>
> <img src="https://img.shields.io/badge/aws-FF9900?style=for-the-badge&logo=aws&logoColor=white">
> <img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white">
> 
> **Monitoring** <br>
> <img src="https://img.shields.io/badge/Istio-466BB0?style=for-the-badge&logo=istio&logoColor=white">
> <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white">
> <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white">
> 
> **Orchestration** <br>
> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">
> <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=Kubernetes&logoColor=white">
> <img src="https://img.shields.io/badge/EKS-FF9900?style=for-the-badge&logo=amazoneks&logoColor=white">
> 
> **Registry** <br>
> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

<br><br>

<h1>Latest Post of My Blog!!</h1>

"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f:
    f.write(resultREADME)
