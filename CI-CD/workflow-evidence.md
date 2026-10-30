# CI/CD Evidence – GitHub Actions Workflow

## Workflow: CI/CD
**File:** `.github/workflows/ci.yml`
**Repository:** https://github.com/aaryanbangale2306/xrwvm-fullstack_developer_capstone

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

| Job ID | Job Name | Status |
|---|---|---|
| `lint-python` | Lint Python Files | ✅ Success |
| `lint-javascript` | Lint JavaScript Files | ✅ Success |

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

### lint-python job
1. ✅ Checkout Repository
2. ✅ Set up Python 3.12
3. ✅ Install Python Linter (pip install flake8)
4. ✅ Lint Python Files → **0 errors** → Complete job: lint-python

### lint-javascript job
1. ✅ Checkout Repository
2. ✅ Set up Node.js 20
3. ✅ Install JavaScript Linter (npm install)
4. ✅ Lint JavaScript Files → **0 errors** → Complete job: lint-javascript

---

## Both Jobs: COMPLETED SUCCESSFULLY
