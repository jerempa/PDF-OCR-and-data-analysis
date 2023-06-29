from data_visualization_and_analysis import values_for_analysis
from error_handling import errors
from file_operations import file_handling
from data_fetchers import df_operations

import numpy as np
import statistics
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from linearmodels.panel import PanelOLS, RandomEffects, PooledOLS, compare
from linearmodels.iv import IV2SLS
# from linearmodels.iv import compare_models
from scipy.stats import chi2
import statsmodels.api as sm
import pandas as pd
import numpy.linalg as la
from scipy import stats



teams = ['Brentford FC', 'Brighton & Hove Albion', 'Leeds United', 'Leicester City', 'Nottingham Forest', 'Southampton FC', 'Wolverhampton Wanderers',
         'Blackburn Rovers', 'Blackpool FC', 'Cardiff City', 'Huddersfield Town', 'Hull City', 'Norwich City', 'Reading FC', 'Stoke City', 'Sunderland AFC', 'Swansea City', 'Queens Park Rangers', 'Wigan Athletic',
         'Bolton Wanderers', 'Charlton Athletic', 'Ipswich Town', 'Portsmouth FC']

# teams = ['AFC Bournemouth', 'Brentford FC', 'Brighton & Hove Albion', 'Leeds United', 'Leicester City', 'Nottingham Forest', 'Southampton FC', 'Wolverhampton Wanderers',
#          'Blackburn Rovers', 'Blackpool FC', 'Cardiff City', 'Huddersfield Town', 'Hull City', 'Norwich City', 'Reading FC', 'Sheffield United', 'Stoke City', 'Sunderland AFC', 'Swansea City', 'Queens Park Rangers', 'Wigan Athletic',
#          'Bolton Wanderers', 'Charlton Athletic', 'Derby County', 'Ipswich Town', 'Portsmouth FC']

def main():
    dfs = []
    teams.sort()
    #print(teams)
    for team in teams:
        df = values_for_analysis.financial_statement_data_cleansing(team)
        #print(df)
        #df.to_excel('FS_data.xlsx', index=False)
        #print(team, df)
        #average_attendance(df, team)
        #average_attendance_to_capacity(df, team)
        #bought_players_avg_and_median(df, team)
        #squad_value_avg_median(df, team)
        #avg_squad_value_avg_median(df, team)
        dfs.append(df)

    concat_df = df_operations.concat_dfs(dfs)
    #print(len(concat_df))
    concat_df.to_excel('FS_data2.xlsx', index=False)

    #concat_df.to_excel('Transfermarkt_data2.xlsx', index=False)


    #print(concat_df)
    #print(concat_df)
        #print(type(df))
        #print(team, df)
    # average_attendance(concat_df, "Total")
    # average_attendance_to_capacity(concat_df, "Total")
    # bought_players_avg_and_median(concat_df, "Total")
    # squad_value_avg_median(concat_df, "Total")
    # avg_squad_value_avg_median(concat_df, "Total")
    revenue(concat_df, "Total")
    wages(concat_df, "Total")

def average_attendance(df, team):
    premier_league_attendance = []
    championship_attendance = []
    league_one_attendance = []
    league_two_attendance = []

    for index, row in df.iterrows():
        if row['Average attendance'] > 2000 and row['Year'] > 1990: #don't take into account covid year without spectators
            if row['League level'] == 'First Tier':
                premier_league_attendance.append(row['Average attendance'])
            elif row['League level'] == 'Second Tier':
                championship_attendance.append(row['Average attendance'])
            elif row['League level'] == 'Third Tier':
                league_one_attendance.append(row['Average attendance'])
            elif row['League level'] == 'Fourth Tier':
                league_two_attendance.append(row['Average attendance'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_attendance)
    championship_median, championship_avg = errors.median_avg_errors(championship_attendance)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_attendance)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_attendance)

    premier_league_n = len(premier_league_attendance)
    championship_n = len(championship_attendance)
    league_one_n = len(league_one_attendance)
    league_two_n = len(league_two_attendance)

    data = append_values_to_data(team, premier_league_n, premier_league_median, premier_league_avg,
                                 championship_n, championship_median, championship_avg,
                                 league_one_n, league_one_median, league_one_avg,
                                 league_two_n, league_two_median, league_two_avg)


    file_handling.calculations_to_csv("team_data10.csv", "Average attendance", data)

