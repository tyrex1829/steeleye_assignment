from fastapi import FastAPI,Depends
from . import schemas,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import Union


app= FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/addtrades')
def get_all_trades(request: Union[schemas.Trade,schemas.TradeDetails],db:Session = Depends(get_db)):
    new_trade = models.Trade(trader=request.trader, trade_details=request.trade_details, asset_class=request.asset_class, 
    counterparty=request.counterparty,
    instrument_id=request.instrument_id, instrument_name=request.instrument_name,  trade_date_time=request.trade_date_time)
    db.add(new_trade)
    db.commit()
    db.refresh(new_trade)
    return new_trade






  
     
