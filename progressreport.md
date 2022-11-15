# Title
Art classification

# Team members
Borano Llana, Nicholas Rommel, Carl Stoker

# Introduction

# Problem Definition
Art can be classified into many different genres and categories, across multiple mediums. The problem of determining the category of art something falls has no simple solution. This is a task that is often best left to the experts in the field. Though the issue of categorizing art will always be subjective at best, it may be possible to train a machine learning model to recognize these different genres of art and determine to what genre a new piece belongs.

We are attempting to classify different works of art into their respective genres. These include adstract, realism, as well as other categories. We will be including as many categories to our classifier as is feasible.

# Data

# Methods
The pipeline we will use to solve this problem is as follows:

1. Find or create a tagged and labeled dataset of art images
2. For each class of image:
   1. Train one-vs-all classifiers to distinguish that class from all others
   2. Run the classifiers on the validation set to select the best classifier
3. Select the best classifier for each class and combine them into a single meta-classifier
4. Run the meta-classifier on the test set to get the final results
5. Display the results to the user