def average_attendance_to_capacity(df, team):
    premier_league_attendance = []
    championship_attendance = []
    league_one_attendance = []
    league_two_attendance = []

    for index, row in df.iterrows():
        if row['Average attendance / capacity %'] > 2.00 and row['Year'] > 1990: #don't take into account covid year without spectators
            if row['League level'] == 'First Tier':
                premier_league_attendance.append(row['Average attendance / capacity %'])
            elif row['League level'] == 'Second Tier':
                championship_attendance.append(row['Average attendance / capacity %'])
            elif row['League level'] == 'Third Tier':
                league_one_attendance.append(row['Average attendance / capacity %'])
            elif row['League level'] == 'Fourth Tier':
                league_two_attendance.append(row['Average attendance / capacity %'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_attendance)
    championship_median, championship_avg = errors.median_avg_errors(championship_attendance)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_attendance)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_attendance)

    premier_league_n = len(premier_league_attendance)
    championship_n = len(championship_attendance)
    league_one_n = len(league_one_attendance)
    league_two_n = len(league_two_attendance)

    data = append_values_to_data(team, premier_league_n, premier_league_median, premier_league_avg,
                                 championship_n, championship_median, championship_avg,
                                 league_one_n, league_one_median, league_one_avg,
                                 league_two_n, league_two_median, league_two_avg)


    file_handling.calculations_to_csv("team_data10.csv", "Average attendance / capacity %", data)

def bought_players_avg_and_median(df, team):
    premier_league_arrivals = []
    championship_arrivals = []
    league_one_arrivals = []
    league_two_arrivals = []
    #print(f'\n{team}')
    for index, row in df.iterrows():
        if row['Year'] > 1990:
            if row['League level'] == 'First Tier':
                premier_league_arrivals.append(row['Infl adjusted arrivals M€'])
            elif row['League level'] == 'Second Tier':
                championship_arrivals.append(row['Infl adjusted arrivals M€'])
            elif row['League level'] == 'Third Tier':
                league_one_arrivals.append(row['Infl adjusted arrivals M€'])
            elif row['League level'] == 'Fourth Tier':
                league_two_arrivals.append(row['Infl adjusted arrivals M€'])
    #print(df)
    #print(team, premier_league_arrivals, championship_arrivals, league_one_arrivals, league_two_arrivals)


    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_arrivals)
    championship_median, championship_avg = errors.median_avg_errors(championship_arrivals)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_arrivals)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_arrivals)

    premier_league_n = len(premier_league_arrivals)
    championship_n = len(championship_arrivals)
    league_one_n = len(league_one_arrivals)
    league_two_n = len(league_two_arrivals)

    data = append_values_to_data(team, premier_league_n, premier_league_median, premier_league_avg,
                                 championship_n, championship_median, championship_avg,
                                 league_one_n, league_one_median, league_one_avg,
                                 league_two_n, league_two_median, league_two_avg)

    file_handling.calculations_to_csv("team_data10.csv", "Inflation adjusted arrivals M€", data)

