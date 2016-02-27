# Run the scripts
These **Linux** scripts scrape data from Wikipedia page about S&P500 and computes a datapackage augmented with yahoo webservices.

They have been tested under Debian Jessy.


## Install the dependencies
The scripts work with some python and shell scripts glued together with a Makefile.

Install the required python libraries :

    cd scripts
    pip install -r requirements.txt

You can also work on a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) .

	
## Run the scripts

	make