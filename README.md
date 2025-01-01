
![20250101 093539-Wed January 01 2025 0935AM](https://github.com/user-attachments/assets/231c9ffc-af83-400b-ad39-a0c3ea328d35)


QuickJournal is a simple journaling application that allows you to write and save text entries with ease. It features a modern GUI with transparency and enhanced functionality.
Configuration File Setup

QuickJournal uses a configuration file (config.ini) to manage multiple paths. These include:
Paths Section:

    save_path:
        Specifies the directory where journal entries will be saved.
        Defaults to the current working directory if not set.

    signatures_path:
        Specifies the directory containing signature files.
        Defaults to a signatures folder in the current directory if not set.

The configuration file will look like this:

[Paths]
save_path = /path/to/save/directory
signatures_path = /path/to/signatures/directory

You can dynamically change these paths through the File menu in the application:

    Change Save Location: Select a directory for saving journal entries.
    Change Signatures Location: Select a directory for signature files.

Features and Usage
Writing and Saving an Entry:

    Text Input:
        Enter your text in the provided text area.
    Title:
        Optionally, specify a custom title in the title box. If left empty, the filename will default to the current timestamp (e.g., January.01.2025.12.00.00.txt).
    Signatures:
        Use the dropdown menu to select a signature. If "No Signature" is selected, no footer will be added.
    Save:
        Click the "Save Entry" button. The entry will be saved to the configured save_path.

Menu Options:

    About:
        View information about QuickJournal, its functionality, and updates.

    Change Save Location:
        Change the save directory. This updates the save_path in the configuration file.

    Change Signatures Location:
        Change the signatures directory. This updates the signatures_path in the configuration file.

    Config Info:
        View the current paths for save_path and signatures_path.

Signatures

    Add .txt files to the directory specified in the signatures_path.
    These files will automatically appear in the dropdown menu for selection.







## Support

Drop a tip

    (BTC) address bc1qnpjpacyl9sff6r4kfmn7c227ty9g50suhr0y9j
    
    (ETH) address 0x94FcBab18E4c0b2FAf5050c0c11E056893134266
    
    (LTC) address ltc1qu7ze2hlnkh440k37nrm4nhpv2dre7fl8xu0egx



![noarche's GitHub stats](https://github-readme-stats.vercel.app/api?username=noarche&show_icons=true&theme=transparent)
