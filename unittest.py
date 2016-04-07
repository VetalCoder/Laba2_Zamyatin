import unittest

def get_Date(year, month, day):
    import datetime
    while True:
        try:
            tmp = datetime.date(year, month, day)           
        except ValueError:
            return('Values is not correct. Try again.')
            break
        return tmp.isoformat()


def get_temp(tmpp):
    while True:
        try:
            tmp = int(tmpp)
        except ValueError:                                  
            return('Values is not correct. Try again.')
            break
        return tmp


def get_humidity(tmpp):
    while True:
        try:
            tmp = int(tmpp)
        except ValueError:                                  
            return('Values is not correct. Try again.')
            break
        if tmp > 100:
            return('Values is not correct. Try again.')
            break  
        if tmp < 0:
            return('Values is not correct. Try again.')
            break  
        return tmp

    
def get_preasure(tmpp):
    while True:
        try:
            tmp = int(tmpp)
        except ValueError:                              
            return('Values is not correct. Try again.')
            break
        if tmp<0:
            return('Values is not correct. Try again.')
            break
        return tmp


def get_wspeed(tmpp):
    while True:
        try:
            tmp = float(tmpp)
        except ValueError:                              
            return('Values is not correct. Try again.')
            break
        if tmp < 0:
            return('Values is not correct. Try again.')
            break  
        return tmp	

class Test(unittest.TestCase):
	def test_get_DAte(self):
		self.assertEqual(get_Date(2014, 12, 23),'2014-12-23')
		self.assertEqual(get_Date(2014, 15, 23),'Values is not correct. Try again.')
		self.assertEqual(get_Date(2014, 12, 34),'Values is not correct. Try again.')
		self.assertEqual(get_Date(-2014, 12, 34),'Values is not correct. Try again.')
	
	def test_get_temp(self):
		self.assertEqual(get_temp(+9), 9)
		self.assertEqual(get_temp(-45), -45)
		
	def test_get_humidity(self):
		self.assertEqual(get_humidity(-65),'Values is not correct. Try again.')
		self.assertEqual(get_humidity(0),0)
		self.assertEqual(get_humidity(122),'Values is not correct. Try again.')
		
	def test_get_preasure(self):
		self.assertEqual(get_preasure(555), 555)
		self.assertEqual(get_preasure(-43), 'Values is not correct. Try again.')
		
	def test_get_wspeed(self):
		self.assertEqual(get_wspeed(555),555.0)
		self.assertEqual(get_wspeed(-43),'Values is not correct. Try again.')
	
	
if __name__ == "__main__":
    unittest.main()   
