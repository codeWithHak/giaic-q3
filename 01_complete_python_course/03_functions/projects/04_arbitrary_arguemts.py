def main(prefix, *values):
    
    output = f'{prefix}: ['
    print('outpout in outerloop:',output)
    separator = ''
    print("separator in outerloop:",separator)
    for val in values:
        output+=separator
        output+=val
        separator = ', '
    output+="]"
    return output     
print(main('names','david', 'john'))


# names: [] if no sec args
# names: [john] if one sec arg
# names: [john, david] if more sec arg

