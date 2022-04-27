def not_string(str):
    if str[0:3] == 'not':
        return str
    return 'not ' + str

print(not_string('not bad'))
print(not_string('x'))