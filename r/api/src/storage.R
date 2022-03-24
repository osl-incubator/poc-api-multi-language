POCAPI_URL <- Sys.getenv("POCAPI_URL", unset="http://localhost:6666")

library(httr)

avg_price <- function(groupby, field, input_path, output_path){
    url <- paste(POCAPI_URL, "/storage/avg-price", sep="")
    input_data <- list(
        groupby = groupby,
        field = field,
        input_path=input_path,
        output_path=output_path
    )
    r <- POST(url, body = input_data, encode = "json")
    return(content(r, as="parsed"))
}
