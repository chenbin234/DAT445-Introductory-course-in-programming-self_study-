import urllib.request as urllib
# use urllib.request to get the data from url

def main(url):
    print("checking connectivity")
    response = urllib.urlopen(url)
    print("connected to ", url, "successfully")
    print("The response code was: ",response.getcode())

print("This ia a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")
main(input_url)
