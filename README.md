#Semi-Supervised Learning
This repository contains the semi-supervised learning (SSL) algorithms I
implemented as part of a course project. The course project used SSL to
classify sections of a text document, however the code to implement the algorithms
for that particular this task are not included in this repository. Rather, this repository includes the underyling algorithms used in the training process.

#Algorithms Implmented
1. Self training, which was originally proposed by Yarowsky [1], in which predictions are first made on the unlabeled data. Predictions with the highest confidence are then considered part of the labeled dataset, and the model is retrained with the additional labeled data [2].

2. Cluster-and-label [3], in which the entire data set is clustered using any standard clustering algorithm, and the unlabeled data points in each cluster are labeled by the majority vote of the labeled data points in that same cluster. Then the model can be retrained using the newly labeled data.

3. Finally, using the EM [4] algorithm, a more advanced generative model can be fit that includes unlabeled data [5].


#References
[1] D.Yarowsky,“Unsupervisedwordsensedisambiguationrivalingsuper- vised methods,” in Proceedings of the 33rd annual meeting on Asso- ciation for Computational Linguistics. Association for Computational Linguistics, 1995, pp. 189–196.
[2] O. Chapelle, B. Scho ̈lkopf, A. Zien, et al., “Semi-supervised learning,” 2006.
[3] X. Zhu, “Semi-supervised learning literature survey,” 2005.
[4] A. P. Dempster, N. M. Laird, and D. B. Rubin, “Maximum likelihood from incomplete data via the em algorithm,” Journal of the royal
statistical society. Series B (methodological), pp. 1–38, 1977.
[5] K. Nigam, A. K. McCallum, S. Thrun, and T. Mitchell, “Text clas- sification from labeled and unlabeled documents using em,” Machine
Learning, vol. 39, no. 2-3, pp. 103–134, May 2000.
