#!/usr/bin/env python

target = 200
nways = 0

for n200 in range(target/200+1):
    for n100 in range(target/100+1):
        for n50 in range(target/50+1):
            for n20 in range(target/20+1):
                for n10 in range(target/10+1):
                    for n5 in range(target/5+1):
                        for n2 in range(target/2+1):
                            nways += 1


print nways
