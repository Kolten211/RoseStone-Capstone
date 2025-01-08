## CapStone API-docs

* Base URL: `/api`

## ALL routes that rewuire Authentication

- phrase
- Phrases
- Lessons
- User Progress

All endpoints that require a current user to be logged in.

* **Request**: endpoints that require authentication
* **Error Response**: Require authentication
  * **Status Code**: 401
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Authentication required"
    }
    

* **Request**: Endpoints that require proper authorization
* **Error Response**: Require proper authorization
  * **Status Code**: 403
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Forbidden"
    }
    ```


## Get Current User

 - **Require Auth**: False

 - **Request**:
    - **Method**: GET
    - Route Path: "/session"
    - **Body**: none
 - **Successful Response**:
    - status: 200
    - Headers
      - Content-Type: application/json ## Messages

      ### Create a Message

      ###  *Sets to this when/if you are returning a JSON response using jsonify()

    - **Body**:
    ```json
      {
         "user": {
            "id": 0,
            "username": "VolunteerLyfe",
            "email": "green4lyfe@planet.com",
            "firstName": "Susan",
            "lastName":"Markcul",
         }
      }
     ```

* **Successful Response**:when there is no logged in user.
  * **Status Code**: 200
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "user": "Null"
    }
    ```

### Log In a User

Logs in a current user with valid credentials and returns the current user's
information.

* **Require Authentication**: false
* **Request**
  * **Method**: POST
  * **Route path**: `/session`
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "credential": "green4lyfe@planet.com",
      "password": "secret password"
    }
    ```

* **Successful Response**
  * **Status Code**: 200
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "user": {
        "id": 1,
        "firstName": "Susan",
        "lastName": "Markcul",
        "email": "green4lyfe@planet.com",
        "username": "Volunteer4Lyfe",
        "createdAt": "2021-11-19 20:39:36",
        "updatedAt": "2021-11-19 20:39:36"
      }
    }
    ```

* **Error Response**: Invalid credentials
  * **Status Code**: 401
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Invalid credentials"
    }
    ```

* **Error response**: Body validation errors
  * **Status Code**: 400
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "credential": "Email or username is required",
        "password": "Password is required",
        "city": "City is required",
        "state": "State is required",
      }
    }
    ```

    ### Sign Up a User

Creates a new user, logs them in as the current user, and returns the current
user's information.

* **Require Authentication**: false
* **Request**
  * **Method**: POST
  * **Route path**: `/users`
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "firstName": "John",
      "lastName": "Smith",
      "email": "john.smith@gmail.com",
      "username": "JohnSmith",
      "password": "secret password"
    }
    ```

* **Successful Response**
  * **Status Code**: 201
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "user": {
        "id": 1,
        "firstName": "John",
        "lastName": "Smith",
        "email": "john.smith@gmail.com",
        "username": "JohnSmith",
        "createdAt": "2021-11-19 20:39:36",
        "updatedAt": "2021-11-19 20:39:36"
      }
    }
    ```

    * **Error response**: User already exists with the specified email or username
  * **Status Code**: 500
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "User already exists",
      "errors": {
        "email": "User with that email already exists",
        "username": "User with that username already exists"
      }
    }
    ```

* **Error response**: Body validation errors
  * **Status Code**: 400
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "email": "Invalid email",
        "username": "Username is required",
        "firstName": "First Name is required",
        "lastName": "Last Name is required"
      }
    }
    ```

## Events

### Get Lessons

Returns all the Lessons.

* **Require Authentication**: false
* **Request**
  * **Method**: GET
  * **Route path**: `/lessons`
  * **Body**: none

* **Successful Response**
  * **Status Code**: 200
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "Events": [
        {
          "id": 1,
          "title": "Help Us",
          "description": "Helping people",
          "word_id": 2,
          "phrase_id": 3,
          "status" : 0
        }
      ]
    }
    ```

### View User Lessons from Dashboard
  Returns all Lessons of the current user.

* **Require Authentication**: true
* **Request**
  * **Method**: GET
  * **Route path**: `/lessons/<int:user_id>`
  * **Body**: none

* **Successful Response**
  * **Status Code**: 200
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "Lessons": [
        {
          "id": 1,
          "title": "Help Us",
          "description": "Helping people",
          "lesson_words": ["Tacsi", "Farmasy"],
          "lesson_phrases": [],
          "createdAt": "2021-11-19 20:39:36",
          "updatedAt": "2021-11-19 20:39:36",
          "status" : 1
        }
      ]
    }
    ```
  
