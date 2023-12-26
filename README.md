The following is a set of scripts that I used to perform structure and parameter learning on a Bayesian network to generate synthetic smart card data for 
Brisbane's public transport network. Gratifyingly, the model worked pretty well, being able to replicate all major statistical features of the original dataset
remarkably well.

This is not production code and should not be used for anything important: there are some very hacky elements to this that should ideally be refactored, 
and they're mostly just scripts rather than a proper pipeline. Still, they might be of interest to some people, even if just as an example of how to use
bnlearn.

More information about the research that this was a part of can be found in the article below:

International Workshop on Agent-Based Modelling of Urban Systems (ABMUS) Proceedings: 2022 - Synthetic generation of individual transport data: the case of Smart Card data
