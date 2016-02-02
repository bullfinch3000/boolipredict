## boolipredict

Gissa priser på bostäder baserat på historisk data från Booli mha SVM epsilon-regression med en RBF-kernel.

Repot innehåll Python-script som:
* hämtar data från Boolis API (collect.py)
* lagrar datat lokalt mha ORM:et Peewee och en SQLite-databas (models.py)
* förbehandlar datat och lagrar det i en csv-fil (preprocess.py)
* gör en grid-search för att hitta de bästa SVM-parametrarna (parameter_search.py)
* kors-validerar träningsresultatet (cross_validate.py)
* tränar en slutlig modell och spar resultatet (train.py)
* tillgängliggör modellen via ett kommandoprompt-verktyg (predict.py)

För att använda, ladda ned repot och kör följande kommando från en terminal:

python predict.py livingArea rooms floor rent areaName
t.ex.: python predict.py 48 2 2 2800 Abrahamsberg