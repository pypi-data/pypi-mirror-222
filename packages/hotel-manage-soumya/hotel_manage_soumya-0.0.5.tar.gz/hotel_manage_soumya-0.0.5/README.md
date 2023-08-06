# [HOTEL-MANAGE-SOUMYA](https://pypi.org/project/hotel-manage-soumya/) PYTHON LIBRARY

## Description:
[Hotel-manage-soumya](https://pypi.org/project/hotel-manage-soumya/) is a lightweight Python library designed to simplify and streamline the management of bookings, rooms, and users within Flask web applications. With its easy-to-use classes and methods, Hotel-manage-soumya provides a set of essential functionalities for handling booking reservations, room management, and user authentication.

## Key Features:
`Booking Class:` The Booking class allows users to manage booking reservations efficiently. It provides methods to create, update, and delete bookings, as well as retrieve booking details such as check in date, check out date, room number, total guests, guest Name, payment etc.

`Room Class:` The Room class offers a convenient way to manage room information. Users can add new rooms, delete rooms, update existing room details, and retrieve information like room type, number of beds, amenities, price, room description and availability.

`User Class:` The User class offers a convenient way to manage user information. Admin can add new user, delete user, update existing user details, and retrieve information like full name, username, email, role and phone. Admin create two type of user i.e Manager and Admin.


## Benefits:

`Easy Integration:` Hotel-manage-soumya is designed specifically for any python web applications, allowing smooth integration into existing projects.

`Time-Saving:` By providing pre-built classes and methods, Hotel-manage-soumya eliminates the need to write boilerplate code for common booking, room, and user tasks.

`Scalability:` Hotel-manage-soumya's modular design allows developers to extend its functionality to suit specific project requirements.

## Prerequisite
* Python >=3.7
* AWS Account
* DynamoDB connection
* Flask


## Installation
Install library using following command
```bash
  pip install hotel-manage-soumya
```

## Usage/Examples
Following Flask app will return the total number of bookings, total number of rooms and total number of users.

**`Note:`** Make sure you already have tables with data in DynamoDB and if you still face any issue then you can contact with us or explore the Class, Function from Github [Hotel-manage-soumya](https://github.com/soumyak96/hotel_manage_soumya) and directory `src/hotel_manage_soumya`.

```javascript
from flask import Flask
from dotenv import load_dotenv
import boto3
import os


// Import classes from hotel_manage_soumya
from hotel_manage_soumya.booking import Booking
from hotel_manage_soumya.room import Room
from hotel_manage_soumya.user import User

load_dotenv()
app = Flask(__name__)
app.secret_key = 'your_secret_key'

// Initialize the DynamoDB client
dynamodb =  boto3.client(
                'dynamodb', 
                aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                region_name=os.environ['AWS_REGION']
            )

// Initialize classes objects
tableName = 'bookings'
booking_obj = Booking(tableName)

roomTableName = 'rooms'
bucketName = 'hotel-management-soumya'
room_obj = Room(roomTableName, bucketName)

userTableName = 'users'
user_obj = User(userTableName)

@app.route('/', methods=['GET'])
def home():
    //  All Bookings
    all_booking = booking_obj.get_all_booking(dynamodb)
    total_booking = len(all_booking['data']['Items'])

    //  All Rooms
    all_rooms = room_obj.get_all_room(dynamodb)
    total_room = len(all_rooms['data']['Items'])

    //  All users
    all_users = user_obj.get_all_user(dynamodb)
    total_users = len(all_users['data']['Items'])
    
    return {
        "statusCode": 200,
        "TotalBooking": total_booking,
        "TotalRoom": total_room,
        "TotalUser": total_users
    }
```

#### Flask APP Response
```javascript
{
  "TotalBooking": 4,
  "TotalRoom": 4,
  "TotalUser": 3,
  "statusCode": 200
}

```


## Support

For support, email x21174059@student.ncirl.ie , soumyaksoochik96@gmail.com.





