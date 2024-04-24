class ProvidedCFGConfig:
    """
    CFG data provided in the assignment.

    Built from the CFG after left-recursion removal
    and the FIRST and FOLLOW table.

    ep. = epsilon
    """
    input_strings = [
        '(a+a)*a$',
        'a*(a/a)$',
        'a(a+a)$'
    ]
    rules = [
        'E',
        'Q',
        'T',
        'R',
        'F'
    ]
    parsing_table = {
        ('E', 'a'): 'TQ',
        ('E', '('): 'TQ',
        ('Q', '+'): '+TQ',
        ('Q', '-'): '-TQ',
        ('Q', '$'): 'ep.',
        ('Q', ')'): 'ep.',
        ('T', 'a'): 'FR',
        ('T', '('): 'FR',
        ('R', '+'): 'ep.',
        ('R', '-'): 'ep.',
        ('R', '*'): '*FR',
        ('R', '/'): '/FR',
        ('R', '$'): 'ep.',
        ('R', ')'): 'ep.',
        ('F', 'a'): 'a',
        ('F', '('): '(E)'
    }
