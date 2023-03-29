import quantsbin.derivativepricing as qbdp

eqOption1 = qbdp.EqOption(option_type='Call', strike=30000, expiry_date='20230407', expiry_type='European')
eqOption2 = qbdp.EqOption(option_type='Put', strike=27000, expiry_date='20230407', expiry_type='European')
# eqOption3 = qbdp.EqOption(option_type='Put', strike=50, expiry_date='20180630', expiry_type='European')
# eqOption4 = qbdp.EqOption(option_type='Call', strike=70, expiry_date='20180630', expiry_type='European')

custom_option_port = [(eqOption1, 1), (eqOption2, 1)]

custom_stgy1 = qbdp.OptionStr1Udl(option_portfolio=custom_option_port)
custom_stgy1_engine = custom_stgy1.engine(model='BSM', pricing_date='20230329', spot0=28300, rf_rate=0.04, volatility=0.64)

custom_stgy1_payoff_plt = qbdp.Plotting(custom_stgy1, 'payoff', x_axis_range=[7000, 50000], no_of_points=100).line_plot()
custom_stgy1_valuation_plt = qbdp.Plotting(custom_stgy1_engine, 'valuation', x_axis_range=[7000, 50000], no_of_points=100).line_plot()
custom_stgy1_valuation_plt.show()

custom_stgy1_delta = qbdp.Plotting(custom_stgy1_engine, 'delta', x_axis_range=[7000, 50000]).line_plot()
custom_stgy1_delta.show()

custom_stgy1_delta = qbdp.Plotting(custom_stgy1_engine, 'gamma', x_axis_range=[7000, 50000]).line_plot()
custom_stgy1_delta.show()

custom_stgy1_delta = qbdp.Plotting(custom_stgy1_engine, 'theta', x_axis_range=[7000, 50000]).line_plot()
custom_stgy1_delta.show()

custom_stgy1_delta = qbdp.Plotting(custom_stgy1_engine, 'vega', x_axis_range=[7000, 50000]).line_plot()
custom_stgy1_delta.show()

custom_stgy1_delta = qbdp.Plotting(custom_stgy1_engine, 'rho', x_axis_range=[7000, 50000]).line_plot()
custom_stgy1_delta.show()
