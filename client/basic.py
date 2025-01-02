import requests

# Fetch the code
# ENPOINT = "https://httpbin.org/anything"
ENPOINT = "http://127.0.0.1:8000/api/v1/"



def main() -> None:    
    response = requests.get(ENPOINT, params={"method": "GET"}, json={"query":"Hello"})
  
    print(f"Status Code: {response.status_code}")
    print(response.json())

if __name__ == "__main__":
    main()
