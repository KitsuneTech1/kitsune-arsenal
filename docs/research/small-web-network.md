# Small web, HTTP, network, DNS and browser micro-utilities for the Kitsune Capability Gateway

Prices are approximate from memory (none verified live). Verified column is "no" on every row.

| # | Tool | Does | Replaces | ~$/mo | Backend/method | Verified |
|---|------|------|----------|-------|----------------|----------|
| 1 | url_expand | Follow redirects on a short link and return the final URL plus the hop chain | Unshorten.me API, CheckShortURL | 0 to 10 | Python httpx with follow_redirects and history, HEAD then GET fallback | no |
| 2 | page_links | Extract all links from a page, tagged internal or external | Screaming Frog light use, Link Extractor SaaS | 0 to 20 | selectolax or BeautifulSoup on fetched HTML | no |
| 3 | domain_available | Check if a domain is registered | Namecheap or GoDaddy search API | 0 | RDAP query via rdap.org plus DNS NXDOMAIN check | no |
| 4 | favicon_get | Fetch a site's best favicon or touch icon | Favicon Grabber, Clearbit logo API | 0 to 50 | Parse link rel icons, fall back to /favicon.ico, pick largest with Pillow | no |
| 5 | ua_parse | Parse a User-Agent string into browser, OS, device | WhatIsMyBrowser API | 0 to 30 | ua-parser or uap-core regexes | no |
| 6 | robots_check | Fetch robots.txt and say if a URL is allowed for a given agent | Ahrefs or SEMrush robots tester | 0 to 99 | Python urllib.robotparser or Protego | no |
| 7 | dns_propagation | Query many public resolvers for a record and compare answers | DNSChecker.org, whatsmydns Pro | 0 to 10 | dnspython against a list of public resolvers | no |
| 8 | cms_detect | Detect a page's CMS and frameworks | BuiltWith, Wappalyzer | 15 to 250 | wappalyzer-core fingerprints (or webappanalyzer data) over fetched HTML and headers | no |
| 9 | og_unfurl | Turn a URL into an OpenGraph and Twitter card summary | Iframely, Embedly, LinkPreview API | 0 to 30 | extruct or opengraph parser | no |
| 10 | ttfb_measure | Measure DNS, connect, TLS and TTFB for a URL | Pingdom, GTmetrix one-offs | 10 to 50 | curl -w timing variables or httpx trace | no |
| 11 | http_headers | Dump response headers and status for a URL | httpstatus.io, Hurl online | 0 | HEAD and GET via httpx | no |
| 12 | redirect_chain | Show every redirect hop with status and timing | Redirect Checker SaaS | 0 to 20 | httpx history walk | no |
| 13 | security_headers_grade | Grade HSTS, CSP, XFO and other security headers | securityheaders.com Pro | 0 to 25 | Local rule table over response headers | no |
| 14 | tls_cert_info | Read a cert: issuer, SAN, expiry, chain | SSL Labs, SSLMate monitoring | 0 to 15 | Python ssl plus cryptography | no |
| 15 | cert_expiry_watch | Warn when a cert has fewer than N days left | Uptime Robot SSL checks, StatusCake | 7 to 25 | Scheduled ssl handshake checks | no |
| 16 | whois_lookup | Registrar, dates and nameservers for a domain | WhoisXML API | 0 to 50 | RDAP with whois CLI fallback | no |
| 17 | dns_records_all | Fetch A, AAAA, MX, TXT, NS, CAA, SOA in one call | MXToolbox, DNSdumpster | 0 to 129 | dnspython | no |
| 18 | reverse_dns | PTR lookup for an IP | MXToolbox reverse | 0 | dnspython | no |
| 19 | ip_geo | Country, city and ASN for an IP | ipinfo.io, ipstack | 0 to 49 | MaxMind GeoLite2 with mmdb reader | no |
| 20 | asn_lookup | Map IP to ASN and org, or list a prefix set | bgp.he.net, IPinfo | 0 to 99 | RIPEstat API or local pyasn dump | no |
| 21 | my_ip | Report the egress IP and geo the gateway appears as | ifconfig.me, ipify | 0 | Own tiny echo endpoint | no |
| 22 | port_check | Test if a TCP port is open on a host | YouGetSignal, canyouseeme | 0 | asyncio open_connection with timeout | no |
| 23 | ping_host | ICMP or TCP ping with loss and latency stats | Pingdom, Uptime tools | 0 to 15 | ping or tcping subprocess | no |
| 24 | traceroute | Trace route to a host with hop RTT | Site24x7 traceroute, Looking Glass | 0 to 10 | mtr --json | no |
| 25 | uptime_probe | One-shot up or down check from the gateway | Uptime Robot, Better Stack | 0 to 29 | httpx with retry logic | no |
| 26 | uptime_monitor | Recurring monitor with change alerts | Uptime Robot Pro, Pingdom | 7 to 15 | Uptime Kuma API | no |
| 27 | page_diff | Detect content change on a page since last check | Visualping, Distill.io | 10 to 50 | changedetection.io API | no |
| 28 | sitemap_fetch | Parse sitemap.xml and index files into a URL list | Screaming Frog, XML sitemap tools | 0 to 259 | ultimate-sitemap-parser | no |
| 29 | sitemap_discover | Find sitemap URLs via robots.txt and common paths | SEO crawlers | 0 | robots parse plus probe list | no |
| 30 | rss_discover | Find a site's RSS or Atom feed URL | Feedbin discovery, Feedly | 0 to 12 | Parse link rel alternate, probe /feed and /rss | no |
| 31 | feed_parse | Fetch and normalize an RSS or Atom feed to JSON | Feedly API, Inoreader API | 0 to 9 | feedparser | no |
| 32 | rss_bridge | Create a feed for a page that has none | FetchRSS, Feedity | 5 to 15 | RSS-Bridge or css-selector scraper | no |
| 33 | html_to_markdown | Convert a page to clean Markdown | Jina Reader, Firecrawl scrape | 0 to 19 | trafilatura or readability plus markdownify | no |
| 34 | readable_extract | Extract the main article text and byline | Diffbot Article API, Mercury Parser | 0 to 299 | trafilatura or readability-lxml | no |
| 35 | page_metadata | Title, description, canonical, lang, hreflang | SEO extension suites | 0 to 30 | selectolax | no |
| 36 | jsonld_extract | Pull JSON-LD and microdata schema from a page | Schema validators, Diffbot | 0 | extruct | no |
| 37 | canonical_check | Compare canonical, redirect and og:url for a page | SEO audit tools | 0 to 99 | httpx plus HTML parse | no |
| 38 | hreflang_check | Validate hreflang reciprocity across pages | Ahrefs, SEMrush site audit | 99 | Fetch and cross-compare | no |
| 39 | broken_links | Crawl a page or site and list dead links | Dr. Link Check, Ahrefs | 0 to 99 | Async httpx crawler with HEAD probes | no |
| 40 | link_status_batch | Bulk status check of a URL list | Link checker SaaS | 0 to 20 | Async httpx with concurrency limit | no |
| 41 | archive_lookup | Find the nearest Wayback snapshot of a URL | Archive.org manual use | 0 | web.archive.org availability API | no |
| 42 | archive_save | Trigger a Wayback Save Page Now for a URL | Perma.cc | 0 to 25 | Save Page Now API | no |
| 43 | screenshot_url | Full-page or viewport screenshot of a URL | ScreenshotOne, Urlbox, Browserless | 17 to 99 | Playwright headless Chromium | no |
| 44 | pdf_from_url | Render a URL to PDF | PDFShift, Api2pdf | 9 to 49 | Playwright page.pdf | no |
| 45 | render_html | Fetch a JS-rendered page's final DOM | ScrapingBee, ScraperAPI | 49 to 99 | Playwright with wait-for-idle | no |
| 46 | element_screenshot | Screenshot one CSS selector | Urlbox selector shots | 19 to 99 | Playwright locator.screenshot | no |
| 47 | css_select | Run a CSS or XPath selector against a URL | Apify actors, Import.io | 0 to 49 | selectolax or lxml | no |
| 48 | table_extract | Pull HTML tables into CSV or JSON | Table Capture, Import.io | 0 to 30 | pandas.read_html | no |
| 49 | text_diff_urls | Diff the text of two URLs or two snapshots | Diffchecker Pro | 0 to 10 | difflib on extracted text | no |
| 50 | js_error_capture | Load a page and list console errors and failed requests | Sentry synthetic, BrowserStack | 0 to 29 | Playwright console and requestfailed events | no |
| 51 | network_waterfall | List every request a page makes with sizes and timing | WebPageTest, GTmetrix | 0 to 50 | Playwright HAR export | no |
| 52 | third_party_scan | List third-party domains a page loads from | Blacklight, Ghostery | 0 | HAR domain grouping | no |
| 53 | tracker_detect | Flag known trackers and ad scripts on a page | Ghostery, Blacklight | 0 to 5 | Disconnect or EasyPrivacy lists over HAR | no |
| 54 | cookie_audit | List cookies set on load with flags and lifetime | CookieYes scanner, Cookiebot | 10 to 30 | Playwright context.cookies | no |
| 55 | lighthouse_quick | Run a Lighthouse score for a URL | PageSpeed paid monitors, Calibre | 0 to 50 | lighthouse CLI in headless Chromium | no |
| 56 | core_web_vitals | Field and lab LCP, CLS, INP | SpeedCurve, DebugBear | 15 to 100 | CrUX API plus web-vitals in Playwright | no |
| 57 | compression_check | Check gzip, brotli and zstd support and savings | GTmetrix, Check GZIP tools | 0 | Request with Accept-Encoding variants | no |
| 58 | http_version_check | Report if a host serves HTTP/1.1, 2 or 3 | HTTP/3 check sites | 0 | curl --http2 and --http3 probes | no |
| 59 | cdn_detect | Identify the CDN or WAF in front of a host | BuiltWith, Wafw00f web | 0 to 295 | Header and CNAME fingerprints, wafw00f | no |
| 60 | server_stack_detect | Guess server software and language from headers | Netcraft, BuiltWith | 0 to 295 | Header and cookie fingerprint table | no |
| 61 | subdomain_list | Enumerate known subdomains from public sources | SecurityTrails, Censys | 50 to 500 | crt.sh CT logs plus subfinder | no |
| 62 | ct_log_search | Search certificate transparency for a domain | Censys, Facebook CT monitor | 0 to 100 | crt.sh JSON endpoint | no |
| 63 | dns_history | Show past DNS records for a domain | SecurityTrails, DNSlytics | 50 to 500 | Passive DNS free APIs, own snapshot store | no |
| 64 | mx_check | Validate MX records and mail server reachability | MXToolbox | 0 to 129 | dnspython plus SMTP banner connect | no |
| 65 | spf_dkim_dmarc | Validate SPF, DKIM selector and DMARC policy | dmarcian, EasyDMARC | 0 to 40 | dnspython with checkdmarc | no |
| 66 | blacklist_check | Check an IP or domain against DNSBLs | MXToolbox Blacklist, HetrixTools | 0 to 15 | DNS queries to common DNSBL zones | no |
| 67 | email_syntax_mx | Validate an email address syntax and MX | ZeroBounce basic, Kickbox | 10 to 40 | email-validator with MX lookup | no |
| 68 | disposable_domain | Flag throwaway email domains | Kickbox, Abstract API | 0 to 25 | disposable-email-domains list | no |
| 69 | url_normalize | Canonicalize a URL, strip tracking params, sort query | none/glue | 0 | Python w3lib or url-normalize | no |
| 70 | utm_strip | Remove UTM and click-id parameters from a URL | Clean-links extensions | 0 | ClearURLs ruleset | no |
| 71 | url_parse | Break a URL into scheme, host, path, params, eTLD+1 | none/glue | 0 | tldextract and urllib.parse | no |
| 72 | punycode_convert | Convert IDN domains to and from punycode | none/glue | 0 | Python idna | no |
| 73 | homoglyph_check | Flag lookalike or mixed-script domains | Phishing lookalike monitors | 0 to 50 | confusable_homoglyphs plus dnstwist | no |
| 74 | typosquat_gen | Generate typo variants and check which are registered | DomainTools Iris, dnstwist SaaS | 0 to 100 | dnstwist | no |
| 75 | phishing_url_check | Check a URL against known phishing lists | Google Safe Browsing UI, VirusTotal | 0 to 10 | OpenPhish and PhishTank feeds plus Safe Browsing API | no |
| 76 | url_reputation | Multi-source reputation for a URL or domain | VirusTotal Premium, URLhaus | 0 to 500 | URLhaus, PhishTank and Tranco rank locally | no |
| 77 | tranco_rank | Look up a domain's popularity rank | SimilarWeb, Alexa (retired) | 0 to 125 | Tranco list download | no |
| 78 | content_type_sniff | Detect real file type from URL bytes, not the extension | none/glue | 0 | libmagic on first bytes | no |
| 79 | file_size_probe | Get remote file size and type without downloading | none/glue | 0 | HEAD or ranged GET | no |
| 80 | download_resumable | Fetch a large file with resume and checksum | none/glue | 0 | aria2 or httpx ranged GET | no |
| 81 | hash_remote_file | Stream a URL and return SHA256 without saving it | none/glue | 0 | httpx stream with hashlib | no |
| 82 | jwt_decode | Decode a JWT header and claims and check expiry (no verify) | jwt.io | 0 | PyJWT decode without verification | no |
| 83 | base64_url_codec | Encode and decode base64, base64url, percent encoding | none/glue | 0 | Python stdlib | no |
| 84 | cors_check | Test whether a URL sends usable CORS headers | Test-CORS tools | 0 | OPTIONS preflight with custom origin | no |
| 85 | curl_convert | Turn a curl command into code and back | curlconverter site | 0 | curlconverter library | no |
| 86 | http_replay | Send a raw HTTP request and return the raw response | Postman, Hoppscotch | 0 to 14 | httpx or raw socket | no |
| 87 | webhook_catcher | Give a temp URL that records incoming requests | webhook.site, RequestBin Pro | 0 to 12 | Small FastAPI store with expiry | no |
| 88 | mock_endpoint | Serve a canned JSON response at a temp URL | Mocky, Beeceptor | 0 to 25 | Small FastAPI route table | no |
| 89 | tunnel_expose | Expose a local port on a public URL for a while | ngrok, Cloudflare Quick Tunnel | 0 to 20 | cloudflared quick tunnel or frp | no |
| 90 | qr_generate | Make a QR code from a URL or text | QR Code Generator Pro | 0 to 15 | python qrcode or segno | no |
| 91 | qr_decode | Read a QR or barcode from an image | Scanova, QR decoders | 0 to 10 | zxing-cpp or pyzbar | no |
| 92 | link_shorten | Shorten a URL on the own domain | Bitly, Rebrandly | 8 to 35 | Existing ktsn.lol shortener or YOURLS | no |
| 93 | http_status_explain | Explain an HTTP status code or header in plain words | none/glue | 0 | Local MDN-derived table | no |
| 94 | mime_lookup | Map extension to MIME type and back | none/glue | 0 | Python mimetypes plus mime-db | no |
| 95 | cron_explain | Explain a cron expression and give next run times | Crontab.guru style tools | 0 | cron-descriptor and croniter | no |
| 96 | timezone_convert | Convert a time between zones with DST awareness | WorldTimeBuddy Pro | 0 to 5 | zoneinfo | no |
| 97 | cidr_calc | Subnet math: range, mask, contains, split | none/glue | 0 | Python ipaddress | no |
| 98 | mac_vendor | Map a MAC address to its vendor | macvendors API | 0 to 10 | IEEE OUI database | no |
| 99 | whois_ip_owner | Find the org and abuse contact that owns an IP | ARIN and RIPE lookups, IPinfo | 0 to 99 | RDAP IP lookup | no |
| 100 | search_operator_build | Build and run a dork-style search across a site | Google Programmable Search, SerpAPI | 0 to 75 | SearXNG instance with site operators | no |

## Top 12 must-haves

1. url_expand
2. html_to_markdown
3. screenshot_url
4. og_unfurl
5. page_links
6. cms_detect
7. dns_records_all
8. redirect_chain
9. robots_check
10. render_html
11. tls_cert_info
12. broken_links

## Merge note

Merged near-duplicates: whois and RDAP domain lookups into one (#16), Wayback read and save kept separate on purpose (#41, #42), header dump and status checking folded into #11 and #12, Lighthouse and Core Web Vitals kept apart because one is lab and one is field data, DNS record types folded into #17, and the several URL-safety lookups collapsed into #75 and #76.
