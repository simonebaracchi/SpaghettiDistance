# SpaghettiDistance
A context-aware set similarity (or distance) algorithm. Python2 and python3 compatible, no dependencies.

Spaghetti Distance is an alternative I developed to Jaccard similarity index.

It computes set distance or similarity attempting to keep context awareness, e.g. common set items (items that appear frequently across all sets) are less valuable when computing similarity.

https://spaghettiwires.com

**Usage**

    from SpaghettiDistance import SpaghettiDistance
    calculator = SpaghettiDistance()
    set1 = {'these', 'are', 'common', 'words'}
    set2 = {'also', 'these', 'are', 'very', 'common', 'words'}
    set3 = {'nearly', 'all', 'of', 'these', 'are', 'very', 'common', 'words'}
    calculator.add(set1)
    calculator.add(set2)
    calculator.add(set3)
    # set1 is made only of common words and thus they are worth nothing
    calculator.get_similarity(set1, set2)
    => 0.0
    # set2 and set3 share one uncommon word 
    calculator.get_similarity(set2, set3)
    => 0.11111111111111112

**Available functions**

    get_similarity(A, B, normalized=True)

Returns the similarity between A and B.
If "normalized" is True, the result is normalized between 0 (less similar) and 1 (more similar).
Otherwise, an unbounded float measuring the value of common items is returned.

    get_distance(A, B)

Returns the distance between A and B (1 - similarity).
The result is normalized between 0 (less distant) and 1 (more distant).

    get_items_value(a)

Returns the cumulative value of items in the set.

    add(items)

Add a new set to the context.

    forget(items)

Remove a set from the context.

