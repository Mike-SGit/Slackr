
# Demonstration of an understanding of the need for software verification and validation
# Development of appropriate acceptance criteria based on user stories and requirements.
# Demonstration of appropriate tool usage for assurance (code coverage, linting, etc.)


Verification and validation are 2 different analysis in software engineering.

Verification ensures the quality of the software. It checks whether the software meets the standard, whether it is free of bugs and whether the system has been built according to the requirements and specifications. Software components need to be tested and guaranteed to be able to run successfully.

Validation aims to make sure the software has met user?s actual needs. The software supposes to be able to fulfill user requirements and be useful to the users. The specification needs to be correct in the first place. For instance, if the user wants the product to be able to create a channel and start a standup, the product should have the function to satisfy the needs.


Email and password fields are placed at the top.
The fields have placeholder grey text: email and password.
The user cannot enter if the token is invalid.
The user cannot enter an unrecognised email format.
The user cannot enter an email already used by another user.
The user's password cannot be less than six characters long.
The user's first and last name must be between 1 and 50 characters long each.
The website produces a token for the user, which their browser sees.
The user recieves a new handle that is the joining of their first and last name.


The user presses a logout button when logged in.
If the users token is invalid, then they cannot logout.
If the users token is valid their token is then invalidated from further use.
The user is returned to the home screen when logged out.
They are prompted to log in again.


The user presses the 'Forgot my password' button.
The user enters their email into the email field.
An email containing a unique reset code for their account is sent to that email.
The user opens their email inbox and finds Slackr's sent email.
The user enters the code within the email into the 'reset code' field.
The user is prompted by a 'new password' field.
The user enters their new password into the field.
The user cannot enter one of their previous passwords.

The user presses the invite to channel button.
They are prompted by a 'User' field.
They enter a username into the field.
If the inviting user is not a member of the channel, they are denied.
The invited user is then a new member of the channel if otherwise successful.
If the invited user is already a member, this invite request is rejected.




