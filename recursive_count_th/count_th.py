'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # save count
    th_count = 0
# I have to make the string into a list... list(str)
    str_list = list(word)
    # check to see if the word is less than the number of letters I am checking for
    if len(str_list) < 2:
        return th_count
# loop over string
    for i in range(len(str_list) - 1):  # - 1 is the last index cannot be == to th
        # and then compare list[i] + list[i + 1] == 'th'
        if str_list[i] + str_list[i + 1] == 'th':
            # if it does add it to a count
            th_count += 1
    return th_count


'''
If I pass in the word 'the' how would this run...
    Output: 1
If I pass in the word 'The' how would this run...
    Output: 0
If I pass in 'th-the' how would this run...
    Output: 2? I do not know if I should be worried about non alpha characters
If I pass in 'word' how would this run...
    Output: 0
If I pass in 'this is not a single word' how would this run...
    Output: 1

So we have a word, which I can make iterable by converting it into an array...
Then we could use the sliding window method to find where th exists...and add that to a count...
-- That's iterative... which I can try first.

For iterative: 
I have to make the string into a list... list(str)
loop over string
and then compare list[i] + list[i + 1] == 'th'
if it does add it to a count

For recursive: I can take ^.... and return 1?
'''

if __name__ == '__main__':
    word = 'this is not a single word'
    print(f'Output of count_th: {count_th(word)},\nexpected output: 0')
