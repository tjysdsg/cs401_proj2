# curl \
#   -d '{"text":"#covid19 new york"}' \
#   -H "Content-Type: application/json" \
#   -X POST http://localhost:5009/api/american || exit 1

python client.py --ip='10.108.131.191' --text='#covid19 new york'