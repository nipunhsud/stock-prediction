def array_stats(input_array)
  sum = input_array.inject(0){|total, i| total + i}
  mean = sum / input_array.length
  median = input_array.sort[input_array.length/2]
  return sum, median, mean
end

print(array_stats([3,2,1]))

