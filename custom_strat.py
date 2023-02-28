import quantsbin.derivativepricing as qbdp

# print(qbdp.StdStrategies.__doc__)

std_stgy_bullcall = qbdp.StdStrategies(
    name='bull_call',
    asset='Stock',
    low_strike=50,
    strike_spread=10,
    expiry_date='20190721',
    expiry_type='European'
)

bull_call_payoff_plt = qbdp.Plotting(
    std_stgy_bullcall,
    'payoff',
    x_axis_range=[20, 100],
    no_of_points=100
).line_plot()

bull_call_payoff_plt.show()

std_stgy_bullcall_engine = std_stgy_bullcall.engine(
    model="BSM",
    spot0=55,
    pricing_date='20180531',
    volatility=.25,
    rf_rate=.05
)
print("Value of Bull Call option strategy is {}".format(std_stgy_bullcall_engine.valuation()))

print("Greeks for Bull Call option strategy are {}".format(std_stgy_bullcall_engine.risk_parameters()))

bull_call_pnl_plt = qbdp.Plotting(
    std_stgy_bullcall_engine,
    'pnl',
    x_axis_range=[20, 100],
    no_of_points=100
).line_plot()

bull_call_pnl_plt.show()

bull_call_val_plt = qbdp.Plotting(
    std_stgy_bullcall_engine,
    'valuation',
    x_axis_range=[20, 100],
    no_of_points=100
).line_plot()

bull_call_val_plt.show()

bull_call_delta_plt = qbdp.Plotting(
    std_stgy_bullcall_engine,
    'delta',
    x_axis_range=[20, 100],
    no_of_points=100
).line_plot()

bull_call_delta_plt.show()

bull_call_gamma_plt = qbdp.Plotting(
    std_stgy_bullcall_engine,
    'gamma',
    x_axis_range=[20, 100],
    no_of_points=100
).line_plot()

bull_call_gamma_plt.show()

bull_call_vega_plt = qbdp.Plotting(
    std_stgy_bullcall_engine,
    'vega',
    x_axis_range=[20, 100],
    no_of_points=100
).line_plot()

bull_call_vega_plt.show()

