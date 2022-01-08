from sqlalchemy import create_engine, Text
from scraper_logic import LastSale, BuyPrice, PriceAdjustment
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

with engine.connect as conn:
    conn.execute(Text("CREATE TABLE Shoe_data_table (Row_Id, Last_Sale_Value, Buy_Price_Value, Price_Recc_Value)"))
    conn.execute(
        Text("INSERT INTO Shoe_Data_Table (Row_Id, Last_Sale_Value, Buy_Price_Value, Price_Recc_Value) VALUES (LastSale, BuyPrice, PriceAdjustment)")
    )
    conn.commit()