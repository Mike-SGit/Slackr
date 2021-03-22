assumptions:

First names given to auth_register were strings of len > 0 (assumed that front end prevents null entry into first and last name sign up slots)

Channel_details returns an array type for owner_members and all_members as they are one continuos type and a dictionary is unneccesary

Channel_addowner allows the current owner to add a new owner who is not a current member of their channel
-> Assumed as this means the user does not need to waste time inviting the user then setting them as an owner

There is a method of finding the current user's u_id with only their token
-> Assumed as Channel_addowner needs to determine if the current user is in the target channel otherwise the user is assumed to be in the channel (this is leads to random users setting owners to random channels)

Assumed channel_create will have enough memory to succeed until further testing can be implemented in iteration 2

Assumed channel_list and channel_listall will have 'related information' about the channels clarified in iteration 2

Assumed message_sendlater will receive a time in datetime(yy/mm/dd/hh/ss) format to allow comparison to time functions in python
