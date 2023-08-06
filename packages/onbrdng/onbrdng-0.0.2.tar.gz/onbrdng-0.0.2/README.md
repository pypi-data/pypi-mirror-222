# `onbrdng`

The `onbrdng` is a package made by Onbrdng for the data team and it's clients to use

It contains multiple modules to analyse different problems:

1. Marketing Mix Modeling
2. Decomposition for logistic regressions over time
3. Multinomial logistic regression with impact of variables 
4. Decision tree / beslisboom
5. Time-series forecasting with regressions and random forest
6. Saving and loading models

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install onbrdng.

```bash
pip install onbrdng
```

## 1. MMM

```python

# import modules
import pandas as pd
import numpy as np
from onbrdng.analyse_mmm_models import mmm, s_curve, decay
import ssl
import statsmodels.formula.api as smf
import plotly.io as pio
pio.renderers.default = "browser"
import warnings
warnings.filterwarnings("ignore")


# Get some example data (you might need to run ssl._create_default_https_context = ssl._create_unverified_context:
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://raw.githubusercontent.com/SimonTeg/nlodatascience/master/sales_vs_media.csv'
df_example = pd.read_csv(url)
# make a dataset for the historical data with the sales, and one to forecast the sales
df_train = df_example.iloc[:26]
df_forecast = df_example.iloc[26:]

# Make your model
formule = 'sales ~ s_curve(decay(tv, 0.3), 3) + s_curve(decay(radio, 0.2), 7) + jackpot + jan + apr + dec + ' \
          'sunday_near_drawing + event + competitor + consumer_trust'
model = smf.ols(formula=formule, data=df_train)

# mmm object maken
analyse_model = mmm(model=model, var_date=df_train.maand_jaar, df=df_train)

# Actual vs fit
analyse_model.actual_vs_fit_graph().show()

# Decompositie
analyse_model.decomposition_graph().show()
analyse_model.decompositie_sum()

# Kosten van de kanalen waarvan je de ROI wilt weten
media_dict = {'tv': 10, 'radio': 5}
analyse_model.roi(media_dict, 'sales')

# Model results
analyse_model.model_characteristics()
analyse_model.VIF()

# Analyse for adding variables
analyse_model.select_n_largest_outliers(5)
analyse_model.check_variables_to_add()

``` 

## 2. Usage Decomposition for logistic regressions over time

```python

# import modules
from onbrdng.generate_example_data import GenerateData
from onbrdng.creating_dataset import CreatingDataSet
from onbrdng.logistic_regression_decomp import LogisticDecomposition
from random import randint
from sklearn.linear_model import LogisticRegression
import plotly.io as pio

pio.renderers.default = 'browser'

# Generate data
example_data = GenerateData(10000)
df_example = example_data.generate_dataset()

# Using CreatingDataSet to clean the data
getting_data = CreatingDataSet(df_example, {})

# The sample size you want from the data and the variables (X and y) to be used
subset_size = 5000 
X_vars = ['percentage_gelezen_mails', 'geslacht', 'leeftijd', 'maanden_lid', 'kanaal_instroom', 'actie_instroom',
          'contact_vorm']
y = 'churn'

# Create the test/train
X_train, X_test, y_train, y_test = getting_data.get_train_test(y, X_vars, divided_by_max=False, scale_data=True,
                                                               add_random_int=False, add_random_cont=False, set_seed=2,
                                                               size=subset_size, test_size=0.25, random_state=12,
                                                               with_mean=True, with_std=True)

# Logistic Regression Model
model_churn = LogisticRegression().fit(X_train, y_train)

# Add a random variable to split on for this example (this should come from own data)
split_var = [randint(2018, 2022) for p in range(0, len(X_train))] 
vars_to_show = []
model_decomp = LogisticDecomposition(model_churn)
decomposition_results = model_decomp.decomposition_logistic(X_train, split_var=split_var, plot=True, y=[],
                                                             X_vars_to_show=vars_to_show,
                                                             scaling_to_mean_odds_model=True,
                                                             scaling_to_actual_odds=False)

```

