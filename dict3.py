# dictionary with multiple inputs in a key
# function to add multiple values
def add_values_in_dict(dic, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in dic:
        dic[key] = list()
    dic[key].extend(list_of_values)
    return dic
 
# dictionary containing states and its cities
technologies = {("aws"):["IAM","S3BUCKET","VPC"],
          ("linux"):["cat","touch","vim"]}
 
print(technologies)
print('\n')

#adding values
add_val=add_values_in_dict(technologies, "aws", ["ALB", "Route53"])
add_val=add_values_in_dict(technologies, "scripting", ["python", "shell"])
print("After adding values")
print(add_val)
