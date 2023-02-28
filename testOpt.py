import quantsbin.derivativepricing as qbdp

equity_option1 = qbdp.EqOption(option_type='Call', strike=50, expiry_date='20190621')

print(equity_option1.payoff(55))
