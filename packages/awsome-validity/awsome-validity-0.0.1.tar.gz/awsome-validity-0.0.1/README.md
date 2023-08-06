# awsome-validity  
The validity of the email,phone number,password ...

# usage  
> pip install awsome-validity  
```python
from validity import validate
check = validate.Validation()
# check what you want.  
check.validate_email('1111@qq.com') # True
check.validate_password('1111@qq.com') # True
check.validate_password('12345678899') # False
```

# todo
Further features will be added in the future.

# reference
> https://packaging.python.org/en/latest/tutorials/packaging-projects/