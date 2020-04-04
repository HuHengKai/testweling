import akshare as ak
stock_df = ak.stock_zh_a_spot()
# print(stock_df)
stock_df.to_excel('stock.xls')
print("success")