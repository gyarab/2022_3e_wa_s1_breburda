import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
res = httpx.get(url)
rows = res.text.split("\n")

rows = rows[2:-1]

data = {}

for r in rows:
    cols = r.split("|")
    curr = cols[-2]
    rate = cols[-1]
    rate = rate.replace(",", ".")
    rate = float(rate)
    x = [rate,float(cols[-3])]
    data[curr] = x

code = input("Zadejte kód cílové měny:")

if(code == "CZK"):
    code_t = input("Zadejte kód výchozí měny:")
    user_amount = input(f"Zadej částku v {code_t}: ")
    user_amount = float(user_amount)   
    x = data[code_t]
    result = (user_amount * x[0])/x[1]
    result = round(result, 2)
else:
    user_amount = input(f"Zadej částku v CZK : ")
    user_amount = float(user_amount)   
    x = data[code]
    result = (user_amount / x[0])*x[1]
    result = round(result, 2)
   

print(f"Vysledna castka je {result} {code}")