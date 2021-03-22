## Approach
Since functions seem to be ordered categorically already, it would be advantageous
to distribute implementation of functions to developers by category, perhaps the 
same ones that we?ve written test cases for so that developers don?t waste time 
learning semantics of other functions unnecessarily
For example, one bucket might contain channel functions, while another might contain 
message functions and so on
For example, test functions were distribted as..
Functions to write tests for:	Assigned to:

Authentication - Ben
Channels - James
Messages - Mike
User profiles, search - Justin


It would be best to implement the same functions we've written tests for since we're 
familiar with how these functions should work.

## Timeline
It would be useful to have core functions that will be necessary for other functions 
to be finished in an early stage of iteration 2 such that other functions can be properly
implemented without having to wait or guess how a function might have to interact with the
core functions, for example, Auth_register, login, and channel_create. For this reason it 
may be useful to set weekly deadlines to ensure ample time is left to implement functions 
that depend on these core functions.


Week:	Expected finished functions


	Auth_login
    Auth_logout
    Auth_register
1   Channels_create
    Message_send
    user_profile

    Channel_addowner
2   Message_pin
    Message_react


2+  All functions not mentioned


Judging by the complexity of the functions shown in iteration one, implementation shouldnt 
take more than a few hours each week if spread evenly. As for tools, we will be using a messaging 
group to communicate what progress we?ve made which will supplement face to face weekly group meetings.

