List_of_S%26P_500_companies.html:
	wget https://en.wikipedia.org/wiki/List_of_S%26P_500_companies

../data/constituents.csv: List_of_S%26P_500_companies.html constituents.py
	python consituents.py

../data/constituents-financials.csv: ../data/constituents.csv constituents-financials.py
	python constituents-financials.py

