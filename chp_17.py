#1
"""Using the terminal (Ubuntu)"""
"""
$ grep Dutch zen.txt
"""

#2
"""Using the terminal (Ubuntu)"""
"""
$ echo Arizona 479, 501, 870. California 209, 213, 650. | grep [[:digit:]]
"""

"""Using Python"""
import re

string = "Arizona 479, 501, 870. California 209, 213, 650."

find = re.findall("\d",
                  string,
                  re.IGNORECASE)

print(find)

#3
"""Using the terminal (Ubuntu)"""
"""
$ echo The ghost that says boo haunts the loo. | grep -o .oo
"""

"""Using Python"""

import re

ghost = "The ghost that says boo haunts the loo."

look = re.findall(".oo",
                  ghost,
                  re.IGNORECASE)

print(look)