## 3. Usage Multinomial Logistic Regression
```python
from onbrdng.generate_example_data import GenerateData
from onbrdng.creating_dataset import CreatingDataSet
from onbrdng.ml_models import Models, EvaluateModels
import plotly.io as pio
pio.renderers.default = 'browser'

# Generate data
example_data = GenerateData(10000)
df_example = example_data.generate_dataset()

# Select what and how much data we wanna use
getting_data = CreatingDataSet(df_example, {})
subset_size = 10000
# Selection of variables we wanna use in the model:
X_vars = ['percentage_gelezen_mails', 'geslacht', 'leeftijd', 'maanden_lid', 'kanaal_instroom', 'actie_instroom',
          'contact_vorm']
# The variable we wanna explain:
y = 'tweede_merk_keuze_merk_x_spelers'
# Get train/test datasets
X_train, X_test, y_train, y_test = getting_data.get_train_test(y, X_vars, divided_by_max=False, scale_data=False,
                                                               add_random_int=False, add_random_cont=False, set_seed=2,
                                                               size=subset_size, test_size=0.25, random_state=12,
                                                               with_mean=True, with_std=True)
# Multinomial Logistic Regression Model
model = Models(X_train, y_train)
model_mvl = model.multivariate_logistic_regression()

# Get the accuracy of the model
evalueren_model = EvaluateModels(X_train, X_test, y_train, y_test)
evalueren_model.accuracy_models([model_mvl])

# Visualize the probabilities of the model ##SELECTIE Gaat mis als data geschaald is
evalueren_model.visualize_probabilities_mvlogit(model_mvl, selection='', bin_size=0.01).show()

# We can also make selections to visualize, reminder that you need to have scale_data=False in get_train_test,
# or else you have a hard time making selections Visualize only for males that did not contact with mailing:

# Visualize only for males that did not contact with mailing:
evalueren_model.visualize_probabilities_mvlogit(model_mvl, selection='geslacht_Man == 1 & contact_vorm_mailen == 0',
                                                bin_size=0.01).show()
# Or the opposite (you can see the difference for ld):
evalueren_model.visualize_probabilities_mvlogit(model_mvl, selection='geslacht_Man == 0 & contact_vorm_mailen == 1',
                                                bin_size=0.01).show()

# Visualize the impact of each variable on a brand, merken_x_as=True gives the brands on the x_as, False the y_as
evalueren_model.determine_drivers_mvlogit(model_mvl, merken_x_as=False).show()
```


## 4. Usage Decision tree / beslisboom
```python
from onbrdng.generate_example_data import GenerateData
from onbrdng.make_html import CreateHTML
import time

# Generate some sample data
example_data = GenerateData(10000)
df_example = example_data.generate_dataset()

# Input for the tree
variables_ = ['leeftijd', 'geslacht', 'kanaal_instroom']  # The variables we want in the tree
reorder = True  # False als de volgorde moet zijn zoals in variables_, anders op meest impactvolle split op gini/mean
y = 'churn'  # de veriabelen waarvan de mean telkens wordt berekend
split_method = 'gini'  # de methode waarop gesplits kan worden (gini of mean)
min_records = 500  # min N waarna nog een split gemaakt wordt
max_integer = 5  # maximaal aantal splits bij een integer variabelen
max_nr_splits = 2  # behalve voor categorische variabelen
min_split_values = 1000  # minimale N voor een split
nr_splits = {'leeftijd': 4}  # aantal splits per variabelen (kan overschreven worden door splits)
splits = {'leeftijd': [20,25,40,60]}  # op welke waarde een split
color_reverse = True  # omkering kleuren. bij True, rood laag, blauw hoog
name_all = 'All clients'  # De naam die bij het eerste bolletje staat

# Create the actual HTML file
create_html = CreateHTML(df_example, variables_, y, split_method=split_method, min_records=min_records,
                         max_integer=max_integer, max_nr_splits=max_nr_splits, min_split_values=min_split_values,
                         nr_splits=nr_splits, splits=splits, color_reverse=color_reverse, name_all=name_all,
                         reorder=reorder)
start = time.process_time()

# Input for the created HTML filel
output_file = 'beslisboom_voorbeeld.html'  # name you wanna give it (has to end with .html)
title = 'Super Insights'  # The title on top of the html
explanation= 'One Planet, Plant it:</br> <span class="emoji">&#128514;</span>' # Text for in the explanation box
made_by = 'Onbrdng'  # Made by in the left corner of the file
create_html.build_HTML(output_file=output_file, title=title, explanation=explanation, made_by=made_by)
print(time.process_time() - start)
```

## 5. Usage Time-series forecasting with regressions and random forest

