# Learn to create python packages

## Why __init__.py?

In older versions we would need a file named __init__.py in a folder to mark it as a package but in newer versions we dont neet it we can directly import from folders like:
\
```from utils.math_utils import add```  

## What's the purpose of still using __init__.py sometimes?
**First usecase:**  
When you need to run a code on import like  
__init__.py:  
```print("Imported math_utils")```

So this code will run on importing the module.

**Second usecase:**
Now your imports a bit dirty like what is this :

```from utils.math_utils import add```   
```from utils.math_utils import capitalize ```  

I ned clean imports so i will go in my __init__.py and write this:

``` from math_utils import add ```  
``` from math_utils import capitalize ```

But now it will throw an error that you are passing absolute paths but it need relative paths.

So now again go int __init__.py and write:

``` from .math_utils import math ```  
``` from .math_utils import capitalize ```

Just add a . in the start inside __init__.py and it will be fixed

