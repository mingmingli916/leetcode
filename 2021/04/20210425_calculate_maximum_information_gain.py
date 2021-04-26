"""
Given a group of values, the entropy of the group is defined as the formula as following:

H(X) = -\sum_{i=1}^n P(x_i) \log_2 P(x_i),  \sum_{i=1}^n P(x_i) = 1


where P(x) is the probability of appearance for the value x.

e.g.

the input group:  [1, 1, 2, 2]

the probability of value 1 is:  2/4 = 1/2
the probability of value 2 is:  2/4 = 1/2

Therefore, its entropy can be obtained by:  - (1/2) * log2(1/2) - (1/2) * log2(1/2) = 1/2 + 1/2 = 1

This exercise, however, is aimed to calculate the maximum information gain
that one can obtain by splitting a group into two subgroups.
The information gain is the difference of entropy before and after the splitting.

For a group of L, we divide it into subgroups of {L_1, L_2}, then the information gain is calculated as following:

information_gain(L, L_1, L_2) = H(L) - H(L_1) \frac{size(L_1)}{size(L)}  - H(L_2) \frac{size(L_2)}{size(L)}

The overall entropy of the splitted subgroups {L_1, L_2} is the sum of
entropy for each subgroup weighted by its proportion with regards to the original group.


Problem Description
In this exercise, one can expect a list of samples on Iris flowers.
Each sample is represented with a tuple of two values: <petal_length, species>,
where the first attribute is the measurement on the length of the petal for the sample, and
the second attribute indicates the species of sample. Here is an example.



The task is to split the sample list into two sublists, while complying with the following two conditions:

The petal_length of sample in one sublist is less or equal than that of any sample in the other sublist.
The information gain on the species attribute of the sublists is maximal among all possible splits.

As output, one should just return the information gain.

In addition, one can expect that each value of petal_length is unique.



In the above example, the optimal split would be L1 = [(0.5, 'setosa'), (1.0, 'setosa')] and
L2 = [(1.5, 'versicolor'), (2.3, 'versicolor')].
According the above formulas, the maximum information gain for this example would be 1.0.

Note:  For certain languages (e.g. Java), there is no build-in type of tuple.
As a reuslt, to make the input more general, we decompose the input into two lists:
[petal_length] [species] respectively, where the petal_length would be of float value and the species is of string.
The elements in the petal_length list and species list are associated to each other one by one by order.
"""
from typing import List
import math
import collections


class Solution:
    def calculateMaxInfoGain(self, petal_length: List[float], species: List[str]) -> float:
        petal_species = zip(petal_length, species)
        petal_species = sorted(petal_species, key=lambda x: x[0])
        sorted_species = [x[1] for x in petal_species]

        max_gain = 0
        h = self.calculateEntropy(sorted_species)
        l = len(sorted_species)

        for i in range(1, len(sorted_species)):
            l1 = sorted_species[:i]
            l2 = sorted_species[i:]
            h1 = self.calculateEntropy(l1)
            h2 = self.calculateEntropy(l2)
            gain = h - h1 * len(l1) / l - h2 * len(l2) / l

            if gain > max_gain:
                max_gain = gain

        return max_gain

    def calculateEntropy(self, input) -> float:
        length = len(input)
        counter = collections.Counter(input)
        ans = 0
        for i in counter:
            p_i = counter[i] / length
            ans += -p_i * math.log(p_i, 2)

        return ans


if __name__ == '__main__':
    petal_length = [0.5, 2.3, 1.0, 1.5]
    species = ["setosa", "versicolor", "setosa", "versicolor"]

    solution = Solution()
    ans = solution.calculateMaxInfoGain(petal_length, species)
    print(ans)
