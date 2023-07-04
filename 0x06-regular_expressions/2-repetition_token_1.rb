#!/usr/bin/env ruby
exp = /hb?tn/
match = ARGV[0].scan(exp)
puts match.join
