
#!/usr/bin/env python3

"""currency.py: Currency converter.

__author__ = "Hu Ruihua"
__pkuid__  = "1800011843"
__email__  = "1800011843@pku.edu.cn"
"""

from urllib.request import urlopen
    
def exchange(currency_from, currency_to, amount_from):
    """定义exchange函数
    """
    original_url = "http://cs1110.cs.cornell.edu/2016fa/a1server.php?from = "\
        +currency_from+"&to = "+currency_to+"&amt = "+str(amount_from)
    
    doc = urlopen(original_url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode("ascii")
    bool_value = jstr.replace("true","True")
    jstr = eval(bool_value)
    
    return jstr["to"]
   
    
def test_exchange():
    
    assert "2.1589225 Euros" == exchange("USD","EUR",2.5)
    assert "289.53 Argentine Peso" == exchange("USD","ARS",2.5)
    assert "278.4975 Japanese Yen" == exchange("USD","JPY",2.5)       
        
def main():
    a = input("Please input the currency on hand: ")
    b = input("Please input the currency to convert to: ")
    c = str(input("please input amount of currency to convert:"))
    test_exchange()
    print(exchange(a,b,c)) 

    
if __name__ == '__main__':
    main()
