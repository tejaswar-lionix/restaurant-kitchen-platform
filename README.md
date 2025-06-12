# Restaurant/Kitchen Operations Intelligence Platform

Ties together POS, inventory, supplier pricing, recipe costing to tell owners in real time which menu items are profitable, predicts waste, auto-generates POs.

## Architecture
- **Backend:** Django 4.2 + DRF + Celery + Redis, PostgreSQL (sqlite fallback)
- **Frontend:** React 18 + Vite + Chart.js
- **15 Apps:** pos, inventory, supplier, recipes, waste, purchasing, menu, forecasting, costing, integrations, compliance, analytics, api, frontend, reports

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
npm run build
```

## Run
```bash
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
celery -A kitchen worker -l info
npm run dev
docker-compose up
```

## Tests
```bash
pytest -q
pytest --cov=apps --cov-report=xml
npm test
```

## Features
- **POS adapters:** Square/Toast ticket ingestion, voids, comps
- **Recipe costing:** ingredient `yield 0.85`, `units g→kg`, `plate_cost = sum(qty*unit_cost/yield)`
- **Waste prediction:** `ARIMA` on covers + spoilage `3-day` trend
- **Auto POs:** `par 20, on_hand 5, on_order 0 → order 15` with `EOQ`
- **Menu engineering:** `stars/puzzles/plowhorses/dogs` via `profitability vs popularity`

## License
Proprietary — All rights reserved.
