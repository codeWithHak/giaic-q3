# see here we gave last_name a default value so if user forget to put last name in arguement the code will not throw an error
# but the first name is not optional its mandatory
# we gave empty string as default vlaue but we can assign any value as default like: ``` last_name="khan" ```

def main(first_name, last_name=""):
    print(first_name + " " + last_name)

# these both will work
main("Huzair")
main("Huzair","Ahmed")

#this will throw an error becaus first name is mandatory
""" main() """ #Error: TypeError: main() missing 1 required positional argument: 'first_name'
    