all: pushed.txt

../data:
	mkdir ../data    
    
../data/constituents.csv: ../data List_of_S%26P_500_companies.html constituents.py
	python constituents.py

valid.txt: ../data/constituents.csv ../data/constituents-financials.csv ../datapackage.json test_data.py
	python test_data.py
	echo "Datapackage is valid" > valid.txt

pushed.txt: valid.txt
	git add ../data/constituents.csv ../data/constituents-financials.csv
	git commit -m "[data][skip ci] automatic update" || exit 0
	git push publish
	echo "Update has been pushed if there was a change" > pushed.txt

.PHONY: all
