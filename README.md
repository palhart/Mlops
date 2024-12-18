# Mlops

paul.hartmann
nicolas.schmitt


## Backend
- Example
```
curl -X 'POST' 'https://ml-ops-prokect.ew.r.appspot.com:8000/generate_meme' \
  -H 'Content-Type: application/json' \
  -d '{"user_input": "Hello"}' --output test.jpg
```

## Load Testing
```
locust -f load_testing/locustfile.py --host=https://ml-ops-prokect.ew.r.appspot.com
```