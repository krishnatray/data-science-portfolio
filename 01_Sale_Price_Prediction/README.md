Regression Case Study
======================

In today's exercise you'll get a chance to try some of what you've learned
about supervised learning on a real-world problem.

The goal of the contest is to predict the sale price of a particular piece of
heavy equipment at auction based on it's usage, equipment type, and
configuration.  The data is sourced from auction result postings and includes
information on usage and equipment configurations.


Version Control
=====================
Before you begin feature engineering and model building, you will need to establish
a workflow for your team. For this you will git and github! Version control is your friend.
The last thing you want at the end of the day is version proliferation with
multiple, conflicting versions of your code floating around on Slack, email or elsewhere.
Instead, you want one centralized repository of code that is version controlled
and shared between every member of your team. Here is a recommended workflow:

* Your team captain should fork the [case study repository](https://github.com/gSchool/dsi-regression-case-study). This will be your team's "upstream repo".
* All other team members should fork the upstream repo.
* Everyone clones their own forked repo to their own local machine.
* On your local machine, create and checkout a branch to work on: `git checkout -b <feature_name>`. This will be your feature branch. No one works on the master branch, not even the upstream owner.
* Do your work.
* Everytime you complete an atomic piece of work: `git add -p` `git commit -m` `git push origin <your feature branch>`
  * `git add -p` to interactively stage chunks of new/modified code. This is crucial to ensuring you commit only what you intend.
  * `git commit -m <something useful>`. Your commit messages serve as documentation and communication for your team.
  Example of a _good_ commit message: "add private method to feature engineering class to one-hot-encode categorical variables".
  Examples of a _useless_ commit message: "stuff", "commit", "bug fix".
  * `git push origin feature_1`, `git pull -r origin master`. Be explicit about which remote branch you want when you push/pull.
* Once a useful chunk of work is complete, issue a pull request to merge your branch with the upstream repo.
* The owner of the upstream repo can accept your pull request and merge it into the upstream master branch, then delete your feature branch.
* Iterate frequently.
* Avoid merge conflicts by working on separable areas of code and rebasing often `git pull -r origin master`.
* In the end, everything will be merged to the master branch in the upstream repo.  This will be your “production” code that everyone will have a copy of in the end.
* Consult the [github documentation](https://guides.github.com/introduction/flow/) if/when you get stuck.

Evaluation
======================
The evaluation of your model will be based on Root Mean Squared Log Error.
Which is computed as follows:

![Root Mean Squared Logarithmic Error](images/rmsle.png)

where *p<sub>i</sub>* are the predicted values and *a<sub>i</sub>* are the
target values.

Note that this loss function is sensitive to the *ratio* of predicted values to
the actual values, a prediction of 200 for an actual value of 100 contributes
approximately the same amount to the loss as a prediction of 2000 for an actual
value of 1000.  To convince yourself of this, recall that a difference of
logarithms is equal to a single logarithm of a ratio, and rewrite each summand
as a single logarithm of a ratio.

This loss function is implemented in score_model.py.

Setup
======================
Run `pip install git+https://github.com/gschool/dsi-performotron.git`.

Data
======================
The data for this case study are in `./data`. Although there are both training
and testing data sets, the testing data set will only be utilized to evaluate
your final model performance.  In other words, you should use cross-validation
on the training data set to identify potential models, then score those models
on the test data.

In order to score your model, you will need to output your predictions in the
format specified in `data/median_benchmark.csv`. Then you can submit your
solution for evaluation using the command:

    python score_model.py data/your_predictions.csv

Note that this will announce your score on Slack to everybody else, but feel
free to submit an early model to make sure you have a working model.

Be wary about scoring the test set too many times.  If you respond to your test
set loss by changing your model, you risk overfitting to the test set, which is
unrecoverable.  Overfitting to a test set can only be discovered after a model
has been productionalized.

Restrictions
============
When learning a predictive model, we would like you to use only *regression*
methods for this case study.  The following techniques are legal

  - Linear Regression.
  - Logistic Regression.
  - Median Regression (linear regression by minimizing the sum of absolute deviations).
  - Any other [GLM](http://statsmodels.sourceforge.net/devel/glm.html).
  - Regularization: Ridge and LASSO.

You may use other models or algorithms as supplements (for example, in feature
engineering), but your final submissions must be scores from a linear type
model.

Important Tips
=========================

1. This data is quite messy. Try to use your judgement about where your
cleaning efforts will yield the most results and focus there first.
2. Because of the restriction to linear models, you will have to carefully
consider how to transform continuous predictors in your model.
3. Remember any transformations you apply to the training data will also have
to be applied to the testing data, so plan accordingly.
4. Any transformations of the training data that *learn parameters* (for
example, standardization learns the mean and variance of a feature) must only
use parameters learned from the *training data*.
5. It's possible some columns in the test data will take on values not seen in
the training data. Plan accordingly.
6. Use your intuition to *think about where the strongest signal about a price
is likely to come from*. If you weren't fitting a model, but were asked to use
this data to predict a price what would you do? Can you combine the model with
your intuitive instincts?  This is important because it can be done *without
looking at the data*; thinking about the problem has no risk of overfitting.
7. Start simply. Fit a basic model and make sure you're able to get the
submission working then iterate to improve. Try to submit a model--even if you
know it has some weaknesses--within the first hour.
8. Remember that you are evaluated on a loss function that is only sensitive to
the *ratios* of predicted to actual values.  It's almost certainly too much of
a task to implement an algorithm that minimizes this loss function directly in
the time you have, but there are some steps you can take to do a good job of
it.
