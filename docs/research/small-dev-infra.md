# Kitsune Gateway long tail: 100 small dev, infra, cloud, CI/CD, monitoring, API and database micro-tools

Prices are approximate, from general knowledge as of mid 2026, and were NOT web-verified. "Verified" means checked live in this pass: all rows are "no" (backend named from knowledge, not tested). Web-verify before quoting any price externally. "none/glue" means no paid product, just a convenience wrapper.

| # | Tool | Does | Replaces | ~$/mo | Backend/method | Verified |
|---|------|------|----------|-------|----------------|----------|
| 1 | gitignore_generate | Build a .gitignore for a list of languages, IDEs and OSes | gitignore.io / GitHub templates | 0 | github/gitignore templates, local merge | no |
| 2 | config_validate | Validate a YAML, JSON or TOML file and report line and column errors | none/glue (JSON/YAML linter sites) | 0 | PyYAML, tomllib, jsonschema | no |
| 3 | dockerfile_lint | Lint a Dockerfile for bad practice and security smells | Snyk Container basic, Docker Scout | 0-25 | hadolint | no |
| 4 | systemd_unit_generate | Generate a systemd service or timer unit from a command and options | none/glue | 0 | Template plus systemd-analyze verify | no |
| 5 | cron_next_runs | Preview the next N run times for a cron expression in a timezone | crontab.guru style sites | 0 | croniter | no |
| 6 | port_check | Check if a local or remote TCP port is open or free | none/glue | 0 | Python socket / nmap -p | no |
| 7 | ssh_keypair_generate | Generate an ed25519 SSH keypair with fingerprint, private key returned once | none/glue | 0 | ssh-keygen | no |
| 8 | jwt_decode | Decode and inspect a JWT header, claims and expiry without verifying | jwt.io (free) | 0 | PyJWT decode, no verify | no |
| 9 | jwt_verify | Verify a JWT signature against a secret or JWKS URL | Auth0 debugger | 0 | PyJWT, JWKS fetch | no |
| 10 | openapi_stub_from_url | Probe a URL or JSON response and emit an OpenAPI 3 stub | Stoplight / Postman API gen | 15-40 | genson plus templating | no |
| 11 | curl_to_code | Convert a curl command to Python, JS, Go or PHP snippets | Postman code gen | 0-14 | curlconverter | no |
| 12 | semver_tool | Bump, compare and range-match semantic versions | none/glue | 0 | python-semver / node-semver | no |
| 13 | password_generate | Generate strong passwords and passphrases with entropy estimate | 1Password / Bitwarden generator | 0-4 | secrets module, EFF wordlist, zxcvbn | no |
| 14 | shell_explain | Explain a shell command piece by piece | explainshell / Warp AI | 0-20 | explainshell corpus plus man pages | no |
| 15 | log_regex_generate | Build a regex or grok pattern from sample log lines | Datadog log pipelines builder | 15-30 | Grok patterns, python re, LLM assist | no |
| 16 | prom_alert_rule_generate | Generate a Prometheus alert rule from a plain-English condition | Grafana Cloud alert wizard | 0-50 | PromQL templates, promtool check | no |
| 17 | sql_explain_pretty | Prettify EXPLAIN / EXPLAIN ANALYZE output and flag slow nodes | pev2 hosted, Datadog DBM | 0-70 | pev2 logic, pgMustard-style rules | no |
| 18 | mock_rest_endpoint | Spin up a throwaway mock REST endpoint from a JSON example | Mockoon cloud, Beeceptor | 0-25 | json-server / Prism | no |
| 19 | webhook_inspector | Provide a temporary URL that captures and shows incoming requests | webhook.site, RequestBin | 0-9 | Small FastAPI catcher with TTL | no |
| 20 | fake_db_seed | Generate fake rows and SQL inserts for a table schema | Mockaroo | 0-60 | Faker, schema parser | no |
| 21 | env_diff | Diff two .env files by key, value masked | none/glue | 0 | python-dotenv plus set diff | no |
| 22 | env_example_generate | Make a .env.example from a .env with values stripped | none/glue | 0 | dotenv parser | no |
| 23 | dotenv_lint | Find duplicate keys, bad quoting and missing vars in .env | dotenv-linter | 0 | dotenv-linter | no |
| 24 | secret_scan | Scan a folder or text for leaked keys and tokens | GitGuardian, GitHub secret scanning | 0-25 | gitleaks / trufflehog | no |
| 25 | yaml_to_json | Convert between YAML, JSON, TOML and XML | none/glue | 0 | yq / python libs | no |
| 26 | json_query | Run jq or JSONPath queries on a document | none/glue | 0 | jq / jsonpath-ng | no |
| 27 | json_schema_infer | Infer a JSON Schema from sample documents | quicktype, Stoplight | 0-15 | genson | no |
| 28 | json_to_types | Generate TS, Go, Python or Rust types from JSON | quicktype paid tiers | 0-10 | quicktype | no |
| 29 | dockerfile_generate | Generate a Dockerfile for a detected stack with multi-stage build | Docker Init, Copilot | 0-10 | Templates per language | no |
| 30 | compose_lint | Validate and lint a docker-compose file | none/glue | 0 | docker compose config, dclint | no |
| 31 | compose_from_run | Convert a docker run command to compose YAML | composerize | 0 | composerize | no |
| 32 | k8s_manifest_lint | Lint Kubernetes YAML against schemas and best practice | Datree, Kubescape cloud | 0-30 | kubeconform, kube-linter | no |
| 33 | k8s_manifest_generate | Generate a Deployment, Service and Ingress from an image and port | Lens paid, Octopus | 0-25 | Templates plus kubeconform | no |
| 34 | helm_values_diff | Diff two Helm values files or rendered charts | none/glue | 0 | helm template plus dyff | no |
| 35 | terraform_fmt_validate | Format and validate Terraform snippets | Terraform Cloud basic | 0-20 | terraform/tofu fmt validate | no |
| 36 | terraform_plan_summary | Summarize a terraform plan JSON into adds, changes, destroys | Spacelift, env0 | 0-40 | terraform show -json, jq | no |
| 37 | iac_security_scan | Scan Terraform, CloudFormation and K8s files for misconfig | Snyk IaC, Prisma Cloud | 25-98 | checkov / trivy config | no |
| 38 | cloudformation_lint | Lint CloudFormation templates | none/glue | 0 | cfn-lint | no |
| 39 | iam_policy_lint | Lint an AWS IAM policy for wildcards and privilege escalation | AWS Access Analyzer paid checks | 0-10 | parliament / policy_sentry | no |
| 40 | iam_policy_generate | Generate a least-privilege IAM policy from a list of actions | Policy generator sites | 0 | policy_sentry | no |
| 41 | cidr_calc | Subnet math, overlap check and CIDR split | none/glue | 0 | ipaddress module | no |
| 42 | dns_lookup_all | Look up A, AAAA, MX, TXT, NS and CAA records with propagation compare | DNSChecker, whatsmydns | 0-10 | dnspython, multiple resolvers | no |
| 43 | ssl_cert_check | Check cert expiry, chain and SANs for a host | SSL Labs, UptimeRobot SSL | 0-8 | openssl s_client, cryptography | no |
| 44 | ssl_cert_generate | Make a self-signed or local CA cert with SANs | mkcert (free) | 0 | openssl / cryptography | no |
| 45 | csr_generate | Generate a CSR and key for a domain | none/glue | 0 | openssl req | no |
| 46 | http_headers_audit | Grade a site's security headers and CSP | securityheaders.com Pro | 0-10 | requests plus rule set | no |
| 47 | csp_generate | Build a Content-Security-Policy from a list of sources | none/glue | 0 | Template builder | no |
| 48 | cors_tester | Test CORS preflight and headers against a URL | none/glue | 0 | requests OPTIONS | no |
| 49 | http_status_explain | Explain an HTTP status code and typical fixes | none/glue | 0 | Static table | no |
| 50 | url_redirect_trace | Follow a redirect chain and show hops, codes and timing | Redirect Checker | 0 | requests history | no |
| 51 | uptime_probe | One-shot HTTP or TCP check with latency from this hub | Pingdom, UptimeRobot | 0-15 | httpx, socket | no |
| 52 | http_timing_breakdown | DNS, connect, TLS, TTFB timing breakdown for a URL | Catchpoint, WebPageTest basic | 0-30 | curl -w, pycurl | no |
| 53 | grafana_dashboard_generate | Generate a Grafana dashboard JSON for common exporters | Grafana Cloud templates | 0-50 | grafanalib templates | no |
| 54 | promql_explain | Explain a PromQL expression in words | Grafana AI assistant | 0-20 | promql-parser plus LLM | no |
| 55 | alertmanager_route_test | Test which receiver an alert label set would route to | none/glue | 0 | amtool config routes test | no |
| 56 | loki_logql_generate | Build a LogQL query from a description | Grafana Cloud | 0-50 | Templates, logcli | no |
| 57 | healthcheck_generate | Generate Docker, K8s or nginx healthcheck config for a service | none/glue | 0 | Templates | no |
| 58 | nginx_conf_generate | Generate nginx reverse proxy, TLS and cache config | Nginx Config generators | 0 | Templates plus nginx -t | no |
| 59 | nginx_conf_lint | Lint nginx config for common mistakes | none/glue | 0 | gixy | no |
| 60 | caddyfile_generate | Generate and validate a Caddyfile | none/glue | 0 | caddy validate | no |
| 61 | logrotate_generate | Generate a logrotate config for a path | none/glue | 0 | Templates plus logrotate -d | no |
| 62 | github_actions_generate | Generate a GitHub Actions workflow for build, test, deploy | Copilot workflow help | 0-10 | Templates per stack | no |
| 63 | github_actions_lint | Lint workflow files and pin action versions | Datree, StepSecurity | 0-30 | actionlint, zizmor | no |
| 64 | gitlab_ci_lint | Validate .gitlab-ci.yml locally | GitLab CI Lint (needs instance) | 0 | gitlab-ci-local, schema | no |
| 65 | ci_config_convert | Convert CI config between GitHub Actions, GitLab CI and Drone | Vendor migration services | 0-50 | Mapping rules | no |
| 66 | commit_message_lint | Check commit messages against Conventional Commits | none/glue | 0 | commitlint | no |
| 67 | commit_message_generate | Write a commit message from a diff | Copilot, GitKraken AI | 0-10 | git diff plus LLM | no |
| 68 | changelog_from_commits | Build a changelog from git history | Release Drafter, LaunchNotes | 0-20 | git-cliff | no |
| 69 | git_command_explain | Explain or fix a git situation and suggest the safe command | Warp AI, GitKraken | 0-20 | Rules plus LLM | no |
| 70 | license_detect | Detect the license of a repo or dependency list | FOSSA, Snyk license | 0-99 | scancode-toolkit / licensee | no |
| 71 | license_compat_check | Check if a set of licenses are compatible | FOSSA | 0-99 | Compat matrix, licensee | no |
| 72 | sbom_generate | Generate a CycloneDX or SPDX SBOM for a project or image | Anchore Enterprise, Snyk | 0-100 | syft | no |
| 73 | dependency_vuln_scan | Scan lockfiles for known vulnerabilities | Snyk, Dependabot alerts | 0-25 | osv-scanner / grype | no |
| 74 | outdated_deps_report | List outdated dependencies with semver gap | Renovate paid, Snyk | 0-10 | npm outdated, pip list -o | no |
| 75 | package_lookup | Get latest version, license and deprecation for a package | libraries.io API | 0-10 | PyPI, npm, crates JSON APIs | no |
| 76 | readme_generate | Generate a README skeleton from a repo tree | Copilot Workspace | 0-10 | Repo scan plus template | no |
| 77 | openapi_lint | Lint an OpenAPI spec for style and errors | Stoplight Spectral cloud | 0-40 | spectral / vacuum | no |
| 78 | openapi_diff | Detect breaking changes between two OpenAPI specs | Bump.sh, Optic | 0-149 | oasdiff | no |
| 79 | openapi_to_client | Generate a client snippet or SDK stub from a spec | Fern, Speakeasy | 0-250 | openapi-generator | no |
| 80 | api_request_replay | Save and replay an HTTP request with variable substitution | Postman, Insomnia sync | 0-19 | httpx plus JSON store | no |
| 81 | graphql_query_generate | Build a query from a schema introspection URL | Apollo Studio | 0-49 | graphql-core introspection | no |
| 82 | graphql_schema_lint | Lint a GraphQL schema | Apollo checks | 0-49 | graphql-schema-linter | no |
| 83 | http_echo | Echo back headers, IP, user agent and body of any request | httpbin (free), Beeceptor | 0-9 | Small FastAPI echo | no |
| 84 | rate_limit_probe | Detect rate limit headers and safe request rate of an API | none/glue | 0 | httpx, header parse | no |
| 85 | cron_generate | Turn plain English into a cron expression | crontab.guru | 0 | Rule parser, croniter verify | no |
| 86 | timezone_convert | Convert times across zones and show DST changes for a schedule | World Time Buddy | 0-5 | zoneinfo | no |
| 87 | unix_timestamp_tool | Convert epoch, ISO 8601 and human dates | epochconverter | 0 | datetime | no |
| 88 | sql_format | Format and lint SQL for a dialect | SQLFluff cloud, Redgate | 0-30 | sqlfluff / sqlglot | no |
| 89 | sql_dialect_convert | Transpile SQL between Postgres, MySQL, SQLite, BigQuery | Vendor migration tools | 0-50 | sqlglot | no |
| 90 | sql_from_english | Draft a SQL query from a schema and plain-English ask, read-only | Text2SQL SaaS, Seek AI | 0-50 | Schema introspection plus LLM plus EXPLAIN check | no |
| 91 | schema_diff | Diff two database schemas and output migration SQL | Redgate, Liquibase Pro | 0-100 | migra / atlas | no |
| 92 | erd_generate | Draw an ERD from a schema or live DB | dbdiagram Pro, DBeaver Pro | 0-9 | SchemaSpy / mermaid-erd | no |
| 93 | db_index_advisor | Suggest missing indexes from slow query text and EXPLAIN | Datadog DBM, pganalyze | 0-150 | dexter / pg hypopg | no |
| 94 | db_size_report | Report table and index sizes for Postgres, MySQL, SQLite | pganalyze basic | 0-50 | Catalog queries | no |
| 95 | db_connection_string | Build and parse connection strings for common databases | none/glue | 0 | urllib plus templates | no |
| 96 | redis_key_inspect | Scan Redis keys by pattern with type, TTL and size | RedisInsight (free), Redis Cloud tools | 0 | redis-py SCAN | no |
| 97 | backup_script_generate | Generate a pg_dump or mysqldump backup script with rotation | Managed backup add-ons | 0-20 | Templates, restic/cron | no |
| 98 | connection_pool_calc | Size a connection pool and max_connections from cores and load | none/glue | 0 | Formulas (PgBouncer guidance) | no |
| 99 | ip_geo_asn_lookup | Look up geo, ASN and reverse DNS of an IP | ipinfo Pro, MaxMind | 0-99 | MaxMind GeoLite2 offline, whois | no |
| 100 | robots_sitemap_check | Validate robots.txt and sitemap.xml and list blocked paths | Screaming Frog, Ahrefs audits | 0-259 | protego, sitemap parser | no |

