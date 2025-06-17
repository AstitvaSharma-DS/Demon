from flask import Flask, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Score.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Sdata= SQLAlchemy(app)
class score(Sdata.Model):
    id = Sdata.Column(Sdata.Integer,primary_key=True)
    game = Sdata.column(Sdata.String(80), nullable=False)
    score = Sdata.Column(Sdata.Integer, nullable=False)
    def __repr__(self):
        return f"score('{self.id}','{self.game}', '{self.score}')"

@app.route('/flappy bird', methods=['GET', 'POST'])
def flappy_bird():
    if request.method == 'POST':
        game = request.form.get('game')
        score_value = request.form.get('score')
        if game and score_value:
            new_score = score(game=game, score=int(score_value))
            Sdata.session.add(new_score)
            Sdata.session.commit()
            return render_template('flappy_bird.html', message="Score saved successfully!")
    return render_template('flappy_bird.html')