MINDS AND MACHINES FINAL PROJECT - CONNECT 4 AI

INTRODUCTION
Connect 4 has been a fun game that playground kids enjoy playing. What's less
commonly known is the fact that Connect 4 is also a solved game, which means
when played optimally, the one of the players (player 1 in this case) will be
able to guarantee a win. The reason why we have chosen this project is due to the
fact that we believe we are competent enough coders that could code up some
suboptimal but still very good AI that can beat most people (and also because
of that fateful coinflip that professor John made). We were also interested in
answering the questions of how AI works. This connects with the AGI presentations
we have done during the class.

PROGRAM
To make it short and simple, we have created a Connect 4 board class that is
capable of storing the game state, advancing from one game state to another
by placing tiles on the board, and "fancy" printing of the board state so it's
human readable/understandable when using the program. Other than these basic
features, our Connect 4 class is also capable of (poorly) evaluating whether a
game state is favorable for a certain player by counting the amount of connections
one can make. The evaluation function sounds good on paper but not as well when
demonstrated in practice.

The first draft of the AI simply picks the move that gives it the highest evaluator
score, which sometimes lead into situation where they miss the win even though
it is set up for a win with a connection of 3 and missing one.

The second draft of the AI attempts to harness more of the computation power of
a computer. It tries to run the minimax algorithm where our AI is trying to
maximize the score we are going to get while the AI's opponent will try to minimize
the score we are trying to get (as the opponent wants to win). We have also made
use of alpha-beta pruning in order to slightly cutdown on the amount of time
being spent on this expensive computation process.

RESULT
We originally had high hopes for our AI in the contest. However, two hours before
the contest our AI is still being very stubborn (missed multiple obvious wins
and cornered itself into a losing condition). The two hours of fixes wasn't helpful
so we at last got 5/6, which is not the last place so it's still good in some sense

DISCUSSION
As we have outlined in the introduction section, we hoped to have an AI which
is competent enough to put up a fight against people. However, we can see that
we are still a long way away from that particular goal. I believe one reason that
could have contributed to the subpar performance of the AI is due to the fact that
the AI only thinks about its moves but fails to consider opponent moves (our AI
can't really block another AI's almost winning move). It can also be because
our evaluator isn't as smart which makes the minimax not work as well it could be.
If we were to put more time on this project, I believe our first thing to fix is
to come up with a better evaluator, and then try to come up with better methods
to interact with the opponent's moves. It is also worth mentioning that even though
this is an AI, it's not the deep learning kind as it makes use of bruteforce
searching unlike most deep learning AI that makes use of lots of data.