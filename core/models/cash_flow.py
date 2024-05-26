class CashFlow:
    
    def __init__(self, data = None):
        self.Amortization = data.get("Amortization")
        self.BeginningCashBalance = data.get("BeginningCashBalance")
        self.CapitalExpenditures = data.get("CapitalExpenditures")
        self.CashFromFinancingActivities = data.get("CashFromFinancingActivities")
        self.CashFromInvestingActivities = data.get("CashFromInvestingActivities")
        self.CashFromOperatingActivities = data.get("CashFromOperatingActivities")
        self.CashInterestPaid = data.get("CashInterestPaid")
        self.CashPayments = data.get("CashPayments")
        self.CashReceipts = data.get("CashReceipts")
        self.CashTaxesPaid = data.get("CashTaxesPaid")
        self.ChangesinWorkingCapital = data.get("ChangesinWorkingCapital")
        self.DeferredTaxes = data.get("DeferredTaxes")
        self.DepreciationDepletion = data.get("DepreciationDepletion")
        self.EndingCashBalance = data.get("EndingCashBalance")
        self.FinancingCashFlowItems = data.get("FinancingCashFlowItems")
        self.ForeignExchangeEffects = data.get("ForeignExchangeEffects")
        self.FreeCashFlow = data.get("FreeCashFlow")
        self.FreeCashFlowGrowth = data.get("FreeCashFlowGrowth")
        self.FreeCashFlowYield = data.get("FreeCashFlowYield")
        self.IssuanceRetirementofDebtNet = data.get("IssuanceRetirementofDebtNet")
        self.IssuanceRetirementofStockNet = data.get("IssuanceRetirementofStockNet")
        self.NetChangeinCash = data.get("NetChangeinCash")
        self.NetIncomeStartingLine = data.get("NetIncomeStartingLine")
        self.NonCashItems = data.get("NonCashItems")
        self.OtherInvestingCashFlowItemsTotal = data.get("OtherInvestingCashFlowItemsTotal")
        self.PeriodEnding = data.get("PeriodEnding")
        self.PeriodLength = data.get("PeriodLength")
        self.TotalCashDividendsPaid = data.get("TotalCashDividendsPaid")
        
    def to_dict(self):
        return self.__dict__