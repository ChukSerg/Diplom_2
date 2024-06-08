class ApiConstants:
    REGISTRATION_USER_URL = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    USER_URL = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    USER_LOGIN_URL = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    ORDER_URL = 'https://stellarburgers.nomoreparties.site/api/orders'
    INGREDIENTS_URL = 'https://stellarburgers.nomoreparties.site/api/ingredients'
    STATIC_USER = ['test_user_212@ya.ru', '111111', 'TestName']
    CREATE_TWO_SAME_MESSAGE = 'User already exists'
    CREATE_WITHOUT_FIELD_MESSAGE = 'Email, password and name are required fields'
    BAD_VALUE_FIELD_MESSAGE = 'email or password are incorrect'
    EMPTY_INGREDIENTS_MESSAGE = 'Ingredient ids must be provided'
    BAD_HASH_INGREDIENT_MESSAGE = 'One or more ids provided are incorrect'
    NON_AUTHORIZATION_MESSAGE = 'You should be authorised'
