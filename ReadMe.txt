Unzip PYTHON and SQL zipfile

Python Jupyter Notebook:
1) PRAT_Comments.ipynb  -- web server is still down, please start at wsb_comments.csv
2) wsb_comments.csv, export from PRAT_Comments.ipynb
3) VECTOR_SENTENCE.ipynb quick run to create sentences
	Can just use the VECTOR_SENTENCE.csv if you don't want to run this.
4) PRAT_VALID_AUTHORS.ipynb here you can use wsb_comments.csv but for fast results use subset_100.csv or subset_1000.csv.
5) PRACT_VALID_SYMPTOMS.ipynb here you can use wsb_comments.csv but for fast results use subset_100.csv or subset_1000.csv.

MSSQL Server 2019"
1) Restore sarscov2.bak over a new database, name doesn't matter.
2) Import csv:
	author_valid
	symptoms_valid
	wsb_comments
3) In a new query window execute:
	exec DATEUSP_authorStartDate
	exec USP_symptoms
	exec USP_symptomsDATE_Views
* the USPs will clean old data. If you want a clean run just create a new DB and run same name .SQL files; then import the CSVs.
