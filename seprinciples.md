## Refactoring...
## 1.  Changing multi-line variable declartions into a single line.  
    
  * Before:  
    ```
    email = request.form.get('email')  
    password = request.form.get('password')  
    nameFirst = request.form.get('name_first')  
    nameLast = request.form.get('name_last')  
    ```

  * After:  
    ```
    email, password, nameFirst, nameLast = (request.form[x] for x in ('email', 'password', 'name_first', 'name_last'))
    ```

  * Reasoning:  
    It maintains the reability of the former solution whilst also removing unnecessary code  
    that was originally very prevalent in nearly all routes.

## 2.  Abstraction of code into smaller functions.

  * Before:

    _server.py_
    ```
    @APP.route('/auth/logout', methods=['POST'])  
    def logout():  
        data = getData()  
        isSuccess = False  
        token = request.form.get('token')  
        checkTokenValidity(token, data)  
        
    if token in data['tokens']:  
        data['tokens'] = invalidateToken(token, data['tokens'])  
        isSuccess = True  
        
    return sendSuccess({  
        'is_success': isSuccess,  
    })      
    ```

  * After:  
 
    _server.py_
    ```
    from logout_helper import logoutFunc
    
    @APP.route('/auth/logout', methods=['POST'])  
    def logout():  
        data = getData()  
        token = request.form.get('token')  
        checkTokenValidity(token, data)  
        
        return sendSuccess({  
          'is_success': logoutFunc(data, token),  
        }) 
    ```
    
    _logout_helper.py_
    ```
    def logoutFunc(data, token):
        if token in data['tokens']:
            data['tokens'] = invalidateToken(token, data['tokens'])
            return True
        return False
    ```


  * Reasoning:  
    Since functions are now generally responsible for only one task with simple expected outputs,  
    the code is easier to maintain and test as it facilitates the unit-testing of smaller functions.  
    The code is also reusable and avoids taking up too much code space.  
    Adherence to 'DRY' (Don't Repeat Yourself) and the Single Responsibility Principle.  


## 3.  Top-down thinking
    
  * After:   

    _server.py_
    ```
    from auth_register_helper import createUser, emailExists, checkEmail, checkPassword, checkName, 
    createHandle, randomHandle, uniqueHandle, createU_ID, getUserFromToken, validUser
    
    @APP.route('/auth/register', methods=['POST'])
    def create():
        data = getData()
        email, password, nameFirst, nameLast = (request.form[x] for x in ('email', 'password', 'name_first', 'name_last'))
        
        handle = createHandle(nameFirst, nameLast)
        u_id = createU_ID(data) 
    
        if emailExists(email, data):
            raise ValueError ('Email entered is already being used.')
    
        handle = uniqueHandle(data, handle)
                
        checkEmail(email)
        checkPassword(password)
        checkName(nameFirst, nameLast)
    
        createUser(data, email, hashPassword(password), nameFirst, nameLast, handle, u_id, PERMISSION3)
    
        data['users'][0]['is_admin'] = PERMISSION1 
    
        data['tokens'].append(generateToken(u_id))
        print(data)
        
        return sendSuccess({
            'u_id': u_id,
            'token': generateToken(u_id),
        })
    ```
    
  * Reasoning:  
    Breaking down the large function into smaller, more achievable deliverables ensured that the process  
    was logically sound and the addition superfluous functionality was avoided.  
    It also made the code understandable for team members and easily extensible for future updates.


## 4.  Modularisation

  * After:

    @APP.route('/user/profile/setemail', methods=['PUT'])
    def setEmail():
      data = getData()
      email, token = (request.form[x] for x in ('email', 'token'))
      checkTokenValidity(token, data)
      user_profile_setemail(data, token, email)
      return sendSuccess({})

  * Reasoning:  
    Modularised the implementation funtions to make the project less rigid and fragile.
    Route funtions in the server.py will only take in the data, call the implementation funtion and return the outcome. Testability and mobility will be increased.


 ## 5.  Opacity

  * After:

    # Decode token to match user
    u_id = getUserFromToken(token)
    
    # Eroor checking
    req = requests.head(img_url)
    status = req.status_code
    if status != 200:
        raise ValueError("Invaild URL: HTTP status is not 200")
    elif img_url[-3:] != 'jpg':
        raise ValueError("Invaild URL: Not a JPG image")

    # Image down
    save_name = "./photo/" + str(u_id) + "photo.jpg"
    urllib.request.urlretrieve(img_url, save_name)

    # Error checking: Out of dimension
    data = requests.get(img_url).content
    im = Image.open(BytesIO(data))
    width, height = im.size
    if x_start < 0 or x_start > width or x_end < 0 or x_end > width or y_start < 0 or y_start > height or y_end < 0 or y_end > height:
        raise ValueError("Out of dimension")
    elif x_end <= x_start or y_end <= y_start:
        raise ValueError("x_start, y_start are left top corner; x_end, y_end are right bottom corner")
    ...
    ...

  * Reasoning:
    The code should be written in clean, clear and expressive manner..
    Add understandable comments and rename the variable name to avoid opacity.

