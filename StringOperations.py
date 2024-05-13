stringValue='это моя строка'
print("My string exersize will be here! Let's go!\n\n"+
      '1. Print the fisrt symbol of the string, please.\n'+' '*3+
      'I see at least two ways to output first symbol af any string.\n'+' '*3+
      'We can use simple "print(str[0])" like this: "'+stringValue[0]+'".\n'+' '*3+
      'Or more difficult and not optimised method "print(str[::14])", where "14" is greater or equal of the string '
      'length.\n'+' '*3+
      'Result will be the same: "'+stringValue[::14]+'"\n'+"-"*30)

print('2. Print the last symbol of the string by the negative index.\n'+' '*3+
      'The last symbol with "print(str[-1])" is: "'+stringValue[-1]+'"\n'+' '*3+
      "But we can't use this easiest way and we should use something like"+'"print(str[::-1945]" and\n'+' '*3+
      'result be the same: "'+stringValue[::-1945]+'"!\n'+' '*3+
      '"1945", as we already know, is greater or equal of the string length.\n'+"-"*30)
print('3. Output substring of the string from the third symbol till the five symbol.\n'+' '*3+
      "We would like to be sure, so let's enumerate this!\n"+' '*3+
      '1234567890\n'+' '*3+
      stringValue+'\n'+' '*4+
      '"'+stringValue[2:5]+'"\n'+' '*3+
      'Well done, commander! Go ahead! ))\n'+"-"*30)
print('4. Do reverse output for the string.\n'+' '*3+
      'We use standard way for it ("print(str[::-1])"): "'+stringValue[::-1]+'"\n'+' '*3+
      'What about "print(str[-1:-15:-1])": "'+stringValue[-1:-15:-1]+'"\n'+' '*3+
      'Very strange but "-15" is working also!\n'+"-"*30)
print('5. Please output the string length.\n'+' '*3+
      'The length of the string is: '+str(len(stringValue))+'\n'+"-"*30)
print("6. Concatenate strings 'это новая строка' и 'это моя строка' and print it.\n"+' '*3+
      'First of all I tried to do this like a newbie ("print(\'это новая строка \' + \'это моя строка\')")\n'+' '*3+
      'But I did this without google in the end with "str.replace(\'моя\',\'новая\')+\' \'+str"\n'+' '*3+
      'The result is: "'+stringValue.replace('моя','новая')+' '+stringValue+'"\n'+' '*3+
      'I think here should be a space between strings. But we need to ask customer about this! )\n'+"-"*30+'\n'+
      'Best regards,\nOleg!')
