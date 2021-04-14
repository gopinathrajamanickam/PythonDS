# Defang ip address
# given a valid ip address as a string replace all the dots to [.]

def defang(ip,seperator,new_separator):
    res = new_separator.join(ip.split(seperator))
    return res

if __name__ == "__main__":
    ip_addresses = ["12.1.23.11","11.23.55.66"]
    sep = "."
    new_sep = "[.]"
    for ip in ip_addresses:
        print("Defanged ip addresss for {0} is {1}.".format(ip,defang(ip,sep,new_sep)))
