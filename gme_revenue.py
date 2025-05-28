import pandas as pd

gme_revenue_list = []
table = soup_2.find_all("tbody")[1]
for row in table.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip()
        gme_revenue_list.append({"Date": date, "Revenue": revenue})
gme_revenue = pd.DataFrame(gme_revenue_list)
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(',|\$', '', regex=True)
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]
print(gme_revenue.tail())
