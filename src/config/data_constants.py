from typing import NamedTuple
import numpy as np


class RawColumns(NamedTuple):
    LOAN_NUMBER: str = "LoanNumber"
    NEW_CREDIT_CUSTOMER: str = "NewCreditCustomer"
    APPLICATION_SIGNED_HOUR: str = "ApplicationSignedHour"
    APPLICATION_SIGNED_WEEKDAY: str = "ApplicationSignedWeekday"
    VERIFICATION_TYPE: str = "VerificationType"
    LANGUAGE_CODE: str = "LanguageCode"
    AGE: str = "Age"
    GENDER: str = "Gender"
    APPLIED_AMOUNT: str = "AppliedAmount"
    AMOUNT: str = "Amount"
    INTEREST: str = "Interest"
    LOAN_DURATION: str = "LoanDuration"
    MONTHLY_PAYMENT: str = "MonthlyPayment"
    USE_OF_LOAN: str = "UseOfLoan"
    EDUCATION: str = "Education"
    MARITAL_STATUS: str = "MaritalStatus"
    NR_OF_DEPENDANTS: str = "NrOfDependants"
    EMPLOYMENT_STATUS: str = "EmploymentStatus"
    EMPLOYMENT_DURATION_CURRENT_EMPLOYER: str = "EmploymentDurationCurrentEmployer"
    WORK_EXPERIENCE: str = "WorkExperience"
    OCCUPATION_AREA: str = "OccupationArea"
    HOME_OWNERSHIP_TYPE: str = "HomeOwnershipType"
    INCOME_FROM_PRINCIPAL_EMPLOYER: str = "IncomeFromPrincipalEmployer"
    INCOME_FROM_PENSION: str = "IncomeFromPension"
    INCOME_FROM_FAMILY_ALLOWANCE: str = "IncomeFromFamilyAllowance"
    INCOME_FROM_SOCIAL_WELFARE: str = "IncomeFromSocialWelfare"
    INCOME_FROM_LEAVE_PAY: str = "IncomeFromLeavePay"
    INCOME_FROM_CHILD_SUPPORT: str = "IncomeFromChildSupport"
    INCOME_OTHER: str = "IncomeOther"
    INCOME_TOTAL: str = "IncomeTotal"
    EXISTING_LIABILITIES: str = "ExistingLiabilities"
    LIABILITIES_TOTAL: str = "LiabilitiesTotal"
    REFINANCE_LIABILITIES: str = "RefinanceLiabilities"
    DEBT_TO_INCOME: str = "DebtToIncome"
    FREE_CASH: str = "FreeCash"
    STATUS: str = "Status"
    CREDIT_SCORE_ES_MICRO_L: str = "CreditScoreEsMicroL"
    CREDIT_SCORE_EE_MINI: str = "CreditScoreEeMini"
    NO_OF_PREVIOUS_LOANS_BEFORE_LOAN: str = "NoOfPreviousLoansBeforeLoan"
    AMOUNT_OF_PREVIOUS_LOANS_BEFORE_LOAN: str = "AmountOfPreviousLoansBeforeLoan"
    PREVIOUS_REPAYMENTS_BEFORE_LOAN: str = "PreviousRepaymentsBeforeLoan"
    PREVIOUS_EARLY_REPAYMENTS_BEFOLE_LOAN: str = "PreviousEarlyRepaymentsBefoleLoan"
    PREVIOUS_EARLY_REPAYMENTS_COUNT_BEFORE_LOAN: str = "PreviousEarlyRepaymentsCountBeforeLoan"
    COUNTY: str = "County"
    CITY: str = "City"
    LOAN_APPLICATION_STARTED_DATE: str = "LoanApplicationStartedDate"
    DATE_OF_BIRTH: str = "DateOfBirth"

COLUMNS = RawColumns()


class ExcludeColsFromTraining(NamedTuple):
    INCOME_FROM_PRINCIPAL_EMPLOYER: str = "IncomeFromPrincipalEmployer"
    INCOME_FROM_PENSION: str = "IncomeFromPension"
    INCOME_FROM_FAMILY_ALLOWANCE: str = "IncomeFromFamilyAllowance"
    INCOME_FROM_SOCIAL_WELFARE: str = "IncomeFromSocialWelfare"
    INCOME_FROM_LEAVE_PAY: str = "IncomeFromLeavePay"
    INCOME_FROM_CHILD_SUPPORT: str = "IncomeFromChildSupport"
    INCOME_OTHER: str = "IncomeOther"
    GENDER: str = "Gender"
    MARITAL_STATUS: str = "MaritalStatus"
    COUNTY: str = "County"
    CITY: str = "City"
    LOAN_APPLICATION_STARTED_DATE: str = "LoanApplicationStartedDate"
    DATE_OF_BIRTH: str = "DateOfBirth"


EXCLUDE_COLUMNS = ExcludeColsFromTraining()


class NewColumns(NamedTuple):
    AMOUNT_RECEIVED_DIFF: str = "AmountReceivedDiff"
    PERC_PRINCIPAL_EMPLOYER_FROM_TOTAL_INCOME: str = "PercentageIncomeFromPrincipalEmployer"
    PERC_PENSION_FROM_TOTAL_INCOME: str = "PercentageIncomeFromPension"
    PERC_FAMILY_ALLOWANCE_FROM_TOTAL_INCOME: str = "PercentageIncomeFromFamilyAllowance"
    PERC_SOCIAL_WELFARE_FROM_TOTAL_INCOME: str = "PercentageIncomeFromSocialWelfare"
    PERC_LEAVE_PAY_FROM_TOTAL_INCOME: str = "PercentageIncomeFromLeavePay"
    PERC_CHILD_SUPPORT_FROM_TOTAL_INCOME: str = "PercentageIncomeFromChildSupport"
    PERC_OTHER_FROM_TOTAL_INCOME: str = "PercentageIncomeOther"
    MONTH_OF_BIRTH: str = "MonthOfBirth"
    YEAR_OF_BIRTH: str = "YearOfBirth"
    NAN_PERC_PER_ROW: str = "NaNPercPerRow"
    NAN_LEVEL: str = "NaNLevelInd"


