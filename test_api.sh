curl \
  -d '{"text":"#covid19 new york"}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:5009/api/american || exit 1