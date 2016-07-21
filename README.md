Align Column Python Script for Notepad++
================

## Example

Original text:

    some text,20,Number,
    and more text,False,Boolean,
    text,0xFF,Number | String,
    just another line of text,8,Array,


alignColumns(right = 0):

    some text                ,20   ,Number         ,
    and more text            ,False,Boolean        ,
    text                     ,0xFF ,Number | String,
    just another line of text,8    ,Array          ,


alignColumns(right = 1):

                    some text,   20,         Number,
                and more text,False,        Boolean,
                         text, 0xFF,Number | String,
    just another line of text,    8,          Array,



alignColumns(sticky = 1):

    some text,                20,   Number,
    and more text,            False,Boolean,
    text,                     0xFF, Number | String,
    just another line of text,8,    Array,


## Usage

Note: [`Python Script for Notepad++`](http://npppythonscript.sourceforge.net/download.shtml) Plugin is required.

  1. Copy `AlignColumns.py` to `%APPDATA%\Notepad++\plugins\Config\PythonScript\scripts\` or `C:\path\to\npp\plugins\Config\PythonScript\scripts\` if you have `doLocalConf.xml` in `C:\path\to\npp\`
  2. In Notepad++ select the lines you want to align
  3. Restart Notepad++
  4. From top menu choose: `Plugins` -> `Python Script` -> `Scripts` -> `AlignColumns`
  5. In the prompt box input the desired delimited and hit the `Return` key

## Setup a keyboard shortcut

It is a good idea to assign a keyboard shortcut to this script.
Before assigning a shortcut you need to add this script to the menu:

  1. From menu open `Plugins` -> `Python Script` -> `Configuration`
  2. Select `AlignColumns.py` from list of `User Scripts`
  3. Click `Add` from above `Menu item`
  4. Click `Ok` to close the dialog
  5. Restart Notepad++
  6. Open `Settings` -> `Shrotcut mapper...` -> `Plugin commands`
  7. Select `AlignColumns` from the list and click `Modify`
  8. Choose a shortcut (I preffer `Ctrl` + `Alt` + `A`)
  9. Press `Ok`, `Close`, and you are done!


# ToDo:
  1. Add menu entries for each alignment mode
  2. Add more alignment modes

#### P.S.

  I've switched to **[Sublime Text](https://www.sublimetext.com/)**, which has a great plugin for this job - **[AlignTab](https://github.com/randy3k/AlignTab)**, thus I have no interest in improving this script any more!