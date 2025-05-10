import requests

def test_el_injection(url, param):
    # Payload EL Injection sederhana yang menghasilkan angka 49 (7*7)
    payload = "${7*7}"
    params = {param: payload}
    
    response = requests.get(url, params=params)
    
    if "49" in response.text:
        print(f"[+] Possible EL Injection vulnerability detected at {url} with parameter '{param}'")
    else:
        print(f"[-] No EL Injection detected at {url} with parameter '{param}'")

# Contoh penggunaan
target_url = "http://targetsite.com/vulnerable_page"
parameter_name = "input"

test_el_injection(target_url, parameter_name)