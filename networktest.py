#C4D Network Test with Python - Ronak Parikh
#Here I am just testing the network with my secret string for
#the soda machine hosed on github.
import c4d
from c4d import gui
import urllib

def main():
    urlstr = "https://raw.githubusercontent.com/ronakstudios/sodamachine/ede1e663741be3c13396b3824ed0983da415d3ca/secret.txt"
    webworker = urllib.urlopen(urlstr)
    thatLine = webworker.readline()
    print(thatLine)
    
    #This is actually 100 times easier than Java:
    #You would have to account for throws declarations and have
    #BufferedReader and Exception Handling, having an interpreted
    #language like JS or Python for network calls just makes so much sense
    
   # gui.MessageDialog(thatLine)

# call my main method procedurally
if __name__=='__main__':
    main()
