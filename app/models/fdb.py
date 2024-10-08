from typing import List
from datetime import datetime
from pydantic import BaseModel, Field


class Genre(BaseModel):
    Name: str
    GenreCode: str


class TicketType(BaseModel):
    Name: str
    Seats: List[str]


class ScreenDetails(BaseModel):
    Name: str
    ScreenId: int
    FiscalYear: str
    Capacity: int
    Rows: int
    Columns: int
    VerticalStart: str
    HorizontalStart: str
    DisableSeats: List[str]
    TicketType: List[TicketType]


class TheaterDetails(BaseModel):
    Screen: List[ScreenDetails]
    TheaterCode: str


class Tax(BaseModel):
    Title: str
    Rate: float
    Value: float
    Unit: int


class Charge(BaseModel):
    Title: str
    Rate: float
    Value: float
    Unit: int


class TicketDetails(BaseModel):
    TheaterName: str
    TheaterCode: str
    ScreenName: str
    ScreenId: int
    ShowTypeName: str
    ShowTypeId: int
    MovieName: str
    MovieCode: str
    FiscalYear: str
    ShowDateTime: str
    ShowId: int
    TicketPrintDateTime: str
    TicketTypeName: str
    TicketTypeId: int
    PaymentTypeName: str
    PaymentTypeId: int
    TicketCode: str
    SeatNumber: str
    TicketStatusName: str
    TicketStatusValue: int
    TicketNetPrice: float
    TicketPrice: float
    TicketTax: List[Tax]
    TicketCharge: List[Charge]
    DistributorCode: str
    DistributorCommissionValue: float
    IsRealTime: int


class TicketReturnDetails(BaseModel):
    TheaterCode: str
    FiscalYear: str
    ShowId: int
    ShowDateTime: datetime
    RefTicketCode: str
    TicketCancelledReason: str
    TicketCancelledDateTime: datetime
    TicketNetPrice: float
    TicketPrice: float
    TicketTax: List[Tax]
    TicketCharge: List[Charge]
    IsRealTime: int


class ShowDetails(BaseModel):
    TheaterCode: str
    FiscalYear: str
    ShowId: int
    ShowStatus: int
    ShowDateTime: str
    ShowAddedDateTime: str
    IsRealTime: int


class CancelShowDetails(BaseModel):
    TheaterCode: str
    FiscalYear: str
    ShowId: int
    ShowCancelledReason: str
    ShowCancelledDateTime: str
    IsRealTime: int
