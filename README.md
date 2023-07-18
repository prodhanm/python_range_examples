The way the range function (range()) is used as a self iterating tool to generate numbers sequentially. The formula to how range() is used is as such:

        range(start, stop, step)
        default: range(stop)
        default step = 1
        stop = value -1

As is with the range(), there is a starting point and in that
starting point, the function calls the first value as that
starting point. When the range() executes, at a starting point 
value, then it stops at the point, where if stop = 10. then the
code stops at 9 as the displaying value. This is to know that the 
limt is at 10 but the value is less than the value, that is why
the display of the value is value -1 at stop. 

The step is always defaulting at 1, because without a specified
step value. it will assume that each number is +1 after the next
value. If the starting point is 1, the next value is 2 and then 3, all the way up to the stop value. 

Another feature of the range(), is that the function by itself will not display result without utilzing a method for the range function to display. That can be done, utilizing the data set function calls, such as list(), tuple(), set().