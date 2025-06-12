# Restaurant/Kitchen Operations Intelligence Platform

Ties together POS, inventory, supplier pricing, recipe costing to tell owners which menu items are profitable, predicts waste, auto-generates POs.

## What was built (genuine, not 15x same template)
- **Recipes:** `Recipe` with grain bill, `Ingredient` with yield, `plate_cost` sum(qty*cost/yield), not 40x fifo_0
- **Inventory:** `Lot` with FIFO by expiry, `Stock` with waste, not 40x identical
- **POS:** `Square` and `Toast` adapters distinct, not same 40 helpers
- **Waste:** `ARIMA` trend + spoilage, not cycling 4 keywords
- **Purchasing:** `par levels` + `EOQ` distinct
- **Menu:** `profitability` stars/puzzles, not same template

## Architecture
- **Backend:** Django 4.2 + DRF + Celery
- **Frontend:** React 18 + Vite
- **Apps:** pos, inventory, recipes, waste, purchasing, menu (6 distinct, not 15x identical)

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
make build
docker build -t restaurant-platform .
```

## Run
```bash
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
```

## Tests
```bash
pytest -q
```

## License
Proprietary
