#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
    The constant is a, and n is n.
    O(n^3 - c + n ^2) => O(n) ???

b)
    for i in range(n) => O(n)
        j = 1 constant
        while j < n: O(n)
            j *= 2 constant?
            sum += 1 doesn't matter?

c)
    def bunnyEars(bunnies):
        if bunnies == 0:
            return 0
        return 2 + bunnyEars(bunnies-1) recursion...

        if there are n bunnies... 2 + n ^ n
        so... O(c ^ n)?

## Exercise II

Input: Number of floors, and a breaking point.
Output: Number of floors until the breaking point (highest amount of floors until a breaking point)
Creating: ... a function?

Some questions:
    How will I know the egg broke. If I'm on floor 60, I might not be able to tell the egg broke back on floor 1.
    Does the building label it's floors for me?
    If it doesn't how will I keep count so I can tell when I should stop throwing eggs.

    I will assume:
    That I can access outside of the building,
    call a friend with a basket,
    we have cell phones with full batteries,
    and that I have to conut the floors myself.

    First I'd call up a friend to help me with the experiment. I would ask them to stay outside of the building and to check for broken eggs. If the egg is not broken add it to their basket, else if an egg does break to call me and tell me to stop throwing my eggs. Then I would ask my friend to count how many eggs are in the basket.
    Then I would know that as many eggs are in the basket, is how many floors I can climb without breaking an egg.
    Then we would go and have brunch, and I would leave my never ending stock of eggs on the floor that they break for anyone that needs to release some energy.