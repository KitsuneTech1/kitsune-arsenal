# Long tail: 100 small text, data, parsing, encoding, math and formatting tools

Prices are approximate, from general knowledge, not web-checked. "Verified" means live-checked today; none were, so all say no. Most of these are free in open source and only cost money as bundled parts of paid dev-tool or API suites, so many prices are what a user pays for the cheapest plan that includes the feature.

| # | Tool | Does | Replaces | ~$/mo | Backend/method | Verified |
|---|------|------|----------|-------|----------------|----------|
| 1 | json_diff | Diff two JSON objects, output a patch | Diffchecker Pro | 9 | jsondiffpatch / python-jsonpatch | no |
| 2 | json_csv | JSON to CSV and back, flatten nested | ConvertCSV style APIs | 10 | pandas json_normalize | no |
| 3 | json_format | Pretty-print, minify, sort keys, fix trailing commas | JSON formatter pro extensions | 0 | jq, json5 | no |
| 4 | json_schema_validate | Validate JSON against a schema, list errors | Hosted schema validators | 15 | ajv / jsonschema | no |
| 5 | json_schema_infer | Infer a schema from sample JSON | quicktype paid tier | 10 | genson | no |
| 6 | json_query | Run jq or JSONPath on a document | none/glue | 0 | jq, jsonpath-ng | no |
| 7 | config_convert | Convert YAML, JSON, TOML, INI both ways | Online converter suites | 0 | PyYAML, tomli/tomli-w | no |
| 8 | xml_format | Pretty-print or minify XML, check well-formed | Oxygen-style editors | 10 | lxml | no |
| 9 | xml_json | XML to JSON and back | Altova MapForce-lite | 20 | xmltodict | no |
| 10 | xml_select | XPath or CSS selector extraction | Scraper API selector features | 0 | lxml, cssselect | no |
| 11 | csv_clean | Dedupe, trim, fix delimiters, normalize headers | Hosted data-prep tools | 20 | pandas, csvkit | no |
| 12 | csv_profile | Sniff types, nulls, uniques per column | Data profiling SaaS | 25 | ydata-profiling / csvstat | no |
| 13 | csv_to_sql | CSV to CREATE TABLE plus INSERTs | Import wizards | 0 | csvkit csvsql | no |
| 14 | sql_format | Pretty-print and minify SQL by dialect | SQL formatter Pro | 5 | sqlparse | no |
| 15 | sql_lint | Lint and auto-fix SQL style | Hosted SQL linters | 15 | sqlfluff | no |
| 16 | sql_transpile | Translate SQL between dialects | Paid migration helpers | 20 | sqlglot | no |
| 17 | md_to_html | Markdown to clean HTML | none/glue | 0 | markdown-it, cmark-gfm | no |
| 18 | html_to_md | HTML to Markdown | Web clipper add-ons | 0 | turndown / html2text | no |
| 19 | md_table | CSV or JSON to Markdown table and back | Table generators | 0 | tabulate, pandas | no |
| 20 | doc_convert | Convert between docx, md, html, rst, epub, tex | CloudConvert doc tier | 10 | pandoc | no |
| 21 | html_sanitize | Strip scripts and unsafe attributes from HTML | Hosted sanitizer APIs | 10 | bleach / DOMPurify | no |
| 22 | html_to_text | Strip HTML to plain text with structure | Text extraction APIs | 10 | trafilatura, html2text | no |
| 23 | article_extract | Pull main article body, title, byline | Diffbot / Mercury Parser API | 30 | readability-lxml, trafilatura | no |
| 24 | formula_from_text | Excel or Sheets formula from a plain description | Formula Bot | 20 | LLM plus formulas lib test eval | no |
| 25 | formula_explain | Explain a spreadsheet formula step by step | ExcelFormulaBot | 10 | Formula parser plus LLM | no |
| 26 | xlsx_extract | XLSX or ODS sheets to CSV or JSON | Zamzar-style converters | 10 | openpyxl, odfpy | no |
| 27 | regex_test | Test a regex, show matches and groups | regex101 style tools | 0 | Python re, regex, JS RegExp | no |
| 28 | regex_from_examples | Build a regex from match and non-match samples | Regex generators | 10 | LLM plus test loop | no |
| 29 | regex_explain | Explain a regex in plain English | Regexper-style tools | 0 | sre_parse plus LLM | no |
| 30 | cron_explain | Cron expression to plain English | Crontab helper APIs | 0 | cronstrue | no |
| 31 | cron_next | Next N run times with timezone | Cron monitor SaaS | 10 | croniter | no |
| 32 | cron_from_text | "Every weekday 9am" to cron | Scheduling assistants | 0 | dateparser rules plus LLM | no |
| 33 | text_diff | Word or line diff of two texts, HTML or unified | Diffchecker Pro | 9 | difflib, diff-match-patch | no |
| 34 | text_merge | Three-way merge with conflict markers | Merge tool subscriptions | 0 | git merge-file | no |
| 35 | patch_apply | Apply a unified diff to text | none/glue | 0 | patch, unidiff | no |
| 36 | fuzzy_match | Rank closest strings to a query | Fuzzy match add-ons | 10 | rapidfuzz | no |
| 37 | text_similarity | Similarity score between two texts | Plagiarism-lite APIs | 15 | rapidfuzz, TF-IDF cosine | no |
| 38 | near_dupes | Find near-duplicate docs in a list | Dedupe SaaS | 25 | datasketch MinHash | no |
| 39 | slugify | Text to URL slug, any script | none/glue | 0 | python-slugify | no |
| 40 | case_convert | camel, snake, kebab, title, sentence case | Case converter sites | 0 | inflection, custom | no |
| 41 | encoding_detect | Detect text encoding with confidence | none/glue | 0 | charset-normalizer | no |
| 42 | mojibake_fix | Repair garbled text | none/glue | 0 | ftfy | no |
| 43 | strip_accents | Transliterate to ASCII, normalize Unicode | none/glue | 0 | unidecode, unicodedata | no |
| 44 | unicode_inspect | Show code points, names, categories, homoglyph flags | Unicode lookup sites | 0 | unicodedata, confusables | no |
| 45 | base64 | Encode and decode base64 and base64url | none/glue | 0 | stdlib base64 | no |
| 46 | hex_bin | Hex, binary, octal, bytes conversions | none/glue | 0 | stdlib binascii | no |
| 47 | url_codec | URL encode, decode, parse into parts, build query | none/glue | 0 | urllib.parse | no |
| 48 | html_entities | Encode and decode HTML entities | none/glue | 0 | html.entities | no |
| 49 | jwt_decode | Decode JWT header and claims, check expiry (no key needed) | jwt.io debugger | 0 | PyJWT decode without verify | no |
| 50 | punycode | IDN to punycode and back | Domain tools | 0 | idna | no |
| 51 | hash_text | MD5, SHA family, BLAKE of text or file | none/glue | 0 | hashlib | no |
| 52 | hmac_sign | HMAC sign and verify | none/glue | 0 | hmac | no |
| 53 | checksum | CRC32, Adler, xxHash | none/glue | 0 | zlib, xxhash | no |
| 54 | uuid_ulid | Generate and parse UUID v1/4/5/7, ULID, KSUID | none/glue | 0 | uuid, python-ulid | no |
| 55 | random_string | Random tokens, passwords, hex strings | Password generator apps | 3 | secrets | no |
| 56 | passphrase | Diceware-style passphrases | Password manager generators | 3 | EFF wordlist | no |
| 57 | password_strength | Estimate crack time, flag weak patterns | Password checkers | 0 | zxcvbn | no |
| 58 | qr_generate | Text, URL, WiFi, vCard to QR PNG or SVG | QR Code Generator Pro | 8 | qrcode, segno | no |
| 59 | qr_decode | Read QR or barcode from an image | QR scan APIs | 10 | zbar / pyzbar | no |
| 60 | barcode_generate | Code128, EAN, UPC, DataMatrix images | Barcode generator SaaS | 10 | python-barcode, treepoem | no |
| 61 | token_count | Count tokens for an LLM and estimate cost | Token counter sites | 0 | tiktoken, tokenizer libs | no |
| 62 | text_stats | Word, sentence, char count, reading time | Word counter tools | 0 | textstat | no |
| 63 | readability_score | Flesch, Gunning fog, grade level | Hemingway, Grammarly tier | 12 | textstat | no |
| 64 | language_detect | Detect language of a text | Language detection APIs | 10 | lingua-py, fastText | no |
| 65 | extract_entities | Pull emails, URLs, phones, IPs, hashtags from text | Extractor tools | 10 | regex, urlextract | no |
| 66 | phone_parse | Parse, validate, format phone numbers by region | Phone lookup APIs | 5 | phonenumbers | no |
| 67 | email_validate | Syntax and MX check, no sending | ZeroBounce-lite | 20 | email-validator | no |
| 68 | dates_from_text | Extract dates and times from prose | Text analytics APIs | 15 | dateparser, dateutil | no |
| 69 | date_parse | Natural language to ISO date ("next Friday") | Scheduling assistants | 0 | dateparser | no |
| 70 | tz_convert | Convert time between zones, meeting overlap finder | World Time Buddy Pro | 5 | zoneinfo | no |
| 71 | date_math | Add or diff dates, business days, holidays | Date calculators | 0 | dateutil, python-holidays | no |
| 72 | unix_time | Epoch to date and back, seconds or ms | none/glue | 0 | datetime | no |
| 73 | duration_parse | "2h 15m" to seconds and humanized back | none/glue | 0 | pytimeparse, humanize | no |
| 74 | unit_convert | Length, mass, temp, volume, data sizes | Unit conversion apps | 0 | pint | no |
| 75 | locale_format | Format numbers, currency, dates by locale | i18n formatting APIs | 0 | babel | no |
| 76 | number_to_words | 1234 to words, many languages | Check-writing tools | 0 | num2words | no |
| 77 | roman_numerals | Roman numeral conversion both ways | none/glue | 0 | roman lib / custom | no |
| 78 | base_convert | Convert numbers between bases 2 to 36 | none/glue | 0 | stdlib int | no |
| 79 | math_eval | Safe arithmetic expression evaluation | Wolfram Alpha Pro basic calc | 7 | asteval, sympy | no |
| 80 | algebra_solve | Solve equations, simplify, differentiate, integrate | Wolfram Alpha Pro | 7 | sympy | no |
| 81 | stats_summary | Mean, median, std, percentiles, correlation | Stats calculators | 0 | numpy, pandas | no |
| 82 | finance_calc | Compound interest, NPV, IRR, CAGR | Finance calculator APIs | 5 | numpy-financial | no |
| 83 | loan_amortize | Amortization schedule from terms | Mortgage calculator apps | 0 | numpy-financial | no |
| 84 | matrix_ops | Matrix multiply, invert, eigen | MATLAB Online basic | 20 | numpy | no |
| 85 | number_theory | Primes, factors, gcd, lcm, modular math | none/glue | 0 | sympy.ntheory | no |
| 86 | iban_validate | Validate IBAN, parse bank and country | IBAN validation APIs | 20 | schwifty | no |
| 87 | card_luhn | Luhn check, card brand from BIN prefix | Card validation APIs | 0 | python-stdnum | no |
| 88 | ean_isbn | Validate and convert EAN, UPC, ISBN checksums | GS1 tools | 0 | python-stdnum | no |
| 89 | tax_id_validate | Validate VAT, EIN, national IDs by format | VAT validation APIs | 15 | python-stdnum | no |
| 90 | bic_lookup | Validate SWIFT/BIC, decode country and bank code | SWIFT lookup APIs | 10 | schwifty | no |
| 91 | address_parse | Split free-text address into fields | Address parsing APIs | 25 | libpostal | no |
| 92 | name_parse | Split full name into title, first, last, suffix | Name parsing APIs | 10 | nameparser | no |
| 93 | fake_data | Fake names, addresses, companies, cards (test) | Mockaroo Pro | 15 | Faker | no |
| 94 | lorem_ipsum | Placeholder text, words, paragraphs, other languages | Lorem generators | 0 | Faker, lorem-text | no |
| 95 | synthetic_dataset | Generate CSV or JSON with a given schema and row count | Mockaroo Pro | 15 | Faker, mimesis | no |
| 96 | color_convert | HEX, RGB, HSL, OKLCH conversion, contrast ratio | Color tools, contrast checkers | 0 | coloraide | no |
| 97 | semver_compare | Compare and sort versions, range satisfy | none/glue | 0 | semver, packaging | no |
| 98 | cidr_calc | Subnet math, IP in range, expand CIDR | Subnet calculator sites | 0 | ipaddress | no |
| 99 | user_agent_parse | Parse browser, OS, device from UA string | UA parsing APIs | 15 | ua-parser | no |
| 100 | template_render | Render Jinja or Mustache templates with data | Templating SaaS | 0 | jinja2, chevron | no |

## Near-dupes merged

- Base64, hex, URL, HTML entity encoders (45 to 48) could be one `encode_decode` tool with a mode flag; kept split for clear discovery, but implement on one shared codec module.
- 30, 31, 32 (cron explain, next runs, from text) share one cron library; ship as one server with three tools.
- 93, 94, 95 (fake data, lorem, synthetic dataset) share Faker.
- 86, 88, 89, 90 (IBAN, EAN/ISBN, tax ID, BIC) share the stdnum and schwifty stack.
- 17, 18, 20 (md to html, html to md, pandoc) overlap; keep pandoc as fallback.
- 82 and 83 (finance calc, amortization) could merge.

## Top 12 must-haves

1. token_count (61)
2. json_diff (1)
3. text_diff (33)
4. json_csv (2)
5. regex_test (27)
6. cron_explain (30)
7. encoding_detect plus mojibake_fix (41, 42)
8. extract_entities (65)
9. tz_convert (70)
10. unit_convert (74)
11. formula_from_text (24)
12. iban_validate plus card_luhn plus ean_isbn (86 to 88)