### Get details of a Lesson from an id

Returns the details of a lesson specified by its id.

* **Require Authentication**: false
* **Request**
  * **Method**: GET
  * **Route path**: `/lessons/<int:lesson_id>`
  * **Body**: none

* **Successful Response**
  * **Status Code**: 200
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "id": 1,
      "title": "Help Us",
      "description": "Helping people",
      "lesson_words": ["Tacsi", "Farmasy"],
      "lesson_phrases": ["I need a Tacsi", "ware is tha Farmasy"],
      "createdAt": "2021-11-19 20:39:36",
      "updatedAt": "2021-11-19 20:39:36",
      "status" : 1,
       "User": {
        "id": 1,
        "description": "Some stuff about the Creator",
        "username": "theCreator",
      }
    }
    ```

* **Error response**: Couldn't find Lesson with the specified id
  * **Status Code**: 404
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Lesson couldn't be found"
    }
    ```

### **Create an lesson**

Creates a new lesson and returns the newly created Event's information.

* **Require Authentication**: true
* **Request**
  * **Method**: POST
  * **Route path**: `/lessons`
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
        {
          "title": "Help Us",
          "description": "Helping people",
          "lesson_words": ["Tacsi"],
          "lesson_phrases": [],
        },
    ```

* **Successful Response**
  * **Status Code**: 201
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "id": 1,
      "title": "Help Us",
      "description": "Helping people",
      "lesson_words": ["Tacsi"],
      "lesson_phrases": [],
      "createdAt": "2021-11-19 20:39:36",
      "updatedAt": "2021-11-19 20:39:36",
      "status" : 0
    }
    ```
  
* **Error Response**: Validation errors**
  * **Status Code**: 400
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Bad Request",
      "errors": {
        "title": "Title is required",
        "description": "Description is required",
        "lesson_words": "Words are required"
      }
    }
    ```

### **Edit a Lesson**

Edits an Lesson if user is creator of Lesson.

* **Require Authentication**: true
* **Require Authorization**: User must be creator of Lesson to make edits
* **Request**
  * **Method**: PUT
  * **Route path**: `/lessons/<int:lesson_id>`
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
        {
          "title": "Help Us Help You",
          "description": "Helping Learn Together",
          "lesson_words": ["Tacsi", "Farmasy"],
          "lesson_phrases": [],
        },
    ```

* **Successful Response**
  * **Status Code**: 201
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "id": 1,
      "title": "Help Us Help You",
      "description": "Helping Learn Together",
      "lesson_words": ["Tacsi", "Farmasy"],
      "lesson_phrases": []
    }
    ```

* **Error Response**: **Validation errors**
  * **Status Code**: 400
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Bad Request",
      "errors": {
        "title": "Title is required",
        "description": "Description is required",
        "lesson_words": "Words are required"
      }
    }
    ```

### **Delete a Lesson**

Deletes an Event. Only the creator of the Event is allowed to delete it.

* **Require Authentication**: true
* **Require Authorization**: User must be the creator of the Lesson
* **Request**
  * **Method**: DELETE
  * **Route path**: `/lessons/<int:lesson_id>`
  * **Body**: none

* **Successful Response**
  * **Status Code**: 200
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Successfully deleted lesson"
    }
    ```

* **Error Response**: Lesson not found**
  * **Status Code**: 404
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Lesson not found"
    }
    ```

* **Error Response**: User not authorized**
  * **Status Code**: 403
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Forbidden"
    }
    ```

### View all learned words

Return all the Messages associated with an Event

* **Require Authentication**: true
* **Request**
  * **Method**: GET
  * **Route path**: `/words`
  * **Body**: none

* **Successful Response**:
  * **Status Code**: 200
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "Learned": [
        "Tacsi", 
        "Farmasy"
      ]
    }
    ```
* **Error response**: Couldn't find any learned words
  * **Status Code**: 404
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Nothing learned Yet"
    }
    ```

### Create a word

Creates word for a lesson and returns the newly created word/s information.

* **Require Authentication**: true
* **Require Authorization**: User must be logged in
* **Request**
  * **Method**: POST
  * **Route path**: `/word`
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
      {
        "words": "Jelo"
      }
    ```