NEW_COLUMNS = NewColumns()


class TrainingColumns(NamedTuple):
    # @todo: make this raw - exclude + newCols
    pass


REPLACE_VALUES = {
    COLUMNS.CREDIT_SCORE_ES_MICRO_L: {"": "Non-M"},
    COLUMNS.OCCUPATION_AREA: {
        -1.0: np.nan,
        0.0: np.nan,
        1.0: "Other",
        2.0: "Mining",
        3.0: "Processing",
        4.0: "Energy",
        5.0: "Utilities",
        6.0: "Construction",
        7.0: "Retail and wholesale",
        8.0: "Transport and warehousing",
        9.0: "Hospitality and catering",
        10.0: "Info and telecom",
        11.0: "Finance and insurance",
        12.0: "Real-estate",
        13.0: "Research",
        14.0: "Administrative",
        15.0: "Civil service & military",
        16.0: "Education",
        17.0: "Healthcare and social help",
        18.0: "Art and entertainment",
        19.0: "Agriculture, forestry and fishing",
    },
    COLUMNS.EMPLOYMENT_STATUS: {
        -1.0: np.nan,
        0.0: np.nan,
        1.0: "Unemployed",
        2.0: "Partially Employed",
        3.0: "Fully Employed",
        4.0: "Self-Employed",
        5.0: "Entrepreneur",
        6.0: "Retiree",
    },
    COLUMNS.MARITAL_STATUS: {
        -1.0: np.nan,
        0.0: np.nan,
        1.0: "Married",
        2.0: "Cohabitant",
        3.0: "Single",
        4.0: "Divorced",
        5.0: "Widow",
    },
    COLUMNS.EDUCATION: {
        -1.0: np.nan,
        1.0: "Primary",
        2.0: "Basic",
        3.0: "Vocational",
        4.0: "Secondary",
        5.0: "Higher",
        0.0: np.nan,
    },
    COLUMNS.USE_OF_LOAN: {
        -1.0: np.nan,
        0: "Loan Consolidation",
        1: "Real Estate",
        2: "Home Improvement",
        3: "Business",
        4: "Education",
        5: "Travel",
        6: "Vehicle",
        7: "Other",
        8: "Health",
        101: "Working Capital",
        102: "Purchase of Machinery Equipment",
        104: "Accounts Receivable Financing",
        106: "Construction Finance",
        107: "Acquisition of Stocks",
        108: "Acquisition of Real Estate",
        110: "Other Business",
    },
    COLUMNS.GENDER: {0.0: "Male", 1.0: "Woman", 2.0: np.nan},
    COLUMNS.VERIFICATION_TYPE: {
        0.0: np.nan,
        1.0: "Income Unverified",
        2.0: "Cross-Ref by Phone",
        3.0: "Income Verified",
        4.0: "Income and Expenes Verified",
    },
    COLUMNS.LANGUAGE_CODE: {
        1: "Estonian",
        2: "Other",
        3: "Russian",
        4: "Other",
        5: "Other",
        6: "Other",
        9: "Other",
        7: np.nan,
        10: np.nan,
        13: np.nan,
        15: np.nan,
        21: np.nan,
        22: np.nan,
    },
    COLUMNS.HOME_OWNERSHIP_TYPE: {
        -1: np.nan,
        0: "Other",
        1: "Owner",
        2: "Living with parents",
        3: "Tenant, pre-furnished property",
        4: "Tenant, unfurnished property",
        5: "Other",
        6: "Joint tenant",
        7: "Joint ownership",
        8: "Mortgage",
        9: "Owner",
        10: "Other",
    },
    COLUMNS.AGE: {0: np.nan, 1: np.nan, 2: np.nan},
}

REPLACE_NAN = {
    COLUMNS.VERIFICATION_TYPE: {np.nan: "Income Unverified"},
    COLUMNS.GENDER: {np.nan: "Male"},
    COLUMNS.EDUCATION: {np.nan: "Basic"},
    COLUMNS.HOME_OWNERSHIP_TYPE: {np.nan: "NaN"},
    COLUMNS.WORK_EXPERIENCE: {np.nan: "NaN"},
    COLUMNS.EMPLOYMENT_DURATION_CURRENT_EMPLOYER: {np.nan: "NaN"},
    COLUMNS.USE_OF_LOAN: {np.nan: "NaN"},
    COLUMNS.MARITAL_STATUS: {np.nan: "NaN"},
    COLUMNS.EMPLOYMENT_STATUS: {np.nan: "NaN"},
    COLUMNS.OCCUPATION_AREA: {np.nan: "NaN"},
    COLUMNS.CREDIT_SCORE_EE_MINI: {np.nan: "NaN"}
}

GROUP_VALUES = {
    COLUMNS.USE_OF_LOAN: {
        "Working Capital": "Business",
        "Purchase of Machinery Equipment": "Business",
        "Accounts Receivable Financing": "Business",
        "Construction Finance": "Business",
        "Acquisition of Stocks": "Business",
        "Acquisition of Real Estate": "Business",
        "Other Business": "Business",
    },
    COLUMNS.OCCUPATION_AREA: {
      "Utilities": "Other",
      "Mining": "Other"
    }
}

OUTLIERS = (2383, 573, 979, 6231, 12741, 37948)
