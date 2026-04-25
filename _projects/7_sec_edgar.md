---
layout: page
title: SEC EDGAR 13F Holdings Pipeline
description: Pure Python (stdlib only) pipeline for fetching, parsing, and storing SEC EDGAR 13F institutional holdings filings into a SQLite database. No third-party dependencies.
img: assets/img/projects/sec_edgar.png
importance: 4
category: mlops
tags: [Python, SQLite, SEC EDGAR, Data Engineering]
github: https://github.com/mohcinemadkour
---

## Overview

A **zero-dependency Python pipeline** for institutional holdings data from SEC EDGAR. Fetches 13F filings, parses XML, and stores structured holdings data in SQLite — using only Python's standard library.

## Features

- Fetches 13F-HR filings from SEC EDGAR full-text search API
- Parses XML holdings data (issuer, CUSIP, value, shares, investment discretion)
- Stores to SQLite with proper schema and indexes
- Rate-limit compliant with SEC EDGAR fair access policy
- No pip installs required — pure `urllib`, `xml.etree`, `sqlite3`

## Use Cases

- Quantitative research on institutional positioning
- Building signal features from smart money flows
- Portfolio overlap analysis
- Historical holdings trend analysis

## Tech Stack

`Python stdlib` · `SQLite` · `SEC EDGAR API` · `XML parsing`