def squad_value_avg_median(df, team):
    premier_league_squad_value = []
    championship_squad_value = []
    league_one_squad_value = []
    league_two_squad_value = []
    #print(f'\n{team}')
    for index, row in df.iterrows():
        if row['Year'] > 2003: #don't take into account years that don't have values
            if row['League level'] == 'First Tier':
                premier_league_squad_value.append(row['Infl adjusted squad market value M€'])
            elif row['League level'] == 'Second Tier':
                championship_squad_value.append(row['Infl adjusted squad market value M€'])
            elif row['League level'] == 'Third Tier':
                league_one_squad_value.append(row['Infl adjusted squad market value M€'])
            elif row['League level'] == 'Fourth Tier':
                league_two_squad_value.append(row['Infl adjusted squad market value M€'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_squad_value)
    championship_median, championship_avg = errors.median_avg_errors(championship_squad_value)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_squad_value)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_squad_value)

    premier_league_n = len(premier_league_squad_value)
    championship_n = len(championship_squad_value)
    league_one_n = len(league_one_squad_value)
    league_two_n = len(league_two_squad_value)

    data = append_values_to_data(team, premier_league_n, premier_league_median, premier_league_avg,
                                 championship_n, championship_median, championship_avg,
                                 league_one_n, league_one_median, league_one_avg,
                                 league_two_n, league_two_median, league_two_avg)

    file_handling.calculations_to_csv("team_data10.csv", "Inflation adjusted squad value M€", data)

def avg_squad_value_avg_median(df, team):
    premier_league_avg_squad_value = []
    championship_avg_squad_value = []
    league_one_avg_squad_value = []
    league_two_avg_squad_value = []
    #print(f'\n{team}')
    for index, row in df.iterrows():
        if row['Year'] > 2003: #don't take into account years that don't have values
            if row['League level'] == 'First Tier':
                premier_league_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])
            elif row['League level'] == 'Second Tier':
                championship_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])
            elif row['League level'] == 'Third Tier':
                league_one_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])
            elif row['League level'] == 'Fourth Tier':
                league_two_avg_squad_value.append(row['Infl adjusted avg squad market value M€'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_avg_squad_value)
    championship_median, championship_avg = errors.median_avg_errors(championship_avg_squad_value)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_avg_squad_value)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_avg_squad_value)

    premier_league_n = len(premier_league_avg_squad_value)
    championship_n = len(championship_avg_squad_value)
    league_one_n = len(league_one_avg_squad_value)
    league_two_n = len(league_two_avg_squad_value)

    data = append_values_to_data(team, premier_league_n, premier_league_median, premier_league_avg,
                                 championship_n, championship_median, championship_avg,
                                 league_one_n, league_one_median, league_one_avg,
                                 league_two_n, league_two_median, league_two_avg)

    file_handling.calculations_to_csv("team_data10.csv", "Inflation adjusted average squad value M€", data)

def attendances_by_league_level(team):
    team_df = values_for_analysis.transfermarkt_data_cleansing(team)

    #print(values_for_analysis.league_tier_throughout_years(team))

    premier_league_spectators = []
    championship_spectators = []
    league_one_spectators = []
    league_two_spectators = []

    #print(f'\n{team}')
    for index, row in team_df.iterrows():
        if row['Year'] > 1995 and row['Year'] != 2020: #don't take into account years that don't have values and COVID year without spectators
            if row['League level'] == 'First Tier':
                premier_league_spectators.append(row['Total spectators'])
            elif row['League level'] == 'Second Tier':
                championship_spectators.append(row['Total spectators'])
            elif row['League level'] == 'Third Tier':
                league_one_spectators.append(row['Total spectators'])
            elif row['League level'] == 'Fourth Tier':
                league_two_spectators.append(row['Total spectators'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_spectators)
    championship_median, championship_avg = errors.median_avg_errors(championship_spectators)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_spectators)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_spectators)

    premier_league_n = len(premier_league_spectators)
    championship_n = len(championship_spectators)
    league_one_n = len(league_one_spectators)
    league_two_n = len(league_two_spectators)

    data = append_values_to_data(team, premier_league_n, premier_league_median, premier_league_avg,
                                 championship_n, championship_median, championship_avg,
                                 league_one_n, league_one_median, league_one_avg,
                                 league_two_n, league_two_median, league_two_avg)

    #print(data)

