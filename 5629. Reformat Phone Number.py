'''You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.

You would like to reformat the phone number in a certain manner.
Firstly, remove all spaces and dashes.
Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits.
The final digits are then grouped as follows:


2 digits: A single block of length 2.
3 digits: A single block of length 3.
4 digits: Two blocks of length 2 each.
The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2.

Return the phone number after formatting.'''
class Solution:
    def reformatNumber(self, number: str):
        # 1. remove spaces  and  '-'
        number = number.replace(' ','').replace('-','')

        # 2. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits.
        temp  =  []

        # if  length  of number is > 4, then extract the  first 3 letters to form a block
        while  len(number) > 4:
            temp.append(number[:3])
            number = number[3:]


        # else: according to the rule to form the final block
        length = len(number)

        if length == 2 or length  == 3:
            temp.append(number)
        else:
            temp.append(number[:2])
            temp.append(number[2:])


        return '-'.join(temp)


# print(Solution().reformatNumber("1-23-45 6"))



