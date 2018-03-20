# Password list generator v 0.01

## Work algorithm:
Uses a dictionary of words (by default - list.txt) and a list of delimiter("delimiters" in main.cfg)
Combines these two lists passwords and delimeters. In passwords uses from 2 to max_words_on_pass (param in main.cfg) words

## How to use:
Type: ```python main.py```

- you get a list of passwords in the file "passwords_list.txt"

Type: ```python main.py -o output_file```

- you get a list of passwords in the file "output_file"

## Example:

###List.txt:
```
CompanyName
WIFI
WPA
PSK
```
    
###Delimeters:
```-,_, , ```  : dash, underline, space, no separation


###Result:

```
WPA.PSK
CompanyName.WIFI-WPA
CompanyName.WIFI-PSK
WIFI.WPA-PSK
CompanyName.WIFI-WPA-PSK

and other (37500 variations)
```
