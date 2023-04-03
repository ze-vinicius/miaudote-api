class ErrorCode:
    AUTHENTICATION_REQUIRED = "authentication_required"
    AUTHORIZATION_FAILED = "authorization_failed_user_has_no_access"
    INVALID_TOKEN = "invalid_tokne"
    INVALID_CREDENTIALS = "invalid_credentials"
    EMAIL_TAKEN = "email_already_taken"
    REFRESH_TOKEN_NOT_VALID = "refresh_token_not_valid"
    REFRESH_TOKEN_REQUIRED = "refresh_token_is_required_either_in_the_body_or_cookie"