def revenue(df, team):
    premier_league_revenue = []
    championship_revenue = []
    league_one_revenue = []
    league_two_revenue = []

    for index, row in df.iterrows():
        #if row['Average attendance / capacity %'] > 2.00 and row['Year'] > 1990: #don't take into account covid year without spectators
            if row['League level'] == 'First Tier':
                premier_league_revenue.append(row['Ln(turnover)'])
            elif row['League level'] == 'Second Tier':
                championship_revenue.append(row['Ln(turnover)'])
            elif row['League level'] == 'Third Tier':
                league_one_revenue.append(row['Ln(turnover)'])
            elif row['League level'] == 'Fourth Tier':
                league_two_revenue.append(row['Ln(turnover)'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_revenue)
    championship_median, championship_avg = errors.median_avg_errors(championship_revenue)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_revenue)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_revenue)

    premier_league_n = len(premier_league_revenue)
    championship_n = len(championship_revenue)
    league_one_n = len(league_one_revenue)
    league_two_n = len(league_two_revenue)

    data = append_values_to_data(team, premier_league_n, premier_league_median, premier_league_avg,
                                 championship_n, championship_median, championship_avg,
                                 league_one_n, league_one_median, league_one_avg,
                                 league_two_n, league_two_median, league_two_avg)


    file_handling.calculations_to_csv("team_data10.csv", "Ln(Turnover)", data)

def wages(df, team):
    premier_league_wages = []
    championship_wages = []
    league_one_wages = []
    league_two_wages = []

    for index, row in df.iterrows():
        #if row['Average attendance / capacity %'] > 2.00 and row['Year'] > 1990: #don't take into account covid year without spectators
            if row['League level'] == 'First Tier':
                premier_league_wages.append(row['Ln(inflation adjusted wages)'])
            elif row['League level'] == 'Second Tier':
                championship_wages.append(row['Ln(inflation adjusted wages)'])
            elif row['League level'] == 'Third Tier':
                league_one_wages.append(row['Ln(inflation adjusted wages)'])
            elif row['League level'] == 'Fourth Tier':
                league_two_wages.append(row['Ln(inflation adjusted wages)'])

    premier_league_median, premier_league_avg = errors.median_avg_errors(premier_league_wages)
    championship_median, championship_avg = errors.median_avg_errors(championship_wages)
    league_one_median, league_one_avg = errors.median_avg_errors(league_one_wages)
    league_two_median, league_two_avg = errors.median_avg_errors(league_two_wages)

    premier_league_n = len(premier_league_wages)
    championship_n = len(championship_wages)
    league_one_n = len(league_one_wages)
    league_two_n = len(league_two_wages)

    data = append_values_to_data(team, premier_league_n, premier_league_median, premier_league_avg,
                                 championship_n, championship_median, championship_avg,
                                 league_one_n, league_one_median, league_one_avg,
                                 league_two_n, league_two_median, league_two_avg)


    file_handling.calculations_to_csv("team_data10.csv", "Ln(Inflation adjusted wages)", data)


def append_values_to_data(team, premier_league_n, premier_league_median, premier_league_avg, championship_n, championship_median, championship_avg, league_one_n, league_one_median, league_one_avg, league_two_n, league_two_median, league_two_avg):

    data = []
    data.append(team)

    data.append(premier_league_n)
    data.append(premier_league_median)
    data.append(premier_league_avg)

    data.append(championship_n)
    data.append(championship_median)
    data.append(championship_avg)

    data.append(league_one_n)
    data.append(league_one_median)
    data.append(league_one_avg)

    data.append(league_two_n)
    data.append(league_two_median)
    data.append(league_two_avg)

    return data

def calculate_pearson_correlation_coefficient(x_values, y_values):
    covariance = np.cov(x_values, y_values)[0][1]
    stdev_x = statistics.stdev(x_values)
    stdev_y = statistics.stdev(y_values) #sample values
    pearson_correlation_coefficient = round(covariance / (stdev_x * stdev_y), 8)

    return pearson_correlation_coefficient, round(covariance, 2), round(stdev_x, 2), round(stdev_y, 2)


