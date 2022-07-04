from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class TradeDetails(Base):
    __tablename__ = "trade_details"

    id = Column(Integer, primary_key=True, index=True)
    buySellIndicator = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    
    trades = relationship("Trade", back_populates='trade_details')


class Trade(Base):
    __tablename__ = "trades"

    trade_id = Column(String, primary_key=True, index=True)
    trader = Column(String)
    asset_class = Column(String)
    counterparty = Column(String)
    instrument_id = Column(Integer)
    instrument_name = Column(String)
    trade_date_time = Column(DateTime)
    trade_details_id = Column(Integer, ForeignKey("trade_details.id"))

    trade_details = relationship("TradeDetails", back_populates='trades')
