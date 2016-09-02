found out about the [median of median algorithm](https://en.wikipedia.org/wiki/Median_of_medians) from [this course](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/)

here's an interesting discussion
https://news.ycombinator.com/item?id=7415708

want to try implementing the diff algorithms in a TDD fashion to compare actual
running time, and to maybe use diff languages to implement them


setup
=====
- use python3. install requirements.txt
- then just run py.test


notes
=====
- turns out median of median = quickselect + smart selection of pivots to avoid worst case. let's implement quickselect first

- now let's skip hypothesis test and build up quickselect bit by bit
