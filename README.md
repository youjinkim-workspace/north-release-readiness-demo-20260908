# Lumen Export Service - Release Review Demo

A small executable Python application and a deliberately inconsistent release checklist.
All business data is synthetic. No customer data, production secrets or deployable infrastructure is included.

## Run locally
```sh
python -m unittest discover -s tests -v
python release_review.py
```

## What to inspect
- [Release checklist](release/checklist.json): two tasks are marked done by the fictional team.
- [Export timeout PR](../../pull/2): still open despite the completed checklist item.
- [Access-control PR](../../pull/4): unresolved release blocker.
- [Release notes PR](../../pull/6): merged documentation change, not deployment proof.

North reads the checklist and real PRs, shows evidence, asks for one review, and optionally writes a new Google Sheet.
Do not present a synthetic scenario as a customer outcome or a merged PR as a successful deployment.
