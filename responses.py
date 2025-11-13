# responses.py
from typing import Dict, List

FAQS: Dict[str, List[str]] = {
    "tax": [
        "Income tax is charged based on slabs. Under the new regime, slabs change by year — always check the official income tax site for latest slabs.",
        "Basic tip: investments under Section 80C (like PPF, ELSS) can reduce taxable income up to the allowed limit.",
    ],
    "mutual fund": [
        "Mutual funds pool investor money to invest in stocks, bonds or other instruments. There are equity, debt, and hybrid funds.",
        "ELSS (Equity Linked Savings Scheme) is a tax-saving mutual fund with a 3-year lock-in and qualifies under Section 80C.",
    ],
    "insurance": [
        "Term insurance is pure life cover — higher cover at lower premium. Endowment policies combine insurance + savings but cost more.",
        "Health insurance covers medical expenses — check sub-limits, co-pay, and pre-existing disease waiting periods.",
    ],
    "government scheme": [
        "Popular schemes: PMAY (housing), PMVVY (pension), Sukanya Samriddhi Scheme (girl child savings). Eligibility differs by scheme.",
        "For official details and eligibility always refer to the government portal (e.g., india.gov.in) or scheme-specific sites.",
    ],
    "saving": [
        "Basic saving strategies: set up an emergency fund (3-6 months of expenses), automate monthly SIPs for investing, reduce high-interest debt.",
    ],
    "default": [
        "I’m not sure about that exact question. Try asking about tax, mutual funds, insurance, government schemes, or saving tips.",
    ],
}
