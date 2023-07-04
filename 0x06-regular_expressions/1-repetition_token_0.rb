#!/usr/bin/env ruby
exp = /hbt{2,5}n/
match = ARGV[0].scan(exp)
puts match.join