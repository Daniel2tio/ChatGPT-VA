# ChatGPT VA

This is a project based upon creating a Virtual Assistant that connects to a reverse engineered EdgeGPT API,  
who actively listens for a user's prompt using speech recognition and Amazon's Polly, turning it into a spoken response  
the same way a user would receive text using ChatGPT. 

## Installation

The program was written using Python 3.9.  
To install the dependencies, run the following command:  

```
 pip install -r requirements.txt  
```

Setting up AWS account to use Polly after installing dependencies:  

0 - Ensure that boto3 and awscli are properly installed  

1 - Create a new account on AWS or login  

2 - Select the profile icon and choose "Security Credentials"  

3 - Scroll down and create an access key, making sure to store both the key and secret key  

4 - Return to the command line and type "aws configure", this will prompt the configuration steps to follow  

https://github.com/aws/aws-cli#getting-started (package reference for further details)  

Upon completion of the configuration step and assuming all dependencies are installed, the program will run as the VA prompts the user to speak a wake up word (in this case it is set as Bing by default).  

The program will continue and listen for a prompt the user may give the same way it would type into ChatGPT.  




