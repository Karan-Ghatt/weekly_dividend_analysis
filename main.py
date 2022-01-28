import pandas as pd
import numpy as np
from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si
import html5lib


t_return = []

def get_data(tickers):

    lst = []
    montly_return = []

    company_dict = {
        "WMT": "Wall-Mart",
        "KMB": "Kimberly-Klark",
        "MO": "Alteria Group",
        "WPC": "W.P. Carey Inc. REIT",
        "CSCO": "Cisco",
        "T": "AT&T Inc.",
        "BX": "Blackstone Group",
        "AAPL": "Apple",
        "CAT": "Caterpillar Inc.",
        "SPG": "Simon Property Group (REIT)",
        "PFE": "Pfizer",
        "JNJ": "Johnson & Johnson",
        "MMM": "3M",
        "TFSL": "TFS Financial Corporation ",
        "AVY": "Avery Dennison"



    }

    for tick in tickers:

        #print(tick)

        quote_table = si.get_quote_table(tick)
        dividend_data = quote_table["Forward Dividend & Yield"].split(" ")
        div_amount = (float(dividend_data[0]))

        #print(div_amount)


        dividend_data = quote_table["Forward Dividend & Yield"].split(" ")
        div_percent = (dividend_data[1])

        quote_price = quote_table["Quote Price"]
        tick_price = (round(quote_price, 2))

        my_div = round((100 / tick_price) * div_amount, 2)

        lst.append(company_dict[tick])
        lst.append(tick)
        lst.append(tick_price)
        lst.append(div_percent)
        lst.append(div_amount)
        lst.append(100)
        lst.append(my_div)
        montly_return.append(my_div)

    x = 0
    y = 7
    z = 0
    max_range = len(lst) / 7
    new_lst = []

    while z < max_range:
        new_lst.append(lst[x:y])
        x += 7
        y += 7
        z += 1
    columns = ["Name", "Ticker", "Current", "Div %", "Div/Share", "Invested", "Return"]

    pd.set_option('display.max_columns', None)

    dataFrame = pd.DataFrame(np.array(new_lst), columns=columns)

    sum_monthly_return = sum(montly_return)
    t_return.append(sum_monthly_return)
    m_return_prcnt = (sum_monthly_return/(len(tickers) * 100))*100

    print(dataFrame)
    print(f"Monthly return of {sum_monthly_return} at a {m_return_prcnt}%")



jan_ticks = ["WMT", "KMB", "MO", "WPC", "CSCO"]
feb_ticks = ["T", "BX", "AAPL", "CAT", "SPG"]
mar_ticks = ["PFE", "JNJ", "MMM", "TFSL", "AVY"]
apr_ticks = ["WMT", "KMB", "MO", "WPC", "CSCO"]
may_ticks = ["T", "BX", "AAPL", "CAT", "SPG"]
jun_ticks = ["WMT", "PFE", "JNJ", "MMM", "TFSL", "AVY"]
jul_ticks = ["KMB", "MO", "WPC", "CSCO"]
aug_ticks = ["T", "BX", "AAPL", "CAT", "SPG"]
sep_ticks = ["WMT", "PFE", "JNJ", "MMM", "TFSL", "AVY"]
oct_ticks = ["KMB", "MO", "WPC", "CSCO"]
nov_ticks = ["T", "BX", "AAPL", "CAT", "SPG"]
dec_ticks = ["PFE", "JNJ", "MMM", "TFSL", "AVY"]

get_data(jan_ticks)
get_data(feb_ticks)
get_data(mar_ticks)
get_data(apr_ticks)
get_data(may_ticks)
get_data(jun_ticks)
get_data(jul_ticks)
get_data(aug_ticks)
get_data(sep_ticks)
get_data(oct_ticks)
get_data(nov_ticks)
get_data(dec_ticks)

sum_t_return = sum(t_return)
sum_t_return_prcnt = (sum_t_return/(16*100)) * 100

print(f"A total return of {sum_t_return} at {sum_t_return_prcnt}%")







