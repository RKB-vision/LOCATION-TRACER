import requests
def trace_ip():
    #PATH FOR BASE URL
    BASE_URL = "http://ip-api.com/json/"
    #INITIALIZING AN EMPTY LIST
    info=[]
    #REQUESTING THE SERVER  AND CONVERSION TO JSON
    try:
        while True:
            req=requests.get(BASE_URL+input("What is the public ip to trace? (Click Enter for using your own public ID)"))
            if req.status_code==200:
                response=req.json()
                if response["status"]!="fail":
                    #DISPLAYING THE RESULT OF REQUEST
                    for x in response:
                        if x != "status" and x != "org" and x != "query" and x!="zip":
                            info.append(f"{x}" " : " f"{response[x]}")
                    return info
                else:
                    print("INVALID IP! PROVIDE A CORRECT IP (eg. 8.8.8.8)")
                    continue

            else:
                print("FAILED TO COMMUNICATE WITH THE BASE URL.")
    except:
        print("CHECK THE BASE URL PROPERLY..IS IT CORRECT?")

if __name__=="__main__":
    info=trace_ip()
    for i in info:
        print(i)