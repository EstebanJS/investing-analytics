class IncomeStatement:
    
    def __init__(self,data = None):
        self.CostofRevenueTotal = data.get("CostofRevenueTotal")
        self.DPSCommonStockPrimaryIssue = data.get("DPSCommonStockPrimaryIssue")
        self.DepreciationAmortization = data.get("DepreciationAmortization")
        self.DilutedEPSExcludingExtraordinaryItems = data.get("DilutedEPSExcludingExtraordinaryItems")
        self.DilutedNetIncome = data.get("DilutedNetIncome")
        self.DilutedNormalizedEPS = data.get("DilutedNormalizedEPS")
        self.DilutedWeightedAverageShares = data.get("DilutedWeightedAverageShares")
        self.DilutionAdjustment = data.get("DilutionAdjustment")
        self.EquityInAffiliates = data.get("EquityInAffiliates")
        self.GainLossonSaleofAssets = data.get("GainLossonSaleofAssets")
        self.GrossProfit = data.get("GrossProfit")
        self.IncomeAvailabletoCommonExcludingExtraordinaryItems = data.get("IncomeAvailabletoCommonExcludingExtraordinaryItems")
        self.InterestExpenseIncomeNetOperating = data.get("InterestExpenseIncomeNetOperating")
        self.InterestIncomeExpenseNetNonOperating = data.get("InterestIncomeExpenseNetNonOperating")
        self.MinorityInterest = data.get("MinorityInterest")
        self.NetIncome = data.get("NetIncome")
        self.NetIncomeAfterTaxes = data.get("NetIncomeAfterTaxes")
        self.NetIncomeBeforeExtraordinaryItems = data.get("NetIncomeBeforeExtraordinaryItems")
        self.NetIncomeBeforeTaxes = data.get("NetIncomeBeforeTaxes")
        self.OperatingIncome = data.get("OperatingIncome")
        self.OtherNet = data.get("OtherNet")
        self.OtherOperatingExpensesTotal = data.get("OtherOperatingExpensesTotal")
        self.OtherRevenueTotal = data.get("OtherRevenueTotal")
        self.PeriodEnding = data.get("PeriodEnding")
        self.ProvisionforIncomeTaxes = data.get("ProvisionforIncomeTaxes")
        self.ResearchDevelopment = data.get("ResearchDevelopment")
        self.Revenue = data.get("Revenue")
        self.SellingGeneralAdminExpensesTotal = data.get("SellingGeneralAdminExpensesTotal")
        self.TotalAdjustmentstoNetIncome = data.get("TotalAdjustmentstoNetIncome")
        self.TotalExtraordinaryItems = data.get("TotalExtraordinaryItems")
        self.TotalOperatingExpenses = data.get("TotalOperatingExpenses")
        self.TotalRevenue = data.get("TotalRevenue")
        self.USGAAPAdjustment = data.get("USGAAPAdjustment")
        self.UnusualExpenseIncome = data.get("UnusualExpenseIncome")
        
    def to_dict(self):
        return self.__dict__