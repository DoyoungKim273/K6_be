first_name = "eric"
last_name = "brown"
nickname = "    simson    "
simple_url = "https://github.com/DoyoungKim273/K6_be_vs"

print(f"Hello, {first_name.title()} {last_name.title()}.")
print(f"Hello, {first_name.upper()} {last_name.lower()}.")
print(f"Hey, {nickname.strip()}.")
print(simple_url.removeprefix('https://'))