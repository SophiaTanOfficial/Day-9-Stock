import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://student:PqyqrY2aEC22B5SB@cluster0-ya1yr.mongodb.net/stock-prices?retryWrites=true")
db = client['stock-prices'] #Make sure to replace this with the name of the database!
collection = db.prices

# write your queries here

stocks = list(collection.find({}))

# for each in stocks:

# stocks = list(collection.find({"symbol":"MSFT"}))
# print(stocks)


# stocks = list(collection.find({"year":2004}))
# print(stocks)
        
        
# stocks = list(collection.find({"month":"Sep"}))
# print(stocks)

# stocks = list(collection.find({"month":"Sep", "year":2004}))
# print(stocks)

# stocks = list(collection.find().sort("price", pymongo.ASCENDING))
# print(stocks)

# stocks = list(collection.find().sort("price", pymongo.DESCENDING))
# print(stocks)

# for stock in stocks:
#     stocks = list(collection.find().limit(5))

# print(stocks)

# stocks = list(collection.find({"price":100.52}))
# print(stocks)

# for each in stocks:
#     stocks = collection.count()
    
# print(stocks)

# stocks = list(collection.find({"symbol":"AAPL"}).limit(10))
# print(stocks)

# stocks = list(collection.find({"month":"Jan","symbol":"IBM"}).sort("price",pymongo.ASCENDING))
# print(stocks)

highStock = []
for stock in stocks:
    if stock.price >200:
        highStock.append(stock)

print(highStock)
