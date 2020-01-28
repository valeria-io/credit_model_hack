from typing import NamedTuple
import numpy as np



class RawColumns(NamedTuple):
    LOAN_NUMBER: str = 'LoanNumber'
    NEW_CREDIT_CUSTOMER: str = 'NewCreditCustomer'
    LOAN_APPLICATION_STARTED_DATE: str = 'LoanApplicationStartedDate'
    APPLICATION_SIGNED_HOUR: str = 'ApplicationSignedHour'
    APPLICATION_SIGNED_WEEKDAY: str = 'ApplicationSignedWeekday'
    VERIFICATION_TYPE: str = 'VerificationType'
    LANGUAGE_CODE: str = 'LanguageCode'
    AGE: str = 'Age'
    DATE_OF_BIRTH: str = 'DateOfBirth'
    GENDER: str = 'Gender'
    COUNTRY: str = 'Country'
    APPLIED_AMOUNT: str = 'AppliedAmount'
    AMOUNT: str = 'Amount'
    INTEREST: str = 'Interest'
    LOAN_DURATION: str = 'LoanDuration'
    MONTHLY_PAYMENT: str = 'MonthlyPayment'
    COUNTY: str = 'County'
    CITY: str = 'City'
    USE_OF_LOAN: str = 'UseOfLoan'
    EDUCATION: str = 'Education'
    MARITAL_STATUS: str = 'MaritalStatus'
    NR_OF_DEPENDANTS: str = 'NrOfDependants'
    EMPLOYMENT_STATUS: str = 'EmploymentStatus'
    EMPLOYMENT_DURATION_CURRENT_EMPLOYER: str = 'EmploymentDurationCurrentEmployer'
    WORK_EXPERIENCE: str = 'WorkExperience'
    OCCUPATION_AREA: str = 'OccupationArea'
    HOME_OWNERSHIP_TYPE: str = 'HomeOwnershipType'
    INCOME_FROM_PRINCIPAL_EMPLOYER: str = 'IncomeFromPrincipalEmployer'
    INCOME_FROM_PENSION: str = 'IncomeFromPension'
    INCOME_FROM_FAMILY_ALLOWANCE: str = 'IncomeFromFamilyAllowance'
    INCOME_FROM_SOCIAL_WELFARE: str = 'IncomeFromSocialWelfare'
    INCOME_FROM_LEAVE_PAY: str = 'IncomeFromLeavePay'
    INCOME_FROM_CHILD_SUPPORT: str = 'IncomeFromChildSupport'
    INCOME_OTHER: str = 'IncomeOther'
    INCOME_TOTAL: str = 'IncomeTotal'
    EXISTING_LIABILITIES: str = 'ExistingLiabilities'
    LIABILITIES_TOTAL: str = 'LiabilitiesTotal'
    REFINANCE_LIABILITIES: str = 'RefinanceLiabilities'
    DEBT_TO_INCOME: str = 'DebtToIncome'
    FREE_CASH: str = 'FreeCash'
    STATUS: str = 'Status'
    CREDIT_SCORE_ES_MICRO_L: str = 'CreditScoreEsMicroL'
    CREDIT_SCORE_ES_EQUIFAX_RISK: str = 'CreditScoreEsEquifaxRisk'
    CREDIT_SCORE_FI_ASIAKAS_TIETO_RISK_GRADE: str = 'CreditScoreFiAsiakasTietoRiskGrade'
    CREDIT_SCORE_EE_MINI: str = 'CreditScoreEeMini'
    NO_OF_PREVIOUS_LOANS_BEFORE_LOAN: str = 'NoOfPreviousLoansBeforeLoan'
    AMOUNT_OF_PREVIOUS_LOANS_BEFORE_LOAN: str = 'AmountOfPreviousLoansBeforeLoan'
    PREVIOUS_REPAYMENTS_BEFORE_LOAN: str = 'PreviousRepaymentsBeforeLoan'
    PREVIOUS_EARLY_REPAYMENTS_BEFOLE_LOAN: str = 'PreviousEarlyRepaymentsBefoleLoan'
    PREVIOUS_EARLY_REPAYMENTS_COUNT_BEFORE_LOAN: str = 'PreviousEarlyRepaymentsCountBeforeLoan'


