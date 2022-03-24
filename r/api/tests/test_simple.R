library(testit)

if(!exists("avg_list", mode="function")) {
  source("../src/simple.R")
}

test_avg_list <- function() {
  assert(avg_list(c(1,2,3,4,5)) == 3)
}

test_avg_list()
