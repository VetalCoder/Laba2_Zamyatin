def get_Date(year, month, day):
    """
    >>> get_Date(2014, 12, 23)
    '2014-12-23'
    >>> get_Date(2014, 15, 23)
    Values is not correct. Try again.
    >>> get_Date(2014, 12, 34)
    Values is not correct. Try again.
    >>> get_Date(-2014, 12, 34)
    Values is not correct. Try again.
    """

    import datetime
    while True:
        try:
            tmp = datetime.date(year, month, day)           
        except ValueError:
            print('Values is not correct. Try again.')
            break
        return tmp.isoformat()


def get_temp(tmpp):
    """
    >>> get_temp(+9)
    9
    >>> get_temp(-45)
    -45
    """
    while True:
        try:
            tmp = int(tmpp)
        except ValueError:                                  
            print('Values is not correct. Try again.')
            break
        return tmp


def get_humidity(tmpp):
    """
    >>> get_humidity(-65)
    Values is not correct. Try again.
    >>> get_humidity(0)
    0
    >>> get_humidity(122)
    Values is not correct. Try again.
    """
   
    while True:
        try:
            tmp = int(tmpp)
        except ValueError:                                  
            print('Values is not correct. Try again.')
            break
        if tmp > 100:
            print('Values is not correct. Try again.')
            break  
        if tmp < 0:
            print('Values is not correct. Try again.')
            break  
        return tmp

    
def get_preasure(tmpp):
    """
    >>> get_preasure(555)
    555
    >>> get_preasure(-43)
    Values is not correct. Try again.
    """
    while True:
        try:
            tmp = int(tmpp)
        except ValueError:                              
            print('Values is not correct. Try again.')
            break
        if tmp<0:
            print('Values is not correct. Try again.')
            break
        return tmp


def get_wspeed(tmpp):
    """
    >>> get_wspeed(555)
    555.0
    >>> get_wspeed(-43)
    Values is not correct. Try again.
    """
    while True:
        try:
            tmp = float(tmpp)
        except ValueError:                              
            print('Values is not correct. Try again.')
            break
        if tmp < 0:
            print('Values is not correct. Try again.')
            break  
        return tmp	


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)   # verbose=True
