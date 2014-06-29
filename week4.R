# 1. Three ways to assign
one <- 'one'
two = 'two'
assign('three', 'three')

# 2. sum and is.na
hasNA = c('if', NA, 'then', NA, 'else', NA, 'finally', NA, NA)
toBeSummed = c()
for(v in hasNA) if (is.na(v)) toBeSummed <- c(toBeSummed,1)
sum(toBeSummed)

# 3. library vs require
# I would use require if I needed to gracefully check for the package. 
# I could check whether the package exists using require and then install it

if( require('accelerometry') ){
  print('Package accelerometry is loaded')
} else {
  print('Warning: You need to install the accelerometry package first ')
}

tryCatch({
  library('accelerometry')
}, error = function(e){
  print('Error: you need to install the accelerometry package first')
}
  )