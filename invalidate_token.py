def invalidateToken(token, tokenList):
    # Tokens are invalidated by removing all occurances from the tokenList
    while token in tokenList: 
        tokenList.remove(token)
    return tokenList