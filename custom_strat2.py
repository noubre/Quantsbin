import quantsbin.derivativepricing as qbdp

eqOption1 = qbdp.EqOption(option_type='Call', strike=50, expiry_date='20180630', expiry_type='European')
eqOption2 = qbdp.EqOption(option_type='Call', strike=55, expiry_date='20180630', expiry_type='European')
eqOption3 = qbdp.EqOption(option_type='Put', strike=50, expiry_date='20180630', expiry_type='European')
eqOption4 = qbdp.EqOption(option_type='Call', strike=70, expiry_date='20180630', expiry_type='European')

custom_option_port = [(eqOption3, 1), (eqOption2, -1), (eqOption1, 1), (eqOption4, 2)]

custom_stgy1 = qbdp.OptionStr1Udl(option_portfolio=custom_option_port)

custom_stgy1_payoff_plt = qbdp.Plotting(custom_stgy1,'payoff', x_axis_range=[20, 100], no_of_points=100).line_plot()
custom_stgy1_payoff_plt.show()
