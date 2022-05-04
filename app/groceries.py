
# READ INVENTORY OF PRODUCTS

#products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
#products_df = read_csv(products_filepath)
#products = products_df.to_dict("records")

import os
import statistics
from pandas import read_csv



# to_usd function
"""
converts a number to currency format with usd sign and two decimal places

@param: number to be converted to currency format

examples:
    to_usd(546.55)

"""
def to_usd(my_price):
    return f"${my_price:,.2f}"


"""

gives the average value of a list or dataframe

@param: list or data frame to be averaged

examples: 
    avg_price(all_prices)

"""
def avg(csv):
    out = statistics.mean(csv)
    return out
    

# PRINTED INVENTORY REPORT
if __name__ == "__main__":
    # checks to see if a products.csv file exists. If not, it uses the default
    if os.path.isfile(os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")) == True:
        print("USING CUSTOM PRODUCTS CSV FILE...")
        csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
    else:
        print("USING DEFAULT PRODUCTS CSV FILE...")
        csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "default_products.csv")
    
    #reads the csv file into products variable
    products = read_csv(csv_filepath)
    #pandas transforms the data into a list of dictionaries
    products = products.to_dict('records')
    
    all_prices = []
    print("---------")
    print("THERE ARE", len(products), "PRODUCTS:")
    print("---------")
    
    for p in products:
        print("..." + p["name"] + " " + to_usd(p["price"]))
        all_prices.append(float(p["price"]))       
    
    avg_price = avg(all_prices)
    
    print("---------")
    print("AVERAGE PRICE:", to_usd(avg_price))










# EMAIL INVENTORY REPORT
