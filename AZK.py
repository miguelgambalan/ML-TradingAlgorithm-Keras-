import QuantLib as ql
import math
import numpy as np
import pandas as pd


today = ql.Date(10,5,2024)

ql.Settings.instance().evaluationDate = today


print(ql.Settings.instance().evaluationDate)


rate = ql.InterestRate(0.05, ql.Actual360(), ql.Compounded, ql.Annual)

print (rate)