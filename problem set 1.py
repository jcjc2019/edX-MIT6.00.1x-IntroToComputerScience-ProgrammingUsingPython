# MIT problem set 1-problem 1
# count number of vowels in a string
def vowel_count(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count = count+1
    print "Number of vowels:", count
    
vowel_count ('azcbobobegghakl')

# MIT problem set 1-problem 2
# count the number of occurrence of a substring in a string
s = 'azcbobobegghakl'
sub = 'bob'

count = 0
bob_len = len(sub)
for i in range(len(s)):
    if s[i:i+bob_len] == sub:
        count += 1
print "Number of times bob occurs is:", count

# MIT problem set 1-problem 3
# count the number of three items in an order

def item_order(order):
    voc = ["salad", "hamburger", "water"]
    salad_num = order.count(voc[0])
    ham_num = order.count(voc[1])
    wat_num = order.count(voc[2])
    combine = "salad:" + str(salad_num)+ " "+ "hamburger:"+ str(ham_num) +" "+ "water:"+ str(wat_num)
    output = str(combine)
    print output
    
item_order('salad water hamburger salad hamburger')
item_order('hamburger water hamburger')
