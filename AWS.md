# **AWS**



```
Setting up an AWS Account as a Root User:
        1. Visit the following URL: "https://aws.amazon.com/"
        2. Click on "Create an AWS Account" to open the "Sign up for AWS" screen.
        3. Enter your email address for the root user and provide an formal name for your AWS account. Click on "Verify email address."
        4. Check your Root user email for the verification code, and enter it in the appropriate field.
        5. Create a secure password for the root user, enter it in the "Root user password" field, and confirm it. Click on "Continue."
        6. Select the option "Personal - for your own projects" and provide the required information.
        7. Fill in your billing information, including your card number, as AWS requires it.
        8. Choose the "Basic support - Free" plan.
        9. Make sure to store the root user email and password in a secure place for future login purposes.
```


```
Setting up a Freelance Developer Account on AWS:
        1. Go to the top bar and search for "IAM." 
        2. Inside the "Access Management" section on the left sidebar, click on "Users." 
        3. Select "Add users." 
        4. Enter a "User name" and leave the option "Provide user access to the AWS Management Console" unchecked. Click "Next." 
        5. Choose "Attach policies directly." 
        6. Add the following AWS services by searching and selecting the corresponding permission policies:
                - Search for "IAMFullAccess" ad select it.
                - Search for "AmazonS3FullAccess" and select it.
                - Search for "AWSLambda_FullAccess" and select it.
                - Search for "AmazonEventBridgeFullAccess" and select it.
                - Search for "CloudWatchFullAccess" and select it.
        7. Click "Create user" to create a new user.
        8. Open the user dashboard by clicking on the newly created user. 
        9. Click on "Security credentials." 
        10. Enable console access. 
        11. Select "Enable" for Console access. 
        12. Choose a custom password (which will be shared with your remote developer). Do not check "User must create a new password." 
        13. Save the credentials either by copying them or exporting them as a CSV file. These credentials will be shared with the developer.
```



## **AWS Lambda**



```cmd
AWS Lambda deployment package with no dependency:
        1. Create new directory
	            $ mkdir my-lambda-function
	            $ cd my-lambda-function
        2. Create new lambda function code, and write code
	            $ touch lambda_function.py
        3. Build zip package
	            $ zip my-deployment-package.zip lambda_function.py
        4. Upload the zip file
```




```cmd
AWS Lambda deployment package with dependency:
        1. Create new directory
	            $ mkdir my-lambda-function
	            $ cd my-lambda-function
        2. Create new lambda function code, and write code
	            $ touch lambda_function.py
        3. Install library to a new "package" directory
	            $ pip install --target ./package requests
        4. Create a deployment package with the installed library at the root
	            $ zip -r ../my-deployment-package.zip .
        5. Add the lambda_function.py file to the root of the zip file
	            $ zip my-deployment-package.zip lambda_function.py
        6. Upload the zip file
```


```
AWS Lambda layers deployment:
        1. Create new directory
	            $ mkdir my-lambda-layers
	            $ cd my-lambda-layers
        2. Create a Python directory
                $ mkdir python
                $ cd python
        3. Install libraries
                $ pip install requests -t .
                $ pip install parsel -t .
        4. Create deployment package
                $ cd ..
                $ zip -r lambda_layer.zip python/
        5. Upload it on AWS Lambda layer and use it
```


