library(testit)
library(arrow, warn.conflicts = FALSE)
library(dplyr, warn.conflicts = FALSE)

if(!exists("avg_price", mode="function")) {
  source("../src/storage.R")
}

test_avg_price <- function() {
  input_path <- "/tmp/input.parquet"
  output_path <- "/tmp/output.parquet"

  df <- data.frame(
    product  = c("car1", "car2", "car3"),
    brand  = c("brand1", "brand2", "brand1"),
    price = c(10000, 20000, 30000)
  )

  write_parquet(df, input_path)

  result <- avg_price(
    groupby="brand",
    field="price",
    input_path=input_path,
    output_path=output_path
  )

  result <- read_parquet(output_path)

  assert(filter(result, brand=="brand1")["price"] == 20000)
  assert(filter(result, brand=="brand2")["price"] == 20000)
}


test_avg_price()
