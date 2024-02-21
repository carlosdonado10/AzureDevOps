from requests import Response


def check_valid_server_response(response: Response, action_prompt: str) -> None:
    """
    Check that the response status code is valid. If not it will raise a meaningful error message
    :param response: Response object from an HTTP request
    :param action_prompt: Message that explains the action that is performed and could potentially fail. e.g., "create card"
    :return: None
    """

    if response.status_code != 200:
        raise ValueError(f'#check_valid_server_response: Unable to {action_prompt}, server returned a status: '
                         f'{response.status_code} because {response.text}!')
