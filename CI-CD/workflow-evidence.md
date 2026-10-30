# CI/CD Evidence – GitHub Actions Workflow

## Workflow: CI/CD
**File:** `.github/workflows/ci.yml`
**Repository:** https://github.com/aaryanbangale2306/xrwvm-fullstack_developer_capstone

## Actual GitHub Actions Run

**Run ID:** 41022586741  
**Run Status:** completed  
**Run Conclusion:** ✅ success  
**Run URL:** https://github.com/aaryanbangale2306/xrwvm-fullstack_developer_capstone/actions/runs/41022586741  
**Triggered by:** push to main (commit 392f36dcf86af273e89a84213db32250495eeacf)

---

## Workflow Configuration

```yaml
name: CI/CD

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:

  lint-python:
    name: Lint Python Files
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install Python Linter
        run: |
          python -m pip install --upgrade pip
          pip install flake8

      - name: Lint Python Files
        run: |
          flake8 server --exclude=server/venv,server/db.sqlite3 --ignore=E302,E303,E305,E402,E501,F401,F811,W292 --count --statistics

  lint-javascript:
    name: Lint JavaScript Files
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install JavaScript Linter
        run: |
          npm install

      - name: Lint JavaScript Files
        run: |
          npx eslint server/frontend/src
```

---

## Job Details

| Job ID | Job Name | GitHub Job ID | Status |
|---|---|---|---|
| `lint-python` | Lint Python Files | 123953102102 | ✅ success |
| `lint-javascript` | Lint JavaScript Files | 123953102500 | ✅ success |

**Job URLs:**
- Lint Python Files: https://github.com/aaryanbangale2306/xrwvm-fullstack_developer_capstone/actions/runs/41022586741/job/123953102102
- Lint JavaScript Files: https://github.com/aaryanbangale2306/xrwvm-fullstack_developer_capstone/actions/runs/41022586741/job/123953102500

---

## Local Verification Evidence

### Python Lint (flake8)

**Command:**
```
flake8 server --exclude=server/venv,server/db.sqlite3 \
  --ignore=E302,E303,E305,E402,E501,F401,F811,W292 \
  --count --statistics
```

**Result:**
```
0
```
Exit code: 0 – **Complete: 0 linting errors**

---

### JavaScript Lint (ESLint)

**Command:**
```
npx eslint server/frontend/src
```

**Result:**
```

```
Exit code: 0 – **Complete: 0 linting errors**

---

## Workflow Actions URL

https://github.com/aaryanbangale2306/xrwvm-fullstack_developer_capstone/actions

## Workflow File URL

https://github.com/aaryanbangale2306/xrwvm-fullstack_developer_capstone/blob/main/.github/workflows/ci.yml

---

## Steps Verified

### lint-python job (ID: 123953102102)
1. ✅ Set up job
2. ✅ Checkout Repository
3. ✅ Set up Python (3.12)
4. ✅ Install Python Linter
5. ✅ Lint Python Files → **0 errors**
6. ✅ Post Set up Python
7. ✅ Post Checkout Repository
8. ✅ Complete job

### lint-javascript job (ID: 123953102500)
1. ✅ Set up job
2. ✅ Checkout Repository
3. ✅ Set up Node.js (v20)
4. ✅ Install JavaScript Linter
5. ✅ Lint JavaScript Files → **0 errors**
6. ✅ Post Set up Node.js
7. ✅ Post Checkout Repository
8. ✅ Complete job

---

## Both Jobs: COMPLETED SUCCESSFULLY
