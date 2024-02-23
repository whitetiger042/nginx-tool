# nginx-tool
This Tool would read a yaml file and create a nginx.conf
#----------------------------------------------
Purpose of the tool 
#----------------------------------------------

* Take input.yaml and create a gninx.conf as per custom requirement  

#----------------------------------------------
Steps to run the tool 

#----------------------------------------------

1> Clone the repository on local
2> Run this command to execute the code --> python3 tool.py
3> Check the output in nginx.conf

#----------------------------------------------
Function 1:

The script parses the given input.yaml file and exports variables inside it using a loops and saves them as a environment variable 

Function 2:
The function 2 picks these environment variables , nginx.conf , jinja template as arguements and parses the jinja template using the variables 

used a Jinja template for rendering the nginx.conf file 
