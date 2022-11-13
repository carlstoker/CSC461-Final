# Title
Art classification

# Team members
Borano Llana, Nicholas Rommel, Carl Stoker

# Introduction

# Problem Definition

# Data

# Methods
The pipeline we will use to solve this problem is as follows:

1. Find or create a tagged and labeled dataset of art images
2. For each class of image, train a one-vs-all classifier to distinguish that class from all others
3. Run the classifiers on the validation set to select the best classifier
4. Select the best classifier for each class and combine them into a single meta-classifier
5. Run the meta-classifier on the test set to get the final results
6. Display the results to the user