# respec-test-suite-scaffolding



```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python generate.py

```


```bash
python -m pytest --alluredir allure-results-pytest test_suites/pytest

```

```bash
npm install --save-dev allure-commandline
npm install --save-dev allure-mocha
npx mocha test_suites/mocha
npx allure serve -h 0.0.0.0 -p 8000 allure-results
```