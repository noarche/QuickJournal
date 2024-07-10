# QuickJournal

QuickJournal is a simple journaling application that allows you to write and save text entries with ease.



## Prepare Configuration and Footer Files:


### Configuration File:

Create a file named config.txt in the same directory as the QuickJournal script.

Inside config.txt, specify the directory where you want to save your journal entries. 

If you leave this file empty or specify an invalid path, QuickJournal will save your entries in the current working directory.


### Optional Footer File:

Create a file named footer.txt in the same directory as the QuickJournal script.

Write any text you want to be appended to the bottom of every saved entry in footer.txt. This step is optional.


## Saving Your Entry:

After typing your journal entry, click the "Save Entry" button located below the text box.

When you click the "Save Entry" button, the following actions occur:

The current date and time are captured.

The text you entered is read from the text box.

The first word of your entry is extracted.

A filename is created using the format Month Day Year HourMinute AM/PM - FirstWord.txt.

If a footer.txt file exists, its content is appended to your entry.

Your entry (with the optional footer) is saved to the directory specified in config.txt or the current working directory.

A message box confirms the save location.

The text box is cleared for your next entry.


![screenshot](https://github.com/noarche/QuickJournal/blob/main/Screenshot.jpg?raw=true)


## Support

Drop a tip

    (BTC) address bc1qnpjpacyl9sff6r4kfmn7c227ty9g50suhr0y9j
    
    (ETH) address 0x94FcBab18E4c0b2FAf5050c0c11E056893134266
    
    (LTC) address ltc1qu7ze2hlnkh440k37nrm4nhpv2dre7fl8xu0egx



![noarche's GitHub stats](https://github-readme-stats.vercel.app/api?username=noarche&show_icons=true&theme=transparent)
