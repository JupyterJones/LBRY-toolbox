# LBRY-toolbox
Some tools I use on LBRY to get and post content. They are in the form of Bash and Python scripts. Also group of Jupyter notebooks used to create the scripts. Enjoy and subscribe to LBRY.


***
This is under developement, howevry many components work quite well. The goal is a Google like **Analytics** visually showing the performance of uploads. 

Now the data is stored in Sqlite3, but to learn the Elasticsearch client it will in the future be stored Elasticsearch Database.

This will be a nice resource to learn the **Nuts and Bolts** of the LBRY platform.
***


### Script to get the size of the LBRY blobfiles directory
  **blobfilesize**
### Plays the last file entered in a directory with vlc
  **watchVID.py**
### This script runs the command *lbrynet wallet balance* 
 
***

  **wallet** <br />
*The script directs / appends the json result into a file called       **wallet.balance** . 
wallet.balance will be used to create plots' This file once made executable may be copied
into /usr/bin and run as a cron job.*

***

### Bashfile `CREATEimage` launches BaseImage an SignBaseImage
**CREATEimage**

***

###`BaseImage` Python executable creates the BaseImage (Plot)
**BaseImage**


***

###`SignBaseImage` adds the Background, Text and LBC prices to the Image created by BaseImage
**SignBaseImage**
