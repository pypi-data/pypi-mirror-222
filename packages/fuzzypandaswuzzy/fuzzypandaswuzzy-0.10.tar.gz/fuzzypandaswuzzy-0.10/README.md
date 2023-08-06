# Fuzzy Comparison Utilities for DataFrame Columns

## pip install fuzzypandaswuzzy 

#### Tested against Windows 10 / Python 3.10 / Anaconda 

	
```python

This module provides a function to perform fuzzy comparison between two columns of a DataFrame using the RapidFuzz library.
It also extends the DataFrame class to add a method for fuzzy comparison between two columns.

Module dependencies:
	- pandas (pd)
	- numpy (np)
	- RapidFuzz (from rapidfuzz import process, fuzz)

Usage:
	import pandas as pd
	from rapidfuzz import fuzz
	from fuzzypandaswuzzy import pd_add_fuzzy_all
	pd_add_fuzzy_all()

	df = pd.read_csv(r"arcore_devicelist.csv")
	df2 = df.d_fuzzy2cols(scorer=fuzz.QRatio) # compares the first 2 columns

			   aa_value1   aa_match  aa_index_v2     aa_value2
	0            Mobicel  82.352943         1978    Mobicel_R1
	1            Hyundai  66.666664         5425         Cunda
	2               OPPO  66.666664        10102         P7PRO
	3            samsung  80.000000          745      samseong
	4               DEXP  66.666664         1174            EP
				  ...        ...          ...           ...
	22523          TECNO  76.923080          587      TECNO-i5
	22524          STYLO  83.333336         7272       STYLOF1
	22525  GarantiaMOVIL  52.631580        16788        armani
	22526  Cherry_Mobile  72.000000         3510  Cherry_Comet
	22527         SANSUI  53.333332         3465     ASUS_P00I


Note:
	The 'scorer' parameter in the fuzzy_compare function and d_fuzzy2cols method accepts a scoring function from the RapidFuzz library
	(e.g., fuzz.WRatio, fuzz.QRatio, etc.). If no scorer is specified, the default scorer used is fuzz.QRatio.

	For more information on the RapidFuzz library, visit https://github.com/maxbachmann/rapidfuzz.	
```