* **Successful Response**
  * **Status Code**: 201
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "id": 1,
      "word":"Jelo"
    }
    ```

* **Error Response**: **Validation errors**
  * **Status Code**: 400
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Bad Request",
      "errors": {
        "word": "spelling is incorrect",
      }
    }
    ```

* **Error Response**: User is not logged in.
  * **Status Code**: 403
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Forbidden",
    }
    ```

### Edit a words 

Edits learned words.

* **Require Authentication**: true
* **Require Authorization**: User must be creator/learner of word to make edits
* **Request**
  * **Method**: PUT
  * **Route path**: `/word/<int:word_id>`
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
      {
        "word": "jelo"
      },
    ```

* **Successful Response**
  * **Status Code**: 201
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "id": 3,
      "word": "gelo"
    }
    ```

* **Error Response**: **Validation errors**
  * **Status Code**: 400
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Bad Request",
      "errors": {
        "message": "word has to have changed"
      }
    }
    ```

* **Error Response**: User not signed in
  * **Status Code**: 403
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Forbidden",
    }
    ```

* **Error Response**: Message not found
  * **Status Code**: 404
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "word": "word not found",
    }
    ```

### Delete a Word

Removes a Word

* **Require Authentication**: true
* **Require Authorization**: word must belong to the current user
* **Request**
  * **Method**: DELETE
  * **Route path**: `/word/<int:word_id>`
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "word_id": 2,
    }
    ```

* **Successful Response**
  * **Status Code**: 200
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Word removed seccessfully"
    }
    ```

* **Error response**: Couldn't find a Word with the specified id
  * **Status Code**: 404
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Word couldn't be found"
    }
    ```

### View all learned phrases

Return all the learned phrases associated with a lesson

* **Require Authentication**: true
* **Request**
  * **Method**: GET
  * **Route path**: `/phrase`
  * **Body**: none

* **Successful Response**:
  * **Status Code**: 200
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "Learned": [
        "I need a Tacsi", 
        "ware is tha Farmasy"
      ]
    }
    ```
* **Error response**: Couldn't find any learned phrase
  * **Status Code**: 404
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Nothing learned Yet"
    }
    ```

### Create a phrase

Creates Phrase for a lesson and returns the newly created Phrase/s information.

* **Require Authentication**: true
* **Require Authorization**: User must be logged in
* **Request**
  * **Method**: POST
  * **Route path**: `/phrase`
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
      {
        "phrase": "ware is tha bathroom"
      }
    ```

* **Successful Response**
  * **Status Code**: 201
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "id": 1,
      "phrase": "ware is tha bathroom"
    }
    ```

* **Error Response**: **Validation errors**
  * **Status Code**: 400
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Bad Request",
      "errors": {
        "phrase": "spelling is incorrect",
      }
    }
    ```

* **Error Response**: User is not logged in.
  * **Status Code**: 403
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Forbidden",
    }
    ```

### Edit a phrase 

Edits Message on Event page if user is creator.

* **Require Authentication**: true
* **Require Authorization**: User must be creator of Phrase to make edits
* **Request**
  * **Method**: PUT
  * **Route path**: `/phrase/<int:phrase_id>`
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
      {
        "Phrase": "ware is tha Farmasy"
      },
    ```

* **Successful Response**
  * **Status Code**: 201
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "id": 3,
      "Phrase": "ware is tha Farmasi"
    }
    ```

* **Error Response**: **Validation errors**
  * **Status Code**: 400
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Bad Request",
      "errors": {
        "message": "Phrase has to have changed"
      }
    }
    ```

* **Error Response**: User not signed in
  * **Status Code**: 403
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "message": "Forbidden",
    }
    ```

* **Error Response**: Phrase not found
  * **Status Code**: 404
  * **Headers**:
    * `Content-Type: application/json`
  * **Body**:
    ```json
    {
      "Phrase": "Phrase not found",
    }
    ```

### Delete a phrase

Removes a phrase

* **Require Authentication**: true
* **Require Authorization**: Phrase must belong to the current user
* **Request**
  * **Method**: DELETE
  * **Route path**: `/phrase/<int:phrase_id>`
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "Phrase_id": 2,
    }
    ```

* **Successful Response**
  * **Status Code**: 200
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Phrase removed seccessfully"
    }
    ```

* **Error response**: Couldn't find a Phrase with the specified id
  * **Status Code**: 404
  * **Headers**:
    * ```Content-Type: application/json```
  * **Body**:

    ```json
    {
      "message": "Phrase couldn't be found"
    }
    ```