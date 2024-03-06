import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.common.exceptions import TimeoutException




def get_price(driver, item_code):
    url = f"https://oman.sharafdg.com/?q={item_code}&post_type=product"
    driver.get(url)
    
    try:
        price_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'price')))
        return price_element.text.strip()
    except TimeoutException:
        print("No price found for the given item code.")
        return 'No item found'


def get_prices(list_of_products):
    results = []
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    try:
        for item_code, competitor_item_code in list_of_products:
            item_price = get_price(driver, item_code)
            competitor_price = get_price(driver, competitor_item_code)
            print(f"Item Code: {item_code}, Price: {item_price}")
            print(f"Competitor Item Code: {competitor_item_code}, Price: {competitor_price}")

            percent_diff = calculate_percent_difference(item_price, competitor_price)

            results.append({
                "VIB": item_code,
                "Price": item_price,
                "Competitor Model": competitor_item_code,
                "Competitor Price": competitor_price,
                "Percent": percent_diff
            })

    except Exception as ex:
        print(ex)

    finally:
        driver.quit()
        return results

def calculate_percent_difference(item_price, competitor_price):
    if item_price == 'No item found' or competitor_price == 'No item found':
        return 'No percent'
    else:
        item_price = float(item_price.replace('OMR', '').replace(',', '').strip())
        competitor_price = float(competitor_price.replace('OMR', '').replace(',', '').strip())
        if competitor_price == item_price:
            return '0%'
        percent_diff = ((competitor_price - item_price) / item_price) * 100
        return f"{percent_diff:.3f}%"

if __name__ == "__main__":
    list_of_products = [["WGA142XVGC", "WW90T554DANGU"], ["WAJ2018SGC", "WW80TA046AXGU"],
                        ["SMS50E92GC", "DFN05310W"], ["SMS50D08GC", "DW60M5050FS/SG"],
                        ["KDN76XI30M", "RT81K7050SL"], ["KDN55NL20M", "RT81K7050SL"],
                        ["HGVDA0Q50M", "ATEC95C31XKR"], ["HGV1E0U50M", "GG15125GX"]]
    results = get_prices(list_of_products)
    df = pd.DataFrame(results)
    df = df[["VIB", "Price", "Competitor Model", "Competitor Price", "Percent"]]  # Reorder columns
    if os.path.exists('scraped_data.xlsx'):
        os.remove('scraped_data.xlsx')
    df.to_excel("scraped_data.xlsx", index=False)
