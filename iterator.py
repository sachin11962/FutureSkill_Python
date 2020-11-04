# nums = [5,6,8,9,4]
#
# #print(nums[7])
#
# # for i in nums:
# #     print(i)
#
#
# #Iterator
# it = iter(nums)
#
# print(it.__next__())
#
# #one more way to use next method
# print(next(it))
#
#
# for i in nums:
#     print(i)



#### Creating own Iterator
# Print top 10 values, not all, one by one
class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

values = TopTen()

print(values.__next__())
print(values.__next__())

for i in values:
    print(i)