## Near-dupes merged

- jwt_decode (8) and jwt_verify (9) stay separate but ship as one "jwt" tool with a verify flag.
- cron_next_runs (5) and cron_generate (85) ship as one "cron" tool with two modes.
- env_diff (21), env_example_generate (22), dotenv_lint (23) ship as one "env" tool with three actions.
- dockerfile_lint (3), compose_lint (30), k8s_manifest_lint (32), iac_security_scan (37), cloudformation_lint (38) can share one "lint_config" front door that routes by file type.
- openapi_lint (77), openapi_diff (78) fold into one "openapi" tool.
- dns_lookup_all (42), ssl_cert_check (43), http_headers_audit (46) fold into a "site_health" tool if a single call is preferred.
- sbom_generate (72) and dependency_vuln_scan (73) share the same syft/grype pipeline.
- uptime_probe (51) and http_timing_breakdown (52) share one curl backend.

## Top 12 must-haves

1. config_validate (YAML/JSON/TOML validation)
2. secret_scan (leaked key and token scan)
3. dockerfile_lint plus the shared lint_config front door
4. jwt_decode / jwt_verify
5. cron (next runs and English to cron)
6. webhook_inspector
7. dependency_vuln_scan (osv-scanner)
8. curl_to_code
9. ssl_cert_check
10. sql_explain_pretty
11. env diff (env_diff, example, lint)
12. github_actions_lint
