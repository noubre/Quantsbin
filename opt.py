import quantsbin.derivativepricing as qbdp

equity_option1 = qbdp.EqOption(option_type='Put', strike=22000.0, expiry_date='20230331', expiry_type='European')

print(equity_option1.list_models())

# print(equity_option1.payoff(55))

# eq1_payoff = qbdp.Plotting(equity_option1, 'payoff', x_axis_range=[15000, 30000]).line_plot()

eq1_engine = equity_option1.engine(model='BSM', pricing_date='20230227', spot0=23517.0, rf_rate=0.05, volatility=0.557)

print(eq1_engine.valuation())

print(eq1_engine.risk_parameters())

# eq1_pnl = qbdp.Plotting(eq1_engine, 'pnl', x_axis_range=[15000, 30000]).line_plot()
# eq1_pnl.show()

eq1_payoff = qbdp.Plotting(equity_option1, 'payoff', x_axis_range=[15000, 30000]).line_plot()
eq1_pnl = qbdp.Plotting(eq1_engine, 'valuation', x_axis_range=[15000, 30000]).line_plot()
eq1_pnl.show()

eq1_delta = qbdp.Plotting(eq1_engine, 'delta', x_axis_range=[15000, 30000]).line_plot()
eq1_delta.show()

eq1_delta = qbdp.Plotting(eq1_engine, 'gamma', x_axis_range=[15000, 30000]).line_plot()
eq1_delta.show()

eq1_delta = qbdp.Plotting(eq1_engine, 'theta', x_axis_range=[15000, 30000]).line_plot()
eq1_delta.show()

eq1_delta = qbdp.Plotting(eq1_engine, 'vega', x_axis_range=[15000, 30000]).line_plot()
eq1_delta.show()

# eq1_engine.pnl_attribution(delta_spot=.03, delta_time=2, delta_rf_rate=.03, delta_vol=.1)