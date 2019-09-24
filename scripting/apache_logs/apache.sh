#!/bin/bash

echo ">>> apache"
# awk -F '[ "]+' '$7 == "/" { ipcount[$1]++ } END { for (i in ipcount) { printf "%15s - %d\n", i, ipcount[i] } }' apache.log

# 1. Surface statistics of HTTP response codes: What percentage of requests return code 200, 400 etc?
cat apache.logz | awk '{print $9}' | sort -n | uniq -c

# 2. Surface statistics on what kind of browsers tried to access the website.

# 3. What is the average number of requests per day?

# 4. You implemented a rating feature on the website and users rate the website significantly worse between 6pm and 9pm. 
# Your boss thinks this is because there are more users during those hours which slows down the response time. 
# Evaluate whether:
# - This timeframe actually experiences most users.
# - The response time is actually slower during this timeframe.