## Scripts

### bash script
#### usage: checklogs.sh FILE [OPTION]

with no options returns nothing
             
    --total           total number of requests

    --by-type TYPE    number of TYPE requests    

    --long            10 requests with the highest
                      value of content-length

    --loc-client      10 requests with the most frequent
                      location among requests with
                      a client error                    

    --long-server     10 requests with the highest
                      value of content-length among
                      requests with a server error
            

### python script
#### usage: checklogs.py FILE [OPTION]

with no options returns nothing

    --total           total number of requests

    --by-type TYPE    number of TYPE requests    

    --long            10 requests with the highest value
                      of content-length

    --loc-client      10 requests with the most frequent
                      location among requests with
                      a client error                

    --long-server     10 requests with the highest
                      value of content-length among 
                      requests with a server error
    
    --json            add results in json format
___

### Output
The results are saved to "results.txt" file. 
If --json option is set, it is  also saved to "results.json" file in json format.

  
