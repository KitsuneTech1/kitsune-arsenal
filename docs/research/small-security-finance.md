# Long-tail utilities: security, OSINT, privacy, crypto, finance and misc (100 tools)

Notes: prices are approximate and come from memory, not web checks (dated 2026-09-29). "Verified" means live-tested against the backend by us; nothing here has been yet, so every row is "no". Gray = needs a ToS or legality check before it ships. Keys marked "free key" are free-tier API keys.

| # | Tool | Does | Replaces | ~$/mo | Backend/method | Verified | Gray |
|---|------|------|----------|-------|----------------|----------|------|
| 1 | password_breach_check | Checks a password against breach corpora without sending it (k-anonymity) | 1Password Watchtower, breach monitors | 3 | HIBP Pwned Passwords range API (free, no key) | no | |
| 2 | totp_generate | Makes the current TOTP code from a base32 secret | Authy, Authenticator apps | 0 | pyotp (RFC 6238) | no | |
| 3 | totp_verify | Verifies a 6-digit code with a drift window | Auth0 MFA add-on | 0 | pyotp verify | no | |
| 4 | cert_expiry | Days left on a domain's TLS cert, plus issuer and SANs | UptimeRobot SSL monitor | 7 | Python ssl + cryptography | no | |
| 5 | tls_grade | Grades protocols, ciphers and known TLS flaws | Qualys SSL Labs-style paid scans | 10 | sslyze or testssl.sh | no | |
| 6 | cve_lookup | Finds CVEs by product, vendor or version | Vulners, Tenable feeds | 50 | NVD API 2.0, OpenCVE | no | |
| 7 | cve_priority | Adds EPSS score and CISA KEV flag to a CVE | Tenable VPR, Kenna | 100 | FIRST EPSS API, CISA KEV JSON | no | |
| 8 | defang_refang | Defangs or refangs URLs, IPs, emails | none/glue | 0 | ioc-fanger | no | |
| 9 | ioc_extract | Pulls IPs, domains, hashes, CVEs out of raw text | Threat-intel platform parsers | 30 | ioc-finder / iocextract | no | |
| 10 | hash_identify | Guesses hash type from a string | none/glue | 0 | name-that-hash | no | |
| 11 | malware_hash_lookup | Looks up a file hash in public malware corpora | VirusTotal premium lookups | 100 | abuse.ch MalwareBazaar API (free key) | no | |
| 12 | multi_hash | Computes MD5, SHA-1, SHA-256, SHA-3, BLAKE3 for text or a file | none/glue | 0 | hashlib, blake3 | no | |
| 13 | yara_scan | Runs YARA rules on a file or bytes | Commercial AV sandboxes | 50 | yara-python | no | |
| 14 | sigma_convert | Converts a Sigma rule to a SIEM query | Splunk/Elastic rule packs | 20 | pySigma | no | |
| 15 | security_headers_check | Scores HSTS, CSP, XFO and other response headers | SecurityHeaders.com Pro, Observatory | 10 | httpx + rules | no | |
| 16 | csp_evaluate | Flags weak Content-Security-Policy directives | Report URI style tools | 10 | csp-evaluator logic port | no | |
| 17 | secret_scan_text | Finds API keys and tokens in pasted text or a diff | GitGuardian | 18 | gitleaks rules, detect-secrets | no | |
| 18 | password_strength | Scores a password offline with crack-time estimate | password manager audits | 3 | zxcvbn | no | |
| 19 | passphrase_generate | Makes diceware or random passwords | password manager generators | 3 | EFF wordlist, secrets | no | |
| 20 | jwt_inspect | Decodes a JWT and flags alg none, expiry, weak claims | Auth debugger tools | 0 | pyjwt | no | |
| 21 | spf_dmarc_check | Validates SPF, DKIM selector, DMARC, MTA-STS | dmarcian, EasyDMARC | 20 | checkdmarc, dnspython | no | |
| 22 | dns_records | Full record dump for a domain, with DNSSEC status | DNSlytics, DNS Checker Pro | 10 | dnspython | no | |
| 23 | subdomain_passive | Passive subdomain list from cert logs and DNS datasets | SecurityTrails | 50 | crt.sh, subfinder passive sources | no | GRAY (passive only, respect scope) |
| 24 | port_check_owned | Checks open ports on hosts you own | Shodan Monitor, Detectify | 30 | nmap top-ports, allowlist-gated | no | GRAY (owned targets only) |
| 25 | ct_log_watch | Lists new certs issued for a domain | Cert Spotter paid, Facebook CT alerts | 20 | crt.sh, certstream | no | |
| 26 | url_blocklist_check | Checks a URL against public phishing and malware lists | Sucuri, URLVoid | 15 | Google Safe Browsing (free key), URLhaus, OpenPhish | no | |
| 27 | url_unshorten | Follows a redirect chain and shows each hop | Unshorten.it tools | 0 | httpx, no body fetch | no | |
| 28 | homoglyph_detect | Flags punycode and lookalike characters in domains | Brand protection suites | 100 | confusables, idna | no | |
| 29 | typosquat_generate | Generates likely typo domains and checks if registered | Bolster, ZeroFox | 200 | dnstwist | no | |
| 30 | ssh_key_audit | Fingerprints a public key and flags weak type or size | none/glue | 0 | ssh-keygen, paramiko | no | |
| 31 | age_encrypt | Encrypts or decrypts short text with age or PGP | Keybase, paid encrypt tools | 0 | age, python-gnupg | no | |
| 32 | email_header_trace | Parses email headers into a hop path with auth results | MxToolbox Pro | 129 | email stdlib | no | |
| 33 | whois_age | Domain registration age, expiry and registrar | WhoisXML API | 20 | RDAP via rdap.org, python-whois | no | |
| 34 | ip_geo_asn | IP to country, ASN and network owner | ipinfo, IPStack | 25 | MaxMind GeoLite2 (free key), RIPEstat | no | |
| 35 | ip_reputation | Checks an IP against public abuse lists | AbuseIPDB paid, Spamhaus | 25 | AbuseIPDB free tier, Tor exit list | no | |
| 36 | dnsbl_check | Checks an IP or domain against DNS blocklists | MxToolbox blacklist check | 129 | dnspython vs public DNSBLs | no | |
| 37 | reverse_dns_neighbors | Reverse DNS and shared-host hints for an IP | ViewDNS paid | 20 | PTR lookups, RIPEstat | no | |
| 38 | email_disposable | Flags disposable or throwaway email domains | Kickbox, ZeroBounce | 40 | disposable-email-domains list | no | |
| 39 | email_validate | Syntax and MX check without sending mail | NeverBounce | 30 | email-validator, dnspython | no | |
| 40 | email_breach_check | Says if an email appears in known breaches | HIBP subscription, Have I Been Pwned Pro | 4 | HIBP breachedaccount API (paid key) | no | GRAY (own addresses only) |
| 41 | username_footprint | Checks where a username exists across sites | Namechk Pro, social OSINT SaaS | 20 | maigret or sherlock | no | GRAY (ToS of sites, stalking risk) |
| 42 | github_footprint | Public repos, orgs, commit emails for a GitHub user | Social Links OSINT | 30 | GitHub REST API | no | GRAY (commit email exposure) |
| 43 | wayback_lookup | Finds archived snapshots of a URL | Archive-It | 0 | Wayback CDX API | no | |
| 44 | wayback_save | Requests an archive snapshot of a URL | Perma.cc | 10 | Save Page Now API | no | |
| 45 | exif_gps | Extracts EXIF fields and GPS from a photo | Jeffrey's EXIF paid, forensic suites | 0 | exiftool | no | |
| 46 | reverse_geocode | Coordinates to address and back | Google Geocoding | 10 | Nominatim (self-host) | no | |
| 47 | image_phash | Perceptual hash and near-duplicate check | TinEye API | 200 | imagehash | no | |
| 48 | sanctions_screen | Screens a name against public sanctions lists with fuzzy match | Dow Jones, ComplyAdvantage | 500 | OFAC SDN, EU, UN lists via OpenSanctions | no | GRAY (OpenSanctions license is non-commercial unless licensed; not legal compliance) |
| 49 | lei_lookup | Legal entity identifier lookup by name or LEI | Bloomberg/Refinitiv entity data | 100 | GLEIF API (free) | no | |
| 50 | company_registry | Company search across registries | OpenCorporates paid, D&B | 100 | OpenCorporates free tier, Companies House API | no | |
| 51 | sec_filing_search | Latest 10-K, 10-Q, 8-K, Form 4 for a company | Sec-api.io | 50 | SEC EDGAR APIs | no | |
| 52 | tech_stack_detect | Detects CMS, frameworks, CDN from a URL | BuiltWith, Wappalyzer | 250 | wappalyzer open fork, headers | no | |
| 53 | favicon_hash | Computes favicon hash for asset pivoting | Shodan favicon pivots | 0 | mmh3 | no | |
| 54 | asn_prefixes | Lists prefixes and peers for an ASN | BGP toolkit paid | 0 | RIPEstat, BGPView | no | |
| 55 | phone_parse | Validates and formats phone numbers, region and line type | Twilio Lookup | 5 | phonenumbers | no | |
| 56 | webfinger_lookup | Resolves a fediverse or WebFinger handle | none/glue | 0 | WebFinger RFC 7033 | no | |
| 57 | gravatar_lookup | Gets the public Gravatar profile for an email hash | Clearbit lite | 0 | Gravatar API | no | GRAY (links email to identity) |
| 58 | pdf_office_metadata | Extracts author, tool, dates from PDF and Office files | FOCA-like tools | 0 | exiftool, pypdf | no | |
| 59 | pii_redact_text | Redacts names, emails, SSNs, phones from text | Private AI, Nightfall | 100 | Microsoft Presidio | no | |
| 60 | pii_detect_file | Lists PII found in a file without changing it | Data classification suites | 100 | Presidio, regexes | no | |
| 61 | metadata_strip | Strips metadata from images, PDFs, Office files | Metadata cleaners | 5 | mat2, our strip script | no | |
| 62 | face_blur | Blurs faces in an image | Redact tools | 10 | OpenCV DNN, YuNet | no | |
| 63 | plate_blur | Blurs license plates in an image | Blur services | 10 | YOLO plate model, OpenCV | no | |
| 64 | url_param_clean | Strips tracking parameters from a URL | ClearURLs style extensions | 0 | ClearURLs rules JSON | no | |
| 65 | tracker_scan | Lists trackers and third-party calls on a page | Blacklight, Ghostery Insights | 20 | Playwright + Ghostery TrackerDB | no | |
| 66 | privacy_policy_summary | Summarises a privacy policy and flags risky clauses | ToS;DR Pro, Termly | 15 | LLM over fetched text | no | |
| 67 | email_alias_make | Creates a masked forwarding alias | SimpleLogin, Firefox Relay | 3 | SimpleLogin self-host | no | |
| 68 | dsar_letter | Drafts a GDPR or CCPA data request letter | Termly DSAR, DeleteMe letters | 10 | templates | no | |
| 69 | broker_optout_list | Returns data broker opt-out links by state | DeleteMe, Incogni | 10 | maintained public opt-out lists | no | GRAY (list accuracy, no submission on user behalf) |
| 70 | tor_exit_check | Says whether an IP is a Tor exit or known VPN range | IP intelligence feeds | 25 | Tor bulk exit list, X4BNet VPN lists | no | |
| 71 | one_time_secret | Creates a self-destructing shared secret link | OneTimeSecret Pro, 1Password sharing | 5 | Yopass or PrivateBin | no | |
| 72 | fingerprint_report | Shows what a browser fingerprint reveals | EFF Cover Your Tracks-style | 0 | CreepJS logic | no | |
| 73 | crypto_address_validate | Validates BTC, ETH, SOL, LTC, XMR, TRX address format and checksum | Block explorer API keys | 0 | multicoin address libs (bech32, base58, EIP-55) | no | |
| 74 | ens_resolve | ENS name to address and reverse | ENS app, Alchemy | 0 | web3 + public RPC | no | |
| 75 | gas_price_now | Current gas price and fee tiers on EVM chains | Etherscan gas API, Blocknative | 30 | eth_feeHistory via RPC | no | |
| 76 | btc_fee_estimate | Current Bitcoin fee tiers | mempool paid plans | 0 | mempool.space API (self-host optional) | no | |
| 77 | tx_status | Confirmation state of a transaction hash across chains | Etherscan Pro, Blockchair | 30 | RPC, ElectrumX | no | |
| 78 | token_metadata | Name, symbol, decimals, supply for a token contract | Moralis, Alchemy tokens | 50 | ERC-20 eth_call, Metaplex for SOL | no | |
| 79 | selector_decode | Decodes a 4-byte function selector or event topic | Tenderly signatures | 0 | openchain signatures, 4byte directory | no | |
| 80 | calldata_decode | Decodes tx calldata with a given or fetched ABI | Tenderly, Etherscan decode | 50 | eth_abi, Sourcify ABI | no | |
| 81 | contract_verified | Says if a contract has verified source and shows compiler | Etherscan Pro | 30 | Sourcify API | no | |
| 82 | token_rug_check | Honeypot, tax and owner-privilege flags for a token | Token Sniffer paid, De.Fi | 30 | GoPlus free API | no | GRAY (not advice, false negatives) |
| 83 | approval_check | Lists open ERC-20 approvals for an address | Revoke.cash Pro | 10 | eth_getLogs, Approval events | no | |
| 84 | sig_verify | Verifies an EIP-191 or Solana message signature | none/glue | 0 | eth_account, PyNaCl | no | |
| 85 | eth_unit_convert | Converts wei, gwei, ether, token decimals | none/glue | 0 | web3 utils | no | |
| 86 | mnemonic_validate | Validates BIP-39 checksum locally and never sends it anywhere | Wallet recovery tools | 0 | mnemonic lib, offline | no | GRAY (seed handling, keep offline, warn on real seeds) |
| 87 | xpub_derive | Derives receive addresses from an xpub | Wallet watch-only apps | 0 | bip_utils | no | |
| 88 | crypto_price | Spot price for a coin with source and timestamp | CoinGecko Pro, CoinMarketCap | 129 | Pyth, CoinGecko free tier | no | |
| 89 | defi_yield_lookup | TVL and APY for a pool or protocol | DeFiLlama Pro, Zapper | 50 | DefiLlama public API | no | |
| 90 | stablecoin_depeg | Shows stablecoin peg deviation now | Chainalysis-lite dashboards | 30 | DefiLlama stablecoins, Pyth | no | |
| 91 | ipfs_cid_validate | Validates a CID and fetches a gateway preview | Pinata gateway | 20 | multiformats, public gateways | no | |
| 92 | chain_address_sanction | Checks a crypto address against OFAC-listed addresses | Chainalysis Sanctions API, TRM | 200 | OFAC SDN digital currency fields | no | GRAY (not a compliance product) |
| 93 | crypto_tax_lots | Computes FIFO, LIFO, HIFO gains from a CSV of trades | Koinly, CoinTracking | 25 | pandas | no | GRAY (not tax advice) |
| 94 | iban_validate | Validates an IBAN and returns bank code parts | Iban.com API, Fintecture | 10 | schwifty, python-stdnum | no | |
| 95 | bic_lookup | SWIFT/BIC to bank and country | SWIFT ref data, Bank codes API | 20 | schwifty bank registry, GLEIF BIC-LEI map | no | |
| 96 | card_luhn_bin | Luhn check and card brand from BIN prefix, no real numbers stored | Binlist, Stripe radar bits | 10 | python-stdnum, iin ranges | no | GRAY (BIN dataset licenses, never handle real PANs) |
| 97 | vat_validate | Validates an EU VAT number and shows company name | Avalara VAT, Vatstack | 20 | EU VIES SOAP API | no | |
| 98 | ticker_resolve | Company name to ticker, ISIN, CUSIP, FIGI | Bloomberg lookup, Refinitiv | 100 | OpenFIGI API (free key), SEC company_tickers.json | no | |
| 99 | fx_convert | Currency conversion with historical dates | XE, Fixer paid | 10 | Frankfurter (ECB rates) | no | |
| 100 | loan_amortization | Loan, mortgage, tip, compound-interest and payoff schedules | Bankrate, Calculator.net apps | 0 | numpy-financial, plain math | no | |

## Near-dupes merged

- ioc_extract and defang_refang stay separate but share the ioc-finder library.
- totp_generate and totp_verify are two tools on one pyotp module; could ship as one with a mode flag.
- crypto_address_validate covers what would have been separate per-chain validators.
- fx_convert absorbs stock-currency and crypto-to-fiat conversion asks; crypto_price stays separate for on-chain sources.
- Sports and stock ticker resolve: ticker_resolve covers stocks only. Sports score lookups were dropped as GRAY (unofficial ESPN endpoints) and can be added later.
- AI-written text detection was left out on purpose. Best-effort detectors are unreliable and cause false accusations; if added, ship it flagged GRAY with a stated error rate.
- Barcode/QR decode and OCR were dropped from this list because the media domain agent is likely to cover them (pyzbar/zxing, tesseract). Flag for de-dupe against that list.

## Top 12 must-haves

1. password_breach_check
2. pii_redact_text
3. crypto_address_validate
4. cve_lookup (with cve_priority as an option)
5. url_blocklist_check
6. cert_expiry
7. email_disposable
8. gas_price_now
9. sanctions_screen (ship with the GRAY warning)
10. exif_gps
11. spf_dmarc_check
12. iban_validate