def calculate_r_squared(x_values1, x_values2, y_values):

    X = np.column_stack((x_values1, x_values2))
    model = LinearRegression().fit(X, y_values)

    r_squared = model.score(X, y_values)
    n = len(y_values)
    p = 2
    adjusted_r_squared = 1 - ((1 - r_squared) * (n - 1) / (n - p - 1))

    print(r_squared, adjusted_r_squared, "!ets")

    return round(r_squared, 2), round(adjusted_r_squared, 2)

def regression_calcs(x_1, x_2, x_3, x_4, df, header, y):

    #y_values = np.array(y)
    #print(df)
    exog_vars = None
    if header == 'Ln(turnover)':
        df = df.set_index(['team', 'year'])
        exog_vars = ["Overall position", "Stadium capacity (thousands)", "Ln(City population)", "Only football team in top 4 leagues in the metropolitan county",
                     'City has a professional rugby team', 'The league in which team is in']
    elif header == 'Ln(inflation adjusted wages)':
        df = df.set_index(['team', 'year'])
        exog_vars = ["Overall position", "(Squad size)^2", "(Average squad age (years))^2", "The league in which team is in"]
    elif header == "Average attendance" or header == 'Average attendance / capacity %' or header == 'Average attendance / capacity %^2':
        exog_vars = ["Overall position", "Stadium capacity (thousands)", "Ln(City population)", "Only football team in top 4 leagues in the metropolitan county",
                     'City has a professional rugby team', 'The league in which team is in', 'Distance to the nearest major city (km)']
        df = df.set_index(['Team', 'Year'])
    elif header in ["Ln(Infl adjusted squad market value M€)", "Ln(Infl adjusted avg squad market value M€)"]:
        exog_vars = ["(Squad size)^2", "(Average squad age (years))^2", "The league in which team is in", "Overall position"]
        df = df.set_index(['Team', 'Year'])
    elif header == "Ln(Infl adjusted arrivals M€)":
        exog_vars = ["The league in which team is in", "Overall position", "(Average squad age (years))^2", 'Managerial change']
        df = df.set_index(['Team', 'Year'])


    #X = np.column_stack((x_1, x_2, x_3, x_4))


    #y_values = y_values.reshape((-1, 1))
    exog = sm.add_constant(df[exog_vars])
    #print(PooledOLS(df[header], exog).fit())
    pooled_ols = PooledOLS(df[header], exog).fit()
    np.set_printoptions(suppress=False)

    #fe_model = PanelOLS(df['Ln(inflation adjusted wages)'], exog, entity_effects=True, time_effects=True).fit()
    fe_model = PanelOLS(df[header], exog, entity_effects=True, time_effects=True, drop_absorbed=True).fit()


    #fe_model = PanelOLS(y_values, X, entity_effects=True, time_effects=True).fit()
    #fe_model = PanelOLS(y_values, X, entity_effects=True).fit()

    fe_model1 = PanelOLS(df[header], exog, entity_effects=True, drop_absorbed=True).fit()
    #print(fe_model.pvalues)
    print(fe_model)
    #print(fe_model1.pvalues)
    print(fe_model1)


    # Estimate a random effects model
    #re_model = RandomEffects(df['Ln(inflation adjusted wages)'], exog).fit()
    re_model = RandomEffects(df[header], exog).fit()
    #print(re_model.pvalues)
    print(re_model)

    comparison = compare({'PooledOLS': pooled_ols, 'FE1': fe_model, 'FE2': fe_model1, 'RE': re_model})

    print(comparison)


    #print(X, y)
    #X = sm.add_constant(X)

    #model = sm.OLS(y_values, X).fit()

    #print(model.summary())

    # results_df = pd.read_html(model.summary().tables[0].as_html(), header=0, index_col=0)[0]
    # results_df1 = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]
    # results_df2 = pd.read_html(model.summary().tables[2].as_html(), header=0, index_col=0)[0]

    #results_df = pd.concat([results_df, results_df1, results_df2], axis=0)

    # results_df.to_excel("results.xlsx")
    # results_df1.to_excel("results1.xlsx")
    # results_df2.to_excel("results2.xlsx")
    #
    #
    # t_values = model.tvalues
    # r_squared = model.rsquared
    # adj_r_squared = model.rsquared_adj
    # coefs = model.params
    # p_values = model.pvalues
    # std_errs = model.bse

    #np.set_printoptions(precision=10, suppress=True)


    # coefs = [format(x, '.10f') for x in coefs]
    # p_values = [format(x, '.10f') for x in p_values]
    # std_errs = [format(x, '.10f') for x in std_errs]

    # print("Coefs: ", coefs)
    #print("P-values", p_values)
    # print("Standard errors", std_errs)
    # print("t values", t_values)
    # print("R squared", round(r_squared, 2))
    #print("\n")
    #print(coefs, p_values, std_errs, t_values, round(r_squared, 2), round(adj_r_squared, 2))

    #return coefs, p_values, std_errs, t_values, round(r_squared, 2), round(adj_r_squared, 2)
    # r_squared = linregress(x_values, y_values).rvalue ** 2
    # predicted_values = slope * np.array(x_values) + intercept
    # residuals = np.array(y_values) - predicted_values
    # ssr = np.sum(residuals ** 2)
    # mean_value = statistics.mean(y_values)
    # sst = np.sum((np.array(y_values) - mean_value) ** 2)
    # r_squared = round(1 - (ssr / sst), 2)
    #print(r_squared, round(linregress(x_values, y_values).rvalue ** 2, 2))
    #
    #
    # n = len(y_values)
    # p = 1
    # adjusted_r_squared = 1 - ((1 - r_squared) * (n - 1) / (n - p - 1))

