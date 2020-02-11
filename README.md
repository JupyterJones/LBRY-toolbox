# LBRY-toolbox
## https://github.com/JupyterJones/LBRY-toolbox 
Some tools I use on LBRY to get and post content. They are in the form of Bash and Python scripts. Also group of Jupyter notebooks used to create the scripts. Enjoy and subscribe to LBRY.

This repository has a complementry website on my VPS, https://lbry-toolbox.com .  lbry-toolbox.com is super new like Feb10, 2020 new, but will be growing FAST. The Site will have daily additions. It will soon have a comments and subscribe area. It is the focus of my daily activity now. 

Eventually all the contents of https://github.com/JupyterJones/LBRY-toolbox will be explained on the site more in depth. 

[https://github.com/JupyterJones/LBRY-toolbox](https://github.com/JupyterJones/LBRY-toolbox)
[https://lbry-toolbox.com](https://lbry-toolbox.com)
***
This is under developement, however many components work quite well. The goal is a Google like **Analytics** visually showing the performance of uploads. 

Now the data is stored in Sqlite3, but to learn the Elasticsearch client it will in the future be stored Elasticsearch Database.

This will be a nice resource to learn the **Nuts and Bolts** of the LBRY platform.
***


### Script to get the size of the LBRY blobfiles directory
filename:  **blobfilesize**
***
### Plays the last file entered in a directory with vlc
  **watchVID.py**
  ***
### This script runs the command *lbrynet wallet balance* 
 


filename:   **wallet** <br />
*The script directs / appends the json result into a file called       filename:  **wallet.balance** . 
wallet.balance will be used to create plots' This file once made executable may be copied
into /usr/bin and run as a cron job.*

***

### Bashfile `CREATEimage` launches BaseImage an SignBaseImage
filename:  **CREATEimage**

***

###`BaseImage` Python executable creates the BaseImage (Plot)
filename: **BaseImage**


***

###`SignBaseImage` adds the Background, Text and LBC prices to the Image created by BaseImage
filename: **SignBaseImage**
