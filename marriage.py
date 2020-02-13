"""Implementation of Gale-Shapley algorithm."""


def smp_converge(men_engage, women_engage):
    """Return True if there exists a couple that are unengaged."""
    return None in men_engage.values() or None in women_engage.values()


def propose(man, woman, women_pref, men_engage, women_engage):
    """Determine whether a proposal man to woman will be successful."""
    if women_engage[woman] is None:
        # If she has nobody, accept him.
        men_engage[man] = woman
        women_engage[woman] = man
        return

    # A second proposal should not occur.
    current_dude = women_engage[woman]
    assert current_dude != man

    # If this is an upgrade for her, accept him.
    if women_pref[woman].index(man) < women_pref[woman].index(current_dude):
        # If she has nobody, accept him.
        men_engage[man] = woman
        women_engage[woman] = man
        # Now the other dude has nobody. Rip.
        men_engage[current_dude] = None


def match_validate(men_engage, women_engage, men_pref, women_pref):
    """Ensure stability of correctness of SMP algorithm."""
    print('Checking symmetry and stability...')
    # Check symmetry of engagements.
    for man, his_gf in men_engage.items():
        assert women_engage[his_gf] == man
    for woman, her_bf in women_engage.items():
        assert men_engage[her_bf] == woman

    # Check stability.
    for man, his_pref in men_pref.items():
        current_woman = men_engage[man]
        # Does there exists a woman who he prefers more?
        for i in range(0, his_pref.index(current_woman)):
            # If so, does she also prefer HIM more?
            that_woman = his_pref[i]
            her_man = women_engage[that_woman]
            her_happiness = women_pref[that_woman].index(her_man)
            her_potential = women_pref[that_woman].index(man)
            # If this is true, she'd be happier with man that her current dude.
            if her_potential < her_happiness:
                print('Man {} is with woman {}. Woman {} is with man {}.'
                      .format(man, current_woman, that_woman, her_man))
                print('They\'d rather be with each other.')
                raise Exception('Matching is unstable.')


def compute_smp(men_pref, women_pref, check=True):
    """
    Compute a stable marriage on two preference lists.

    This function uses the Gale–Shapley algorithm.
    """
    print('Computing stable marriages...')

    # Hold onto the index each man is at.
    man_track = [0] * len(women_pref)

    # Initially, nobody is engaged to anybody else.
    men_engage = {man: None for man in men_pref.keys()}
    women_engage = {woman: None for woman in women_pref.keys()}

    # Iterate until convergence
    while smp_converge(men_engage, women_engage):
        # Each unengaged man proposes to the woman he prefers most.
        for index, man in enumerate(men_pref):
            # If this man is already engaged, move along.
            if men_engage[man] is not None:
                continue

            # Get this man's most preferred woman and increment tracker.
            mi_amor = men_pref[man][man_track[index]]
            man_track[index] += 1

            # Propose to her and make relevant state changes.
            propose(man, mi_amor, women_pref, men_engage, women_engage)

    # We should now have a stable matching.
    if check:
        match_validate(men_engage, women_engage, men_pref, women_pref)
    return men_engage, women_engage
