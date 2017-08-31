# Logs Analysis Project
This is a python program for the Log Analysis Project.

## Usage notes
The program analyzes the log records of a newspaper website to display the required data:
* The most popular articles
* The most popular authors
* Days with high error rates

## Installation notes
In order to run this program successfully, you need to have `VirtualBox` and `Vagrant` installed first.
Please refer to the relevant documentation for your operating system for more details.

Then install a virtual machine with a predefined PostgreSQL database by cloning or downloading this GitHub [repository](https://github.com/udacity/fullstack-nanodegree-vm). Put the files into a chosen working directory.
From your terminal, inside the `vagrant` subdirectory, run the command `vagrant up`.

Next, download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). 
Unzip the file `newsdata.sql` into the `vagrant` directory, which is shared with your virtual machine.

Download or clone the files from [this project](https://github.com/anva76/udacity-log-analysis-project) 
into a new subfolder inside the `vagrant` directory.

Then log into the virtual machine by running `vagrant ssh` inside the `vagrant` directory. To load the data, use the commands:
```
* cd /vagrant
* psql -d news -f newsdata.sql
```

Finally, run the main file:
```
* cd <your subfolder>
* python log_report.py
```
