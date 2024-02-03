from aux import scores


def score_server() -> tuple:
    """
    Read the score from the scores file and will return an HTML and status code.
    
    Returns:
        tuple(str, int): Response massege and status code.
    """
    try:
        SCORE = scores.read_score()
        response_msg = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is:</h1>
                <div id="score">{SCORE}</div>
            </body>
        </html>
        """
        response_code = 200
    except Exception as error:
        ERROR = str(error)
        response_msg = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>ERROR</h1>
                <div id="score" style="color:red">{ERROR}</div>
            </body>
        </html>
        """
        response_code = 500
    return response_msg, response_code
