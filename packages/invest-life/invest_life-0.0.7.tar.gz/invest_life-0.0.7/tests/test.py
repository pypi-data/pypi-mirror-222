# -*- coding: utf-8 -*-

from investlife import set_token,get_stock_list
set_token(token = 'xxxxxxxxxxxxxxxxxx')
data = get_stock_list(listed_state = "1")
print(data.head())