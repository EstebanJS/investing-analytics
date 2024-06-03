from models.base_model import BaseModel
from models.income_statement import IncomeStatement
from models.balance_sheet import BalanceSheet
from models.cash_flow import CashFlow

class CompanyInfo(BaseModel):

    def __init__(self, data = None):
        super().__init__(data)
        self.PtyCd = data.get("PtyCd")
        self.CompanyName = data.get("CompanyName")
        self.Country = data.get("Country")
        self.Currency = data.get("Currency")
        self.InstrumentPriceLast = data.get("InstrumentPriceLast")
        self.InstrumentPriceChange = data.get("InstrumentPriceChange")
        self.InstrumentPriceChangePercent = data.get("InstrumentPriceChangePercent")
        self.Bid_ask = data.get("Bid_ask")
        self.Volume = data.get("Volume")
        self.AvgVolume = data.get("AvgVolume")
        self.OneYearReturn = data.get("OneYearReturn")
        self.SharesOutstanding = data.get("SharesOutstanding")
        self.Revenue = data.get("Revenue")
        self.P_E_Ratio = data.get("P_E_Ratio")
        self.EPS = data.get("EPS")
        self.Dividend = data.get("Dividend")
        self.Dividend = data.get("Dividend")
        self.Beta = data.get("Beta")
        self.ISIN = data.get("ISIN")
        self.Profile = data.get("Profile")
        self.Industry = data.get("Industry")
        self.Sector = data.get("Sector")
        self.Market = data.get("Market")
        
        self.IncomenStatments = [IncomeStatement(IncSta) for IncSta in data.get("IncomenStatments",[])]
        self.BalanceSheets = [BalanceSheet(BlaShe) for BlaShe in data.get("BalanceSheets",[])]
        self.CashFlows = [CashFlow(CshFlw) for CshFlw in data.get("CashFlows",[])]
        
    def to_dict(self):
        company_info_dic = super().to_dict()
        company_info_dic['IncomenStatments'] = [IncSta.to_dict() for IncSta in self.IncomenStatments]
        company_info_dic['BalanceSheets'] = [BlaShe.to_dict() for BlaShe in self.BalanceSheets]
        company_info_dic['CashFlows'] = [CshFlw.to_dict() for CshFlw in self.CashFlows]
        return company_info_dic