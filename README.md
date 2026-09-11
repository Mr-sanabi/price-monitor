# Price Monitor

A Python 3.11+ script that reads a product price, compares it with the previous and target prices, and saves CSV history.

## Run

Copy `config_example.json` to `config.json` and set the product URL, CSS selectors, target price, and output paths.

```bash
python -m pip install -r requirements.txt
python -m src.main --config config.json
```

Keep `config.json` local. Selectors depend on the target page; this is not a universal price parser. Failed fetches preserve the last known price, and state files are replaced atomically.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
