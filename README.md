# colorado_covid_trends
Graphing daily data from https://covid19.colorado.gov/case-data to show trends.

Deployed at: https://colorado-covid-trends.herokuapp.com/

Until the provided Colorado case data starts graphing these trends themselves, I decided to do it myself.
Data is manually pulled from the colorado case data site into data/colorado_covid_data.csv
NOTE: The Heroku app does not need to be updated if only the data changes.  It's set up to use an external
CSV file that it pulls from github directly.