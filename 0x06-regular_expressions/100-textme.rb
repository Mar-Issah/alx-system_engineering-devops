#!/usr/bin/env ruby
exp = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
match = ARGV[0].scan(exp)
puts match.join(',')
