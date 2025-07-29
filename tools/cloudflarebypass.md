# CloudFlare Bypass
```
Source: https://github.com/Anorov/cloudflare-scrape
Description: Script or automate against a page that uses I'm Under Attack Mode from CloudFlare or DDOS protection

#!/usr/bin/env python

import cfscrape

url = 'http://yashit.tech/tryharder/'

scraper = cfscrape.create_scraper()
print scraper.get(url).content
```

## Back to README.md
[BACK](/README.md)