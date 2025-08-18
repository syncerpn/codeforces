# good problem
# for a given root r, the number of operations needed to make all other nodes connected to r
# equal the number of leaves not directly connected to r at the beginning
# the reason is that, we have to visit all those leaves from r
# so just need to count the number of leaves at first
# and check number of leaves not directly connect to every node as the root
a = input().lower()
b = input().lower()
print(0 if a == b else (1 if a > b else -1))