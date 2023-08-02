import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the price element from the Amazon product page
    price_element = soup.find("span", {"id": "priceblock_ourprice"} or {"id": "priceblock_dealprice"})
    
    if price_element:
        price = price_element.get_text().strip()
        return price
    else:
        return "Price not found."

def main():
    print("Amazon Price Checker")
    product_url = input("Enter the Amazon product URL: ")

    price = get_product_price(product_url)

    print("Current Price:", price)

if __name__ == "__main__":
    main()
