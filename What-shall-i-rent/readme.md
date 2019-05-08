### What Shall I rent ###

A basic tool that will pull all rental property data from a web scraper based city and radius and save to a csv output file. Results will be stored in different databases depending on their postcode

### Modules ###
WebScraper: Scrapes a given property website for as much data as possible. Data can then be filtered with the Data Filter



### To develop ###
# Modules #
PostGreSQL: communicate with postgresql database. Database login will be passed as a command line argument with the program initialisation
Data Filter: filters down the data from the api to cut out the unwanted gubbins.
# Adjustment to main program #
Convert city and radius variables to command line arguments
have url output dynamically change based on the website chosen
change variable names to be more appropriate
compress unnecessary variables to single lines
replace key features for loop with a cleaner method

