from itertools import combinations_with_replacement
from numpy import ndarray, array
from os import path, system
# My first shitshow module in python (but hey give it a try, I make use of these functions a lot)
# Author: Demiz
# Other names of Author: Emmanuel J. Kweh, Mizbehave, Eddie, Joshua



def frontstrip(text, char=" "):
    """
This function eliminates the string passed as argument (" " as default) from the front of a string.
ex. frontstrip("PHello WorldP")
output: Hello WorldP
    """
    if text[0] == char:
        text = text[1:]
    return text if text[0] != char else frontstrip(text)



def justify(line=""):
    """
This function takes a long str text as input and returns a list of each line justified.
:param line: str (line=" " as default)
:return: list of justified line(s) of text
    """
    lines = []
    while len(line) > 90:
        line_breaks = frontstrip(line[:90])
        line = line[90:]
        lines.append(line_breaks+"-" if line[0] != " " != line_breaks[-1] else line_breaks)
    lines.append(line.strip())
    return lines



def degenerator(value, method="prime"):
    """
this function(generator) returns a range beginning at index 2 when the method param equals "prime" (default argument),
returns a range of integers beginning at index 1 when method = "integer", and returns a full generator object of an
iterable when method = "iterable".
exp: degenerator(value=45, method="integer")
output: <generator object degenerator at 0x7ff595842900>
:param value:
:param method:
:return: generator object
    """
    if method == "prime":
        for i in range(2, value+1):
            if i == value:
                continue
            yield i
    elif method == "integer":
        for i in range(1, value+1):
            yield i
    elif method == "iterable":
        for i in value:
            yield i



def factors(value, all_factors=True, method="integer"):
    """
This function built by demiz himself returns factors or a factor of a number.
value represent the number whose factor(s) is to be found, all_factors returns a list of factors if True else an integer,
method specifies the data type, 'integer', 'prime' and iterable.
:param value:
:param all_factors:
:param method:
:return: list or integer
    """
    factor = []
    for i in degenerator(value, method):
        if value % i == 0 and all_factors:
            factor.append(i)
        elif value % i == 0:
            factor = i
            break
    return None if factor == [] else factor



def prime(value):
    """
This function returns True if the number input is prime else False.
value is the number whose prime is to be checked
:param value:
:return: boolean
    """
    if value < 2 or factors(value, method="prime", all_factors=False):
        return False
    return True



def lowercasearray(arr):
    """
This function converts all elements of an array into lowercase.
:param array:
:return modified array:
    """
    new_array = []
    if type(arr) == ndarray:
        for i in arr:
            new_array.append(i.lower())
        arr = array(new_array)
        return arr
    raise TypeError(f'{arr} is not an array')



def squeezedarray(arr):
    """
This function removes space(s) out of each array element and return
a modified array.
:param arr (array):
:return new array:
    """
    new_array = []
    if type(arr) == ndarray:
        for i in arr:
            new_array.append(i.replace(' ', ''))
        arr = array(new_array)
        return arr
    raise TypeError(f'{arr} is not an array')



def text_file_handler(location, content):
    """
This function creates/append to a text file, location is the path of the file
while content is what should be written in the text file.
:param location (str - path of file):
:param content:
:return a new text file or appended contents to the file:
    """
    if path.exists(location):
        with open(location, 'a') as file:
            file.write(content+'\n')
    else:
        with open(location, 'w') as file:
            file.write(content+'\n')



def module_downloader(module):
    """
This function is used to download modules.
:param name of module:
:return None:
    """
    system(f'pip install {module} -qq')



def comma(number):
    """
This function is used to add comma to numbers eg. input = 2300, output = 2,300.
:param number (int, float, str):
:return str: number with added comma(s):
    """
    result_list = [i for i in str(number).split('.')[0]]
    if len(result_list) > 3:
        repeat_commas = len(result_list) // 3
        repeat_commas = repeat_commas if len(result_list) % 3 != 0 else repeat_commas - 1
        for comma in range(repeat_commas):
            comma = comma * -4 - 3
            result_list.insert(comma, ',')
        number = ''.join(result_list)
    return number
