'''
Counting syllables
Define a function named count that takes a single parameter.
The parameter is a string.
The string will contain a single word divided into syllables by hyphens, such as these:
"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.
For example, the call count("ho-tel") should return 2.
'''

def count(string):
     syllable_count = 1
     for i in string:
          if i == '-':
               syllable_count +=1
     return syllable_count

def main():
     print(count("ho-tel")) #2
     print(count("cat")) #1
     print(count("met-a-phor")) #3
     print(count("ter-min-a-tor")) #4

if __name__ == '__main__':
     main()