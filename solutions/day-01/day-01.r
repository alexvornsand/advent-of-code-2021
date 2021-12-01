# advent of code
# day 1

# part 1
numbers <- scan('day-01.txt')

countIncreases <- function(numbers, partTwo = F){
  if(partTwo == F){
    sum(numbers[2:length(numbers)] > numbers[-length(numbers)])
  } else {
    sum(
      numbers[2:(length(numbers) - 2)] +
      numbers[3:(length(numbers) - 1)] +
      numbers[4:length(numbers)] >
      numbers[1:(length(numbers) - 3)] +
      numbers[2:(length(numbers) - 2)] +
      numbers[3:(length(numbers) - 1)]
    )
  }
}
countIncreases(numbers)

# part 2
countIncreases(numbers, partTwo = T)
