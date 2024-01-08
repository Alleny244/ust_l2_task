import requests

url = "http://127.0.0.1:8118/graphql"
headers = {"content-type": "application/json"}
query = 'mutation {addCountryMutation(inputData: {name: "Allen",independent: true,currencies: [ { name: "US Dollar", code: "USD" }, { name:"Euro", code:"EUR" }],region: "Americas",capital: ["Washington D.C."],languages: [{ name: "English" },{ name: "Spanish" }],coordinates: [38, -77],area: 9833517,population: 331002651,continents: ["North America"]}) { country {  name }}}'
data = {"query": query}
response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