def hausman2(fe, re):
    """
    Parameters
    ==========
    fe : statsmodels.regression.linear_panel.PanelLMWithinResults
        The results obtained by using sm.PanelLM with the
        method='within' option.
    re : statsmodels.regression.linear_panel.PanelLMRandomResults
        The results obtained by using sm.PanelLM with the
        method='swar' option.
    Returns
    =======
    chi2 : float
        The test statistic
    df : int
        The number of degrees of freedom for the distribution of the
        test statistic
    pval : float
        The p-value associated with the null hypothesis
    Notes
    =====
    The null hypothesis supports the claim that the random effects
    estimator is "better". If we reject this hypothesis it is the same
    as saying we should be using fixed effects because there are
    systematic differences in the coefficients.
    """

    # Pull data out
    b = fe.params
    B = re.params
    v_b = fe.cov
    v_B = re.cov

    # NOTE: find df. fe should toss time-invariant variables, but it
    #       doesn't. It does return garbage so we use that to filter
    #df = b[np.abs(b) < 1e8].size

    df = 0

    #print(df, "jee")

    # compute test statistic and associated p-value
    chi2 = np.dot((b - B).T, la.inv(v_b - v_B).dot(b - B))
    pval = stats.chi2.sf(chi2, df)

    return chi2, df, pval


def calculate_mse_rmse_mae(slope, intercept, x_values1, x_values2, y_values):
    #x_values = np.array(x_values)
    #y_values = np.array(y_values)
    X = np.column_stack((x_values1, x_values2))
    model = LinearRegression().fit(X, y_values)
    predicted_values = model.predict(X)

    #predicted_values = slope * x_values + intercept
    mse = round(mean_squared_error(y_values, predicted_values), 2)
    rmse = round(mean_squared_error(y_values, predicted_values, squared=False), 2)
    mae = round(mean_absolute_error(y_values, predicted_values), 2)


    return mse, rmse, mae
    # residuals = y_values - predicted_values
    #
    # mse = np.mean(residuals ** 2)
    # rmse = round(np.sqrt(mse), 2)
    # mae = round(np.mean(np.abs(residuals)), 2)