COLUMNS = RawColumns()


class ExcludeColsFromTraining(NamedTuple):
    pass


class NewColumns(NamedTuple):
    pass


class TrainingColumns(NamedTuple):
    #@todo: make this raw - exclude + newCols
    pass



REPLACE_VALUES = {
    COLUMNS.OCCUPATION_AREA: {
        -1.: np.nan,
        0.: np.nan,
        1.: 'Other',
        2.: 'Mining',
        3.: 'Processing',
        4.: 'Energy',
        5.: 'Utilities',
        6.: 'Construction',
        7.: 'Retail and wholesale',
        8.: 'Transport and warehousing',
        9.: 'Hospitality and catering',
        10.: 'Info and telecom',
        11.: 'Finance and insurance',
        12.: 'Real-estate',
        13.: 'Research',
        14.: 'Administrative',
        15.: 'Civil service & military',
        16.: 'Education',
        17.: 'Healthcare and social help',
        18.: 'Art and entertainment',
        19.: 'Agriculture, forestry and fishing'
    },
    COLUMNS.EMPLOYMENT_STATUS: {
        -1.: np.nan,
        0.: np.nan,
        1.: 'Unemployed',
        2.: 'Partially Employed',
        3.: 'Fully Employed',
        4.: 'Self-Employed',
        5.: 'Entrepreneur',
        6.: 'Retiree'
    },
    COLUMNS.MARITAL_STATUS: {
        -1.: np.nan,
        0.: np.nan,
        1.: 'Married',
        2.: 'Cohabitant',
        3.: 'Single',
        4.: 'Divorced',
        5.: 'Widow'
    },
    COLUMNS.EDUCATION: {
        -1.: np.nan,
        1.: 'Primary',
        2.: 'Basic',
        3.: 'Vocational',
        4.: 'Secondary',
        5.: 'Higher',
        0.: np.nan
    },
    COLUMNS.USE_OF_LOAN: {
        -1.: np.nan,
        0: 'Loan Consolidation',
        1: 'Real Estate',
        2: 'Home Improvement',
        3: 'Business',
        4: 'Education',
        5: 'Travel',
        6: 'Vehicle',
        7: 'Other',
        8: 'Health',
        101: 'Working Capital',
        102: 'Purchase of Machinery Equipment',
        104: 'Accounts Receivable Financing',
        106: 'Construction Finance',
        107: 'Acquisition of Stocks',
        108: 'Acquisition of Real Estate',
        110: 'Other Business'
    },
    COLUMNS.GENDER: {
        0.: 'Male',
        1.: 'Woman',
        2.: np.nan
    },
    COLUMNS.VERIFICATION_TYPE: {
        0.: np.nan,
        1.: 'Income Unverified',
        2.: 'Cross-Ref by Phone',
        3.: 'Income Verified',
        4.: 'Income and Expenes Verified'
    },
    COLUMNS.LANGUAGE_CODE: {
        1: 'Estonian',
        2: 'English',
        3: 'Russian',
        4: 'Finnish',
        5: 'German',
        6: 'Spanish',
        9: 'Slovakian',
        7: np.nan,
        10: np.nan,
        13: np.nan,
        15: np.nan,
        21: np.nan,
        22: np.nan
    },
    #@TODO: ADD TO TES:T''
    COLUMNS.HOME_OWNERSHIP_TYPE: {
        -1: np.nan,
        0: 'Homeless',
        1: 'Owner',
        2: 'Living with parents',
        3: 'Tenant, pre-furnished property',
        4: 'Tenant, unfurnished property',
        5: 'Council house',
        6: 'Joint tenant',
        7: 'Joint ownership',
        8: 'Mortgage',
        9: 'Owner with encumbrance',
        10:' Other'
    },
    COLUMNS.AGE: {
        0: np.nan,
        1: np.nan,
        2: np.nan
    }
}