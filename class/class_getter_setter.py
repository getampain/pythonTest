class UserInfo:

    """
    getter setter 편하게좀 써보자
    userName
    userId
    userPassword
    """

    def __init__(self, newUserId="", newUserName="", newUserPassword= ""):
        #반드시 '__'를 붙여줘야 한다.
        self.__userName = newUserName
        self.__userId = newUserName
        self.__userPassword = newUserPassword

    #데코레이터를 붙여줌으로 값을 좀 편하게 쓴다.
    @property
    def userName(self):
        return self.__userName

    #setter 데코레이터를 붙여줌으로 값을 좀 편하게 쓴다.
    @userName.setter
    def userName(self, nameValue):
        self.__userName = nameValue 


if __name__ == "__main__":

    newUser = UserInfo("admin", "관리자", '1234')
    print(newUser.userName)
    newUser.userName  = "관리자_22"
    print(newUser.userName)




    