POCAPI_URL <- Sys.getenv("POCAPI_URL", unset="http://localhost:6666")

library(httr)

avg_list <- function(values){
    url <- paste(POCAPI_URL, "/simple/avg-list", sep="")
    r <- POST(url, body = list(values = values), encode = "json")
    return(content(r, as="parsed"))
}