```python
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from onbrdng.forecasting_models import ForecastingModels, check_variables_to_add
import ssl
import plotly.io as pio
pio.renderers.default = "browser"

# Get some example data (you might need to run ssl._create_default_https_context = ssl._create_unverified_context:
url = 'https://raw.githubusercontent.com/SimonTeg/nlodatascience/master/example_sales_data.csv'
df_example = pd.read_csv(url)
# make a dataset for the historical data with the sales, and one to forecast the sales
df_train = df_example.iloc[:26]
df_forecast = df_example.iloc[26:]

# The formula you want to use for the model:
formule = 'np.log(sales) ~ jackpot + jan + apr + dec + sunday_near_drawing + event + competitor + ' \
          'consumer_trust + promotion'
model = smf.ols(formula=formule, data=df_train)
# if you have many variables you can use this to check what it would do to the model if you add them:
# variablesadd_df = check_variables_to_add(model, df_train)

# Create an object to analyse our model and forecast
forecasting_sales = ForecastingModels(df=df_train, df_forecast=df_forecast)

# Analyse our corrent model with actual vs fit:
forecasting_sales.actual_vs_fit_ols_graph('maand_jaar', formule).show()
# Explaining the error of the OLS model with a random forest:
forecasting_sales.actual_vs_fit_graph_rf('sales', 'maand_jaar', formule).show()
# Show the fit of the OLS model and the random forest together:
forecasting_sales.actual_vs_fit_graph_ols_and_rf('sales', 'maand_jaar', formule).show()
# Show the decomposition of both the OLS and the contribution of the random forest:
forecasting_sales.decomposition_graph_ols_rf('sales', 'maand_jaar', formule, color_kpi='deepskyblue')

# Make a forcast for a few moments (test_list) and evaluate:
forecasting_sales.forecast_drawings_ols_randomforest_oos(formule, 'maand_jaar', 'sales',
                                                         'maand_jaar', test_list=['10-2021', '11-2021', '12-2021'],
                                                         random_forest_forecast=True)

# Forecast each 'drawing' (out of sample or not) to see how the current model works:
forecasting_sales.plot_all_drawing_predictions(formule, 'sales', 'maand_jaar', out_of_sample=True)

# Forecast with new data and use the trained models with historical data:
forecasting_sales.forecast(formule=formule, date='maand_jaar', te_voorspellen='sales', show_graph=True, get_data=True,
                           random_forest_forecast=True, max_features=6, n_estimators=500)

# Only get the data from the above graph:
forecast_df = forecasting_sales.forecast(formule=formule, date='maand_jaar', te_voorspellen='sales', show_graph=False
                                         , get_data=True, random_forest_forecast=True, max_features=6, n_estimators=500)
```


## 6. Saving and loading your models
```python
import joblib
from onbrdng.generate_example_data import GenerateData
from onbrdng.creating_dataset import CreatingDataSet
from onbrdng.ml_models import Models, save_model

# Generate data
example_data = GenerateData(10000)
df_example = example_data.generate_dataset()

# Select what and how much data we wanna use
getting_data = CreatingDataSet(df_example, {})
# Selection of variables we wanna use in the model:
X_vars = ['percentage_gelezen_mails', 'geslacht', 'leeftijd', 'maanden_lid', 'kanaal_instroom', 'actie_instroom',
          'contact_vorm']
# The variable we wanna explain:
y = 'churn'
# Get train/test datasets
X_train, X_test, y_train, y_test = getting_data.get_train_test(y, X_vars, divided_by_max=False, scale_data=False)

# Multinomial Logistic Regression Model
model = Models(X_train, y_train)
model_logistic = model.logistic_regression()
model_xgb_c = model.xgboost_classifier()
model_rf = model.random_forest_classifier()

# Save models (you can test all models we use above, even MVL)
model_ = model_logistic
filename = 'model_logistic'
opmerking = 'As D. Trump might call it: The greatest model ever made'
gemaakt_door = 'The Donald'

save_model(model=model_, filename=filename, opmerking=opmerking, gemaakt_door=gemaakt_door, data_used=X_train,
           N_rows_data=15, save_estimates=True)

loaded_model = joblib.load(filename + '.joblib')
loaded_model.predict(X_test)
loaded_model.predict_proba(X_test)
``` 


## License

Copyright (c) 2023 Rumiko
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
