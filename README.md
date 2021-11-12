# Message-Gen
A script that allows you to create a picture with nicely formatted text, using the PIL module

# How to install?
```
$ git clone https://github.com/dawio/Message-Gen.git
$ cd Message-Gen
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

# How to use?
```python
from MessageGen.Gen import Message
from MessageGen.Helpers import Color, Size

msg = Message(
    header = "Simple Title",
    sub_header = "Simple desciption",
    image_size = Size(1920, 1920),
    message_size = Size(1080, 1080)
)
        
msg.save("output.png")
```

# Demo
```
$ python3 demo.py "This is a simple title" "Python is cool <3"
```
This will produce output like this:
![output](https://i.ibb.co/R7vB2rk/output.png)

## You can customize message by chaning arguments
```python
msg = Message(
    header = "Simple Title",
    sub_header = "Simple desciption",
    image_size = Size(1920, 1920),
    message_size = Size(1080, 1080)
)
```
Then run
```
$ python3 demo.py "This is a simple title" "Python is cool <3"
```
It will produce output like this:
![output](https://i.ibb.co/MRFK670/output.png)
  



