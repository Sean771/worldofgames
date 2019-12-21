import html

# score_server - This function will serve the score. It will read the score from the scores file
# and will return an HTML that will be as follows:
class MainScores:
    pass
    def score_server(self):
        html_str_score = """
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is <div id="score">{SCORE}</div></h1>
            </body>
        </html>
        """
        html_str_error = """
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">{ERROR}</div></h1>
            </body>
        </html>
        """


