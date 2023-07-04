#!/usr/bin/env ruby
exp = /hbt+n/
match = ARGV[0].scan(exp)
puts match.join
