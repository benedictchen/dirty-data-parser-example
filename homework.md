# Back End Candidate Homework

### Scenario:
We receive a lot of data from different sources.  That data comes in and after we process it, we need to fuzz and sometimes even fix the data formats.  The folder `./data` has multiple data sets within it that need to be parsed, reduced & normalized, and fuzzed. Each file in `./data` would be a json file that represents a request received. Each request file can contain multiple data sources, where each data source might be of different format(json, xml ,csv).  

### What we want:

Design and implement a service that will watch the `./data` folder, process all items in it (and that are placed in it), and perform the following actions.
Some notes about the data folder.
* All data in the data folder will be in json format, whose schema details are defined in the file `format.json`
* JSON data can contain parts (denoted by the key `values`) that are xml, csv, or json
* Not all data files will be properly formed

* Parse the data
  * Prepare the data to be able to find specific elements within it.  
  * Fix any parse errors that arise.
    * Improperly formatted json
    * Improperly formatted xml
* Anonymize the data in the data files and save the newly created data file into the `./anon_data` folder
  * First Name
  * Last Name
  * DOB
  * Address
  * Phone Number
  * Replace first name, last name, and addresses with random selections from the files in `./replacement_data`.  
  * Save the anonymized data files in `./anon_data`
* Reduce and Normalize the data in a database
  This is left open-ended on purpose, make assumptions and use your best judgement.
  The data should be saved in the database such that we can query asking for applicant data.
  Some queries that can be expected are,
    * Get all applicant data on a date range.
    * Get an individual applicant's data.

#  Assignment:
* Prepare a presentation outlining your architecture, solution and trade-offs.
  * Feel free to have fun with this!
* Load your code up to a git repo and share it with us.
  * We wanna see the code!
* Host the project somewhere or be prepared to run it on your machine.
  * Please don't spend any money, you can use free tier AWS, Azure, or GCP
  * Or, you know, display it on your machine.
* Be prepared to answer a bunch of questions about how and why you did things.


You will present your solution to several members of various Zest teams. Most will have engineering background in various disciplines ranging from Software to Machine Learning. Some will have strong ideas or opinions about parsing and other technologies.  A few will have no technical skills at all.  Be prepared to cater to all audiences.  After the presentation, we will have a short Q&A/working session with the group. There is a hard-stop at the 30-minute mark. We advise allocating maximum 10 minutes for the presentation, 5-10 minutes for the demo and to reserve the remaining time for questions.

Setup: Our conference rooms will have all of the necessary computer and a/v equipment for the presentation and an internet connection so you can access remote infrastructure. Please email your Slides, Powerpoint, or PDF presentation a day before your interview so we can have it up and running in the conference room when you arrive.
