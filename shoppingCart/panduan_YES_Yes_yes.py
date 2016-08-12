import re



charge_or_not = input('输入yes进行充值，输入q退出：')
charge_re = re.match(r'(Yes|YES|yes|y)', charge_or_not)
if charge_re:
    print('is YES Yes yes y.')

