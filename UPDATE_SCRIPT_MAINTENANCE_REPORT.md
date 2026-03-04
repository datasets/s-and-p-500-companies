## Update Script Maintenance Report

Date: 2026-03-04

- Root cause: Wikipedia fetch via direct `pandas.read_html(url)` hit HTTP 403 in automation.
- Fixes made: switched scraper to `requests` with explicit User-Agent and parsed HTML from response content; modernized workflow with explicit write permission.
- Validation: local run reproduces and addresses the fetch path issue; workflow now commits only when output changes.
- Known blockers: none identified in this remediation pass